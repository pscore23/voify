from __future__ import absolute_import

import PySimpleGUI as sg
from PySimpleGUI import Button, Column, Combo, Input, Text

from internal._common_func import get_all_lib, require_update


def calc_layout() -> list[list[Text] | list[Column] | list[Input | Text | Combo | Button] | list[Button]]:
    return _LAYOUT


_PAD: tuple[tuple[int, int], tuple[int, int]] = ((5, 0), (30, 40))
_LIB: tuple[list[str], list[str]] = get_all_lib()


_LAYOUT = [
    [sg.Text("インストール済みの pip ライブラリ:")],

    [sg.Text("名前 | バージョン".rjust(83, " "))],

    [sg.Column([[sg.Input(
        name, disabled=True, text_color="Orange", background_color="White"
    ), sg.Input(
        f"{ver} (バージョン {require_update(name)[1]} にアップデート可能)", disabled=True, text_color="Orange", background_color="White"
    )] if require_update(name)[0] else [sg.Input(
        name, disabled=True, text_color="Green", background_color="White"
    ), sg.Input(
        ver, disabled=True, text_color="Green", background_color="White"
    )] for name, ver in zip(_LIB[0], _LIB[1])], scrollable=True)],

    [sg.Input(
        key="-INPUT-", pad=_PAD
    ), sg.Text(
        "を", pad=_PAD
    ), sg.Combo(
        ["アップデート", "インストール", "アンインストール"], "アップデート", size=(16, None), text_color="Blue", button_arrow_color="Blue", key="-SELECT-", pad=_PAD, readonly=True
    ), sg.Button(
        "実行", button_color="Gray", pad=_PAD, key="-START-"
    )],

    [sg.Text("入力待ちです...", background_color="Black", key="-OUTPUT-")],

    [sg.Button("再起動する...", button_color="Red", key="-RESTART-", pad=_PAD)]
]
