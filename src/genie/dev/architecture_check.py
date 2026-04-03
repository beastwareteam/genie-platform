from __future__ import annotations

import subprocess
import sys
from pathlib import Path
import os


def main() -> int:
    repo_root = Path(__file__).resolve().parents[3]
    command = [
        sys.executable,
        "-m",
        "pytest",
        "-q",
        "tests/contract",
        "tests/unit/test_registries.py",
    ]
    env = os.environ.copy()
    env["PYTEST_DISABLE_PLUGIN_AUTOLOAD"] = "1"
    result = subprocess.run(command, cwd=repo_root, env=env)
    return result.returncode


if __name__ == "__main__":
    raise SystemExit(main())
