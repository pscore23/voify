from __future__ import absolute_import

import subprocess


def _get_all_lib():
    return [name.split("==")[0] for name in list(filter(None, subprocess.run("pip freeze", capture_output=True, text=True, check=True).stdout.split("\n")))]
