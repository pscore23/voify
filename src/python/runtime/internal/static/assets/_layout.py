import PySimpleGUI as sg

from internal.static._common_func import _get_all_lib

sg.theme("DarkBlue3")

# autopep8: off
LAYOUT: list = [
    [sg.Text("インストール済みの pip ライブラリ:")],
    [[sg.Text(lib, text_color="Black", background_color="White")] for lib in _get_all_lib()],
    [sg.Button("情報を更新する...", key="-UPDATE-")]
]
# autopep8: on
