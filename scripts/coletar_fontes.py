#!/usr/bin/env python3
"""Inventaria fontes locais sem executar experimentos nem modificar os repositórios fonte."""
from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import re
import shutil
import subprocess
import tempfile
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def run(args, *, data=None):
    return subprocess.run(args, input=data, stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE, check=True).stdout


def git(repo, *args):
    return run(["git", "--no-optional-locks", "-C", str(repo), *args])


def decode(data):
    return data.decode("utf-8", errors="replace")


def sha(data):
    return hashlib.sha256(data).hexdigest()


def write_json(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def write_jsonl(path, rows):
    with path.open("w", encoding="utf-8") as f:
        for row in rows:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")


def history(repo):
    commits = []
    revisions = decode(git(repo, "rev-list", "--all", "--reverse", "--topo-order")).splitlines()
    for revision in revisions:
        parts = decode(git(repo, "show", "-s", "--format=%H%x00%P%x00%aI%x00%cI%x00%an%x00%B", revision)).split("\0", 5)
        files = decode(git(repo, "diff-tree", "--root", "-m", "--no-commit-id",
                           "--name-only", "-r", "-z", revision)).split("\0")
        commits.append(dict(zip(("sha", "pais", "data_autor", "data_commit", "autor", "mensagem"), parts)))
        commits[-1]["pais"] = parts[1].split()
        commits[-1]["mensagem"] = parts[5].strip()
        commits[-1]["arquivos"] = sorted(set(filter(None, files)))
    return commits


def metadata(repo):
    toplevel = Path(decode(git(repo, "rev-parse", "--show-toplevel")).strip()).resolve()
    if toplevel != repo.resolve():
        raise ValueError(f"{repo} não é a raiz de um clone próprio; o Git encontrado pertence a {toplevel}")
    return {
        "head": decode(git(repo, "rev-parse", "HEAD")).strip(),
        "shallow": decode(git(repo, "rev-parse", "--is-shallow-repository")).strip() == "true",
        "refs": decode(git(repo, "for-each-ref", "--format=%(refname) %(objectname)")).splitlines(),
        "status_porcelain": decode(git(repo, "status", "--porcelain=v1", "--untracked-files=all")).splitlines(),
    }


def default_config(root=ROOT):
    local = root / "fontes.local.json"
    return local if local.is_file() else root / "fontes.json"


def resolve_repositories(config, base):
    required = config["repositorios"]
    optional = config.get("repositorios_opcionais", {})
    if required.keys() & optional.keys():
        raise ValueError("Um repositório não pode ser obrigatório e opcional ao mesmo tempo")
    configured = {**required, **optional}
    if not all(re.fullmatch(r"[a-z0-9_-]+", name) for name in configured):
        raise ValueError("IDs de repositório devem conter apenas a-z, 0-9, _ ou -")
    repos, missing = {}, {}
    for name, value in configured.items():
        path = (base / value).resolve()
        if not path.exists():
            if name in optional:
                missing[name] = {"caminho_configurado": value, "motivo": "nao_encontrado"}
                continue
            raise ValueError(f"Repositório obrigatório ausente: {name} ({path}); clone a fonte ou ajuste a configuração")
        repos[name] = path
    return repos, missing, configured


def inventory(repo, repo_id, patterns):
    tracked = set(filter(None, decode(git(repo, "ls-files", "-z")).split("\0")))
    selected = sorted({p for pattern in patterns for p in repo.glob(pattern) if p.is_file()})
    for path in selected:
        # Do not follow sources outside a configured repository.
        if not path.resolve().is_relative_to(repo):
            raise ValueError(f"Fonte externa por symlink: {path}")
        rel = path.relative_to(repo).as_posix()
        if any(part in {".git", ".env", "node_modules", ".venv"} for part in path.relative_to(repo).parts):
            continue
        before = path.stat()
        content = path.read_bytes()
        after = path.stat()
        if (before.st_size, before.st_mtime_ns) != (after.st_size, after.st_mtime_ns):
            raise ValueError(f"Fonte mudou durante leitura: {path}")
        row = {"repositorio": repo_id, "arquivo": rel, "sha256": sha(content),
               "bytes": len(content), "rastreado_git": rel in tracked}
        if path.suffix == ".csv":
            reader = csv.DictReader(io.StringIO(content.decode("utf-8-sig")))
            row.update(colunas=reader.fieldnames, linhas_dados=sum(1 for _ in reader))
        elif path.name == "execucoes.jsonl":
            records = [json.loads(line) for line in content.splitlines() if line.strip()]
            row.update(registros=len(records), casos_distintos=len({r.get("caso_id") for r in records}))
        yield row


def collect(config_path, destination):
    config_bytes = config_path.read_bytes()
    config = json.loads(config_bytes)
    base = config_path.parent
    if destination.exists():
        raise ValueError(f"Saída já existe; escolha uma coleta nova: {destination}")
    repos, missing, configured = resolve_repositories(config, base)
    pdf = (base / config["pdf_tcc1"]).resolve()
    if not pdf.is_file():
        raise ValueError(f"PDF ausente: {pdf}; copie o TCC1 para esse caminho ou ajuste a configuração")
    if not shutil.which("pdftotext"):
        raise ValueError("pdftotext indisponível (pacote poppler-utils)")
    initial = {name: metadata(repo) for name, repo in repos.items()}
    destination.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix=".coleta-", dir=destination.parent) as temp:
        stage = Path(temp) / "dados"
        stage.mkdir()
        source_pdf = pdf.read_bytes()
        # Extract the exact bytes whose hash is recorded, not a potentially changing source.
        pdf_copy = Path(temp) / "fonte.pdf"
        pdf_copy.write_bytes(source_pdf)
        extracted = decode(run(["pdftotext", "-layout", str(pdf_copy), "-"]))
        pages = extracted.split("\f")
        if not pages[-1].strip():
            pages.pop()
        write_jsonl(stage / "tcc1.paginas.jsonl", [
            {"pagina_pdf": i, "texto": page} for i, page in enumerate(pages, 1)
        ])
        extracted_markdown = "\n\n".join(f"## Página PDF {i}\n\n{page.rstrip()}" for i, page in enumerate(pages, 1))
        (stage / "tcc1.txt").write_text(extracted_markdown + "\n", encoding="utf-8")
        patterns = config["documentos"] + config["artefatos"]
        source_rows = []
        counts = {}
        for name, repo in repos.items():
            commits = history(repo)
            counts[name] = len(commits)
            write_jsonl(stage / f"git-{name}.jsonl", commits)
            table = [f"# Histórico local — {name}", "", "Todos os commits alcançáveis por refs locais, em ordem topológica reversa.",
                     "Mensagens são índices para investigação; os diffs não foram auditados integralmente.", "",
                     "| Commit | Data do autor | Evolução registrada |", "|---|---|---|"]
            for c in commits:
                subject = c["mensagem"].splitlines()[0] if c["mensagem"] else "(sem mensagem)"
                table.append(f"| `{c['sha']}` | {c['data_autor']} | {subject.replace('|', '/')} |")
            (stage / f"git-{name}.md").write_text("\n".join(table) + "\n", encoding="utf-8")
            if name != "escrita":
                source_rows.extend(inventory(repo, name, patterns))
        write_jsonl(stage / "arquivos.jsonl", source_rows)
        changed = [name for name, repo in repos.items() if metadata(repo) != initial[name]]
        if changed:
            raise ValueError(f"Git mudou durante coleta: {changed}; repita em nova saída")
        # Recheck hashes to reject mixed snapshots from an active experiment.
        for row in source_rows:
            if sha((repos[row["repositorio"]] / row["arquivo"]).read_bytes()) != row["sha256"]:
                raise ValueError(f"Arquivo mudou durante coleta: {row['arquivo']}")
        generated = {p.name: sha(p.read_bytes()) for p in sorted(stage.iterdir())}
        manifest = {
            "schema": 1, "coletado_em_utc": datetime.now(timezone.utc).isoformat(),
            "configuracao": config, "configuracao_sha256": sha(config_bytes),
            "escopo_git": "git rev-list --all; sem fetch; sem objetos inalcançáveis/reflog; sem histórico upstream do Juice Shop",
            "limite": "Inventário de arquivos pelos padrões configurados; não é cópia integral dos artefatos nem auditoria de todos os diffs.",
            "pdf": {"arquivo": config["pdf_tcc1"], "sha256": sha(source_pdf), "paginas": len(pages),
                    "extrator": decode(subprocess.run(["pdftotext", "-v"], capture_output=True).stderr).splitlines()[0]},
            "repositorios": {name: {**initial[name], "caminho_configurado": configured[name],
                                     "commits": counts[name]} for name in repos},
            "repositorios_opcionais_ausentes": missing,
            "arquivos_inventariados": len(source_rows), "gerados_sha256": generated,
        }
        write_json(stage / "manifesto.json", manifest)
        stage.rename(destination)
    print(json.dumps({"saida": str(destination), "commits": counts, "paginas_pdf": len(pages),
                      "arquivos": len(source_rows), "opcionais_ausentes": sorted(missing)}, ensure_ascii=False))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=Path, help="Configuração explícita; padrão: fontes.local.json se existir, senão fontes.json")
    parser.add_argument("--saida", type=Path, required=True, help="Diretório novo, relativo à raiz de escrita")
    args = parser.parse_args()
    try:
        collect((args.config or default_config()).resolve(), (ROOT / args.saida).resolve())
    except (OSError, ValueError, subprocess.CalledProcessError) as exc:
        parser.exit(1, f"ERRO: {exc}\n")


if __name__ == "__main__":
    main()
