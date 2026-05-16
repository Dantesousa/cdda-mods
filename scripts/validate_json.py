#!/usr/bin/env python3
"""
validate_json.py

Valida recursivamente todos os arquivos .json em um diretório.
Reporta erros de sintaxe com linha e coluna.
Retorna exit code 0 se todos forem válidos, 1 caso contrário.

Uso:
    ./scripts/validate_json.py
    ./scripts/validate_json.py /caminho/para/outro/dir
"""

import argparse
import json
import sys
from pathlib import Path


def validate_json_file(path: Path) -> bool:
    """
    Lê e valida a sintaxe de um único arquivo JSON.

    Args:
        path: Caminho do arquivo a ser validado.

    Returns:
        True se o JSON for válido, False caso contrário.
    """
    try:
        with path.open("r", encoding="utf-8") as f:
            content = f.read()
        json.loads(content)
        return True
    except json.JSONDecodeError as exc:
        # json.JSONDecodeError fornece lineno e colno da falha
        print(f"ERRO: {path}")
        print(f"  -> Linha {exc.lineno}, Coluna {exc.colno}: {exc.msg}")
        return False
    except OSError as exc:
        print(f"ERRO: {path}")
        print(f"  -> Não foi possível ler o arquivo: {exc}")
        return False


def main() -> int:
    """
    Ponto de entrada principal do script.

    Returns:
        0 se nenhum erro for encontrado, 1 caso contrário.
    """
    parser = argparse.ArgumentParser(
        description="Valida arquivos JSON recursivamente."
    )
    parser.add_argument(
        "directory",
        nargs="?",
        default="/home/dante/cdda-mods",
        help="Diretório raiz para busca recursiva (default: /home/dante/cdda-mods)",
    )
    args = parser.parse_args()

    root = Path(args.directory).resolve()
    if not root.is_dir():
        print(f"ERRO: Diretório não encontrado: {root}", file=sys.stderr)
        return 1

    has_errors = False
    found_any = False

    # rglob('*.json') percorre recursivamente todos os arquivos .json
    for json_path in root.rglob("*.json"):
        # Exclui arquivos dentro de qualquer subdiretório .git/
        if ".git" in json_path.parts:
            continue

        found_any = True
        if not validate_json_file(json_path):
            has_errors = True

    if not found_any:
        print(f"Nenhum arquivo .json encontrado em {root}")
        return 0

    if has_errors:
        print("\nFalha na validação de JSON.")
        return 1

    print(f"Todos os arquivos JSON em {root} são válidos.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
