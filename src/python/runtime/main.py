from __future__ import absolute_import

import gc
import sys

import PySimpleGUI as sg
from PySimpleGUI import Window

from internal.static.assets._layout import LAYOUT


class MainProcess:
    """メインプロセスのクラス:
            - GUI 処理
            - pip の管理
    """

    def __init__(self) -> None:
        self._window: Window = sg.Window("voify", LAYOUT)

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
