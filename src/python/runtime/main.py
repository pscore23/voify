from __future__ import absolute_import

import gc
import io
import os
import sys

import PySimpleGUI as sg
from PySimpleGUI import Window

from internal.static.assets._layout import LAYOUT


class MainProcess(object):
    """メインプロセスのクラス:
            - GUI 処理
            - pip の管理
    """

    def __init__(self) -> None:
        self._system: System = System()
        self._window: Window = sg.Window("voify", LAYOUT, finalize=True)

        self._system.setup()

    def run(self) -> None:
        """全ての処理を開始 (または終了) する:
                - ウィンドウの表示
                    - 入力されたデータの処理
        """
        while True:
            event, values = self._window.read()  # type: ignore

            if event in (sg.WIN_CLOSED,):
                break

            if event == "-UPDATE-":
                self._system.restart()

            self._window.refresh()

        self._window.close()
        self._system.cleanup()
        sys.exit()


class System(object):
    @staticmethod
    def setup():
        """エンコーディング関係のセットアップを行う"""
        sys.stdin = io.TextIOWrapper(sys.stdin.buffer, encoding="utf-8")
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
        sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8")

    @staticmethod
    def cleanup():
        """クリーンアップを行う"""
        sys.stdout.flush()
        gc.collect()

    def restart(self):
        """アプリケーションの再起動を行う"""
        self.cleanup()

        os.execv(sys.executable, ["python"] + sys.argv)


if __name__ == "__main__":
    MP = MainProcess()

    MP.run()
