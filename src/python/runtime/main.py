from __future__ import absolute_import

import gc
import subprocess
import sys

import PySimpleGUI as sg
from PySimpleGUI import Window


class MainProcess:
    """メインプロセスのクラス:
            - GUI 処理
            - pip の管理
    """

    def __init__(self) -> None:
        sg.theme("Dark Black")

        # autopep8: off
        self._layout: list = [
            [[sg.Text(lib)] for lib in [name.split("==")[0] for name in subprocess.run("pip freeze", capture_output=True, text=True, check=True).stdout.split("\n")]]
        ]
        # autopep8: on
        self._window: Window = sg.Window("voify", self._layout)

    def run(self) -> None:
        """全ての処理を開始 (または終了) する:
                - ウィンドウの表示
                    - 入力されたデータの処理
        """
        while True:
            event, values = self._window.read()  # type: ignore

            if event in (sg.WIN_CLOSED,):
                break

        self._window.close()
        sys.exit(gc.collect())


if __name__ == "__main__":
    MP = MainProcess()

    MP.run()
