from __future__ import absolute_import

import subprocess
from typing import Any


def _run_pyf_command(__text: str) -> list[str]:
    return [name.split("==")[0] for name in list(filter(None, subprocess.run(__text, capture_output=True, text=True, check=True).stdout.split("\n")))]


def get_all_lib() -> list[str]:
    return _run_pyf_command("pip freeze --all")


def require_update(lib: Any) -> bool:
    return bool(lib in _UPDATE)


_UPDATE = _run_pyf_command("pip list --outdated --format freeze")
