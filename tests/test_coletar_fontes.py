"""Verifica preservação de fontes, cobertura de refs e estados vazios do inventário."""
import importlib.util
import json
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path

MODULE_PATH = Path(__file__).resolve().parents[1] / "scripts/coletar_fontes.py"
spec = importlib.util.spec_from_file_location("coletar_fontes", MODULE_PATH)
collector = importlib.util.module_from_spec(spec)
spec.loader.exec_module(collector)


def minimal_pdf():
    stream = b"BT /F1 12 Tf 30 100 Td (TCC fixture) Tj ET"
    objects = [b"<< /Type /Catalog /Pages 2 0 R >>",
               b"<< /Type /Pages /Kids [3 0 R] /Count 1 >>",
               b"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 200 200] /Resources << /Font << /F1 4 0 R >> >> /Contents 5 0 R >>",
               b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>",
               b"<< /Length " + str(len(stream)).encode() + b" >>\nstream\n" + stream + b"\nendstream"]
    data = b"%PDF-1.4\n"
    offsets = [0]
    for index, obj in enumerate(objects, 1):
        offsets.append(len(data))
        data += f"{index} 0 obj\n".encode() + obj + b"\nendobj\n"
    start = len(data)
    data += b"xref\n0 6\n0000000000 65535 f \n"
    data += b"".join(f"{offset:010d} 00000 n \n".encode() for offset in offsets[1:])
    return data + f"trailer\n<< /Size 6 /Root 1 0 R >>\nstartxref\n{start}\n%%EOF\n".encode()


class CollectorTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="tcc escrita teste ")
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name)
        self.repo = self.base / "fonte com espaços"
        self.repo.mkdir()
        self.git("init", "-b", "main")
        self.git("config", "user.name", "Autor de teste")
        self.git("config", "user.email", "fixture@example.invalid")
        (self.repo / "README.md").write_text("Base\n", encoding="utf-8")
        self.commit("Início — evidência")

    def git(self, *args):
        return subprocess.check_output(["git", "-C", str(self.repo), *args], stderr=subprocess.PIPE).decode().strip()

    def commit(self, message):
        self.git("add", ".")
        self.git("commit", "-m", message)
        return self.git("rev-parse", "HEAD")

    def test_all_refs_merges_and_full_messages(self):
        self.git("checkout", "-b", "feature")
        (self.repo / "decisão.md").write_text("Uma decisão\n")
        feature = self.commit("Feature\n\nJustificativa detalhada.")
        self.git("checkout", "main")
        (self.repo / "main.md").write_text("Outra mudança\n")
        self.commit("Trabalho independente")
        self.git("merge", "--no-ff", "feature", "-m", "Merge")
        self.git("checkout", "feature")
        (self.repo / "só-na-branch.md").write_text("Ainda não integrada\n")
        only_branch = self.commit("Fora do HEAD principal")
        self.git("checkout", "main")
        records = collector.history(self.repo)
        self.assertEqual(len(records), int(self.git("rev-list", "--all", "--count")))
        self.assertIn(only_branch, {r["sha"] for r in records})
        self.assertTrue(any(len(r["pais"]) == 2 for r in records))
        record = next(r for r in records if r["sha"] == feature)
        self.assertIn("Justificativa detalhada.", record["mensagem"])
        self.assertIn("decisão.md", record["arquivos"])

    def test_empty_csv_and_untracked_are_preserved(self):
        (self.repo / "tentativas.csv").write_text("caso_id,R,F,M\n")
        (self.repo / "metricas.csv").write_text("metrica,valor,denominador\nTRV,,0\n")
        (self.repo / ".env").write_text("FIXTURE_SECRET=never_collect\n")
        records = list(collector.inventory(self.repo, "teste", ["*"]))
        by_name = {r["arquivo"]: r for r in records}
        self.assertEqual(by_name["tentativas.csv"]["linhas_dados"], 0)
        self.assertEqual(by_name["metricas.csv"]["linhas_dados"], 1)
        self.assertFalse(by_name["tentativas.csv"]["rastreado_git"])
        self.assertNotIn(".env", by_name)

    def test_external_symlink_is_rejected(self):
        outside = self.base / "outside.md"
        outside.write_text("outside")
        (self.repo / "link.md").symlink_to(outside)
        with self.assertRaisesRegex(ValueError, "symlink"):
            list(collector.inventory(self.repo, "teste", ["*.md"]))

    def test_local_configuration_takes_precedence(self):
        self.assertEqual(collector.default_config(self.base), self.base / "fontes.json")
        local = self.base / "fontes.local.json"
        local.write_text("{}")
        self.assertEqual(collector.default_config(self.base), local)

    def test_empty_child_directory_cannot_impersonate_parent_git(self):
        empty = self.repo / "experimento-ainda-nao-clonado"
        empty.mkdir()
        with self.assertRaisesRegex(ValueError, "raiz de um clone próprio"):
            collector.metadata(empty)

    def test_missing_required_repository_has_actionable_error(self):
        with self.assertRaisesRegex(ValueError, "Repositório obrigatório ausente: experimento"):
            collector.resolve_repositories({"repositorios": {"experimento": "nao-clonado"}}, self.base)

    @unittest.skipUnless(shutil.which("pdftotext"), "requer Poppler")
    def test_nested_layout_works_without_optional_poc(self):
        writing = self.base / "escrita"
        writing.mkdir()
        def writer_git(*args):
            return subprocess.check_output(["git", "-C", str(writing), *args], stderr=subprocess.PIPE)
        writer_git("init", "-b", "main")
        writer_git("config", "user.name", "Autor de teste")
        writer_git("config", "user.email", "fixture@example.invalid")
        project = MODULE_PATH.parents[1]
        (writing / "fontes.json").write_bytes((project / "fontes.json").read_bytes())
        (writing / ".gitignore").write_bytes((project / ".gitignore").read_bytes())
        writer_git("add", "fontes.json", ".gitignore")
        writer_git("commit", "-m", "Configuração da escrita")
        config = json.loads((writing / "fontes.json").read_text())
        nested = writing / config["repositorios"]["experimento"]
        subprocess.run(["git", "clone", str(self.repo), str(nested)], check=True, capture_output=True)
        (writing / config["pdf_tcc1"]).write_bytes(minimal_pdf())
        self.assertEqual(writer_git("status", "--porcelain").strip(), b"")
        output = writing / "evidencias/coleta"
        collector.collect(writing / "fontes.json", output)
        manifest = json.loads((output / "manifesto.json").read_text())
        self.assertEqual(set(manifest["repositorios"]), {"experimento", "escrita"})
        self.assertEqual(manifest["repositorios"]["experimento"]["head"], self.git("rev-parse", "HEAD"))
        self.assertEqual(manifest["repositorios_opcionais_ausentes"]["poc"]["motivo"], "nao_encontrado")
        self.assertFalse((output / "git-poc.jsonl").exists())
        self.assertEqual(manifest["pdf"]["paginas"], 1)

    @unittest.skipUnless(shutil.which("pdftotext"), "requer Poppler")
    def test_collection_is_read_only_and_refuses_overwrite(self):
        pdf = self.base / "fonte.pdf"
        pdf.write_bytes(minimal_pdf())
        config = self.base / "fontes.json"
        config.write_text(json.dumps({"pdf_tcc1": "fonte.pdf", "repositorios": {"teste": self.repo.name},
                                     "documentos": ["*.md"], "artefatos": []}))
        before = collector.metadata(self.repo)
        output = self.base / "coleta"
        collector.collect(config, output)
        manifest_bytes = (output / "manifesto.json").read_bytes()
        manifest = json.loads(manifest_bytes)
        self.assertEqual(manifest["pdf"]["paginas"], 1)
        self.assertEqual(manifest["pdf"]["sha256"], collector.sha(pdf.read_bytes()))
        self.assertIn("TCC fixture", (output / "tcc1.txt").read_text())
        self.assertEqual(before, collector.metadata(self.repo))
        with self.assertRaisesRegex(ValueError, "já existe"):
            collector.collect(config, output)
        self.assertEqual(manifest_bytes, (output / "manifesto.json").read_bytes())
        for name, digest in manifest["gerados_sha256"].items():
            self.assertEqual(digest, collector.sha((output / name).read_bytes()))


if __name__ == "__main__":
    unittest.main()
