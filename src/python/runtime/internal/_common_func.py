from __future__ import absolute_import

import subprocess
from typing import Any


def _run_command(__text: str) -> list[str]:
    return [line for line in list(filter(None, subprocess.run(__text, capture_output=True, text=True, check=True).stdout.split("\n")))]


def get_all_lib() -> tuple[list[str], list[str]]:
    _info = _run_command("pip freeze --all")

    lib_name = [name.split("==")[0] for name in _info]
    lib_ver = [ver.split("==")[1] for ver in _info]

    return (lib_name, lib_ver)


def require_update(lib: Any) -> bool:
    return bool(lib in _UPDATE)


_UPDATE = (lambda: [name.split("==")[0] for name in _run_command("pip list --outdated --format freeze")])()
