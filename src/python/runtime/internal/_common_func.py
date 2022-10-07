from __future__ import absolute_import

import subprocess

_UPDATE = [name.split("==")[0] for name in list(filter(None, subprocess.run(
    "pip list --outdated --format freeze", capture_output=True, text=True, check=True).stdout.split("\n")))]


def _get_all_lib() -> list[str]:
    return [name.split("==")[0] for name in list(filter(None, subprocess.run("pip freeze --all", capture_output=True, text=True, check=True).stdout.split("\n")))]


def _require_update(lib) -> bool:
    if lib in _UPDATE:
        return True

    else:
        return False
