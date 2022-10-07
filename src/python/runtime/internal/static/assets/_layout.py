from __future__ import absolute_import

import PySimpleGUI as sg
from PySimpleGUI import Button, Combo, Input, Text

from internal._common_func import get_all_lib, require_update

sg.theme("DarkBlue3")

_PAD: tuple[tuple[int, int], tuple[int, int]] = ((5, 0), (30, 40))

# autopep8: off
LAYOUT: list[list[Text] | list[list[Input]] | list[Input | Text | Combo | Button] | list[Button]] = [
    [sg.Text("インストール済みの pip ライブラリ:")],

    [[sg.Input(lib, disabled=True, text_color="Red", background_color="White")] if require_update(lib) else [sg.Input(lib, disabled=True, text_color="Black", background_color="White")] for lib in get_all_lib()],

    [sg.Input(key="-INPUT-", pad=_PAD), sg.Text("を", pad=_PAD), sg.Combo(["アップデート", "インストール", "アンインストール"], "アップデート", size=(16, None), text_color="Green", button_arrow_color="Blue", key="-SELECT-", pad=_PAD, readonly=True), sg.Button("実行", button_color="Gray", pad=_PAD, key="-START-")],

    [sg.Text("入力待ちです...", background_color="Black", key="-OUTPUT-")],

    [sg.Button("再起動する...", button_color="Red", key="-RESTART-", pad=_PAD)]
]
# autopep8: on
