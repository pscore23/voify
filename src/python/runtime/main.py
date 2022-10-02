from __future__ import absolute_import

import gc
import io
import os
import sys

try:
    import psutil

except ModuleNotFoundError:
    raise ModuleNotFoundError("psutil ライブラリが見つかりません")

try:
    import PySimpleGUI as sg
    from PySimpleGUI import Window

except ModuleNotFoundError:
    raise ModuleNotFoundError("PySimpleGUI ライブラリが見つかりません")

from internal.static.assets._layout import LAYOUT


class MainProcess:
    """メインプロセスのクラス:
            - GUI 処理
            - pip の管理
    """

    def __init__(self) -> None:
        self._system: _System = _System()
        self._window: Window = sg.Window("voify", LAYOUT, size=(600, 500), resizable=True, finalize=True)

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

            if event == "-RESTART-":
                self._system.restart()

            self._window.refresh()

        self._window.close()
        self._system.cleanup()
        sys.exit()


class _System:
    """内部の処理で使われるクラス"""

    @staticmethod
    def setup():
        """エンコーディング関係の設定を行う"""
        sys.stdin = io.TextIOWrapper(sys.stdin.buffer, encoding="utf-8")
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
        sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8")

    @staticmethod
    def cleanup():
        """クリーンアップを行う"""
        process = psutil.Process(os.getpid())

        try:
            for f_handler in process.open_files():
                os.close(f_handler.fd)

            for c_handler in process.connections():
                os.close(c_handler.fd)

        except OSError:
            pass

        sys.stdout.flush()
        gc.collect()

    def restart(self):
        """プロセスの再起動を行う"""
        _args = sys.argv[:]
        _args.insert(0, sys.executable)

        self.cleanup()

        os.execv(sys.executable, _args)


if __name__ == "__main__":
    MP = MainProcess()

    MP.run()
