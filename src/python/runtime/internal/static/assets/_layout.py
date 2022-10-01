from __future__ import absolute_import

import subprocess

import PySimpleGUI as sg

sg.theme("DarkBlue3")

# autopep8: off
LAYOUT: list = [
    [sg.Text("インストール済みの pip ライブラリ:")],
    [[sg.Text(lib, text_color="Black", background_color="White")] for lib in [name.split("==")[0] for name in list(filter(None, subprocess.run("pip freeze", capture_output=True, text=True, check=True).stdout.split("\n")))]]
]
# autopep8: on
