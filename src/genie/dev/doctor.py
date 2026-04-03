from __future__ import annotations

import argparse
import platform
import shutil
import subprocess
import sys
from typing import Callable

from genie import __version__
from genie.dev import architecture_check


def _run_check(name: str, check: Callable[[], tuple[bool, str]], required: bool) -> bool:
    ok, detail = check()
    if ok:
        status = "OK"
    elif required:
        status = "FAIL"
    else:
        status = "WARN"
    print(f"[{status}] {name}: {detail}")
    return ok or (not required)


def _check_python_version() -> tuple[bool, str]:
    version_info = sys.version_info
    ok = version_info >= (3, 11)
    return ok, f"{version_info.major}.{version_info.minor}.{version_info.micro}"


def _check_package_version() -> tuple[bool, str]:
    return True, f"genie-platform {__version__}"


def _check_cli_script(name: str) -> tuple[bool, str]:
    path = shutil.which(name)
    if path:
        return True, path
    return False, "nicht gefunden"


def _check_pyside6_import() -> tuple[bool, str]:
    command = [sys.executable, "-c", "import PySide6; print('ok')"]
    result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode == 0:
        return True, "importierbar"

    stderr = (result.stderr or "").strip()
    if stderr:
        return False, f"Import fehlgeschlagen ({stderr.splitlines()[-1]})"
    return False, "Import fehlgeschlagen (unbekannter Fehler)"


def _check_architecture_guards() -> tuple[bool, str]:
    exit_code = architecture_check.main()
    if exit_code == 0:
        return True, "Contract/Boundary-Tests grün"
    return False, f"Architecture-Check ExitCode={exit_code}"


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Genie Doctor")
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Behandelt optionale Checks (z. B. PySide6 Import) als verpflichtend.",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    print("Genie Doctor")
    print(f"Platform: {platform.system()} {platform.release()}")

    pyside_required = args.strict
    checks: list[tuple[str, Callable[[], tuple[bool, str]], bool]] = [
        ("Python >= 3.11", _check_python_version, True),
        ("Package Version", _check_package_version, True),
        ("CLI 'genie'", lambda: _check_cli_script("genie"), True),
        (
            "CLI 'genie-architecture-check'",
            lambda: _check_cli_script("genie-architecture-check"),
            True,
        ),
        ("PySide6 Import", _check_pyside6_import, pyside_required),
        ("Architecture Guards", _check_architecture_guards, True),
    ]

    results = [_run_check(name, check, required) for name, check, required in checks]
    if all(results):
        print("Doctor Ergebnis: OK")
        return 0

    print("Doctor Ergebnis: FEHLER")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
