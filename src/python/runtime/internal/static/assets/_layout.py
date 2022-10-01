import subprocess

import PySimpleGUI as sg

sg.theme("Dark Black")

# autopep8: off
LAYOUT: list = [
    [[sg.Text(lib)] for lib in [name.split("==")[0] for name in list(filter(None, subprocess.run("pip freeze", capture_output=True, text=True, check=True).stdout.split("\n")))]]
]
# autopep8: on
