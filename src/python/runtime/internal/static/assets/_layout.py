from __future__ import absolute_import

import PySimpleGUI as sg

from internal.static._common_func import _get_all_lib

sg.theme("DarkBlue3")

# autopep8: off
LAYOUT: list = [
    [sg.Text("インストール済みの pip ライブラリ:")],
    [[sg.Input(lib, disabled=True, text_color="Black", background_color="White")] for lib in _get_all_lib()],
    [sg.Button("再起動する...", key="-RESTART-")]
]
# autopep8: on
