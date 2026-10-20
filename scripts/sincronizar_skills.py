#!/usr/bin/env python3
"""Publica as skills canônicas do Codex em .claude/skills e detecta divergências."""
import argparse
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Somente verificar, sem escrever")
    args = parser.parse_args()
    source = ROOT / ".agents/skills"
    target = ROOT / ".claude/skills"
    expected = {p.relative_to(source): p.read_bytes() for p in source.rglob("*") if p.is_file()}
    if not expected:
        parser.exit(1, "ERRO: nenhuma skill canônica encontrada\n")
    existing = {p.relative_to(target) for p in target.rglob("*") if p.is_file()}
    extras = existing - expected.keys()
    if extras:
        parser.exit(1, f"Arquivos exclusivos do Claude: {sorted(map(str, extras))}; revise manualmente, sem exclusão automática.\n")
    differences = [rel for rel, content in expected.items()
                   if not (target / rel).is_file() or (target / rel).read_bytes() != content]
    if args.check and differences:
        parser.exit(1, f"Skills divergentes: {sorted(map(str, differences))}\n")
    for rel in differences:
        path = target / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(expected[rel])
    print(f"{len(list(source.glob('*/SKILL.md')))} skills: " + ("espelhos conferidos" if args.check else f"{len(differences)} arquivos sincronizados"))


if __name__ == "__main__":
    main()
