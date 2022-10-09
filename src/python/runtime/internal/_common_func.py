from __future__ import absolute_import

import json
import subprocess
from typing import Any


def _run_command(__text: str) -> list[str]:
    return [line for line in list(filter(None, subprocess.run(
        __text, capture_output=True, text=True, check=True).stdout.split("\n")))]


def get_all_lib() -> tuple[list[str], list[str]]:
    _info = _run_command("pip freeze --all")

    lib_name = [name.split("==")[0] for name in _info]
    lib_ver = [ver.split("==")[1] for ver in _info]

    return (lib_name, lib_ver)


def require_update(lib_name: Any) -> tuple[bool, Any]:
    _lib_dict = {}

    for i in _UPDATE:
        _lib_dict |= i

    return (bool(lib_name in _lib_dict.keys()), _lib_dict.get(lib_name))


_UPDATE: list[dict[Any, Any]] = (lambda: [{name.get("name"): name.get("latest_version")} for name in json.loads(
    str(_run_command("pip list --outdated --format json")[0]))])()
