from __future__ import absolute_import

import PySimpleGUI as sg

from internal._common_func import _get_all_lib

sg.theme("DarkBlue3")

# autopep8: off
LAYOUT: list = [
    [sg.Text("インストール済みの pip ライブラリ:")],
    [[sg.Input(lib, disabled=True, text_color="Black", background_color="White")] for lib in _get_all_lib()],
    [sg.Input(pad=((5, 0), (30, 40))), sg.Text("を", pad=((5, 0), (30, 40))), sg.Combo(["インストール", "アンインストール"], "インストール", size=(16, None), pad=((5, 0), (30, 40)), readonly=True), sg.Button("実行", button_color="Gray", pad=((5, 0), (30, 40)), key="-START-")],
    [sg.Button("再起動する...", button_color="Red", key="-RESTART-")]
]
# autopep8: on
