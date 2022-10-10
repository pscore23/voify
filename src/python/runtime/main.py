from __future__ import absolute_import

import gc
import io
import os
import subprocess
import sys
from typing import Any

try:
    import psutil

except ModuleNotFoundError as e:
    raise ModuleNotFoundError("psutil ライブラリが見つかりません") from e

try:
    import PySimpleGUI as sg
    from PySimpleGUI import Window

except ModuleNotFoundError as e:
    raise ModuleNotFoundError("PySimpleGUI ライブラリが見つかりません") from e

from internal._common_func import get_all_lib
from internal.static.assets._layout import calc_layout


class MainProcess:
    """メインプロセスのクラス:
            - GUI 処理
            - pip の管理
    """

    def __init__(self) -> None:
        self.lib: _Lib = _Lib()
        self.system: _System = _System()
        self.window: Window = sg.Window("voify", calc_layout(), auto_size_text=True,
                                        auto_size_buttons=True, size=(800, 700), resizable=True, finalize=True)

        sg.theme("DarkBlue3")

        self.system.setup()

    def run(self) -> None:
        """全ての処理を開始 (または終了) する:
                - ウィンドウの表示
                    - 入力されたデータの処理
        """
        while True:
            event, values = self.window.read()  # type: ignore

            match event:
                case sg.WIN_CLOSED:
                    break

                case "-START-":
                    _text = ("指定ライブラリを", "しています... (", "後にこのプロセスは再起動されます)")
                    _lib = values["-INPUT-"]
                    _select = values["-SELECT-"]

                    if (_lib not in get_all_lib()[0]) and (not _select == "インストール"):
                        self.window["-OUTPUT-"].update(value="エラー: 指定されたライブラリが見つかりません")

                    else:
                        match _select:
                            case "アップデート":
                                self.window["-OUTPUT-"].update(
                                    value=f"{_text[0]} {_select} {_text[1]} {_select} {_text[2]}")

                                self.window.refresh()

                                self.lib.update(_lib)

                            case "インストール":
                                self.window["-OUTPUT-"].update(
                                    value=f"{_text[0]} {_select} {_text[1]} {_select} {_text[2]}")

                                self.window.refresh()

                                self.lib.install(_lib)

                            case "アンインストール":
                                if _lib in ("psutil", "PySimpleGUI"):
                                    self.window["-OUTPUT-"].update(value="エラー: 指定されたライブラリはこのプロセスの依存ライブラリです")

                                    self.window.refresh()

                                else:
                                    self.window["-OUTPUT-"].update(
                                        value=f"{_text[0]} {_select} {_text[1]} {_select} {_text[2]}")

                                    self.window.refresh()

                                    self.lib.uninstall(_lib)

                        self.system.restart()

                case "-RESTART-":
                    self.system.restart()

        self.window.close()
        self.system.cleanup()

        sys.exit()


class _Lib:
    """ライブラリの管理を行うクラス"""

    def __init__(self):
        """コマンドの初期化など"""
        self.command: tuple = ("pip install", "pip uninstall")
        self.option: tuple = ("-y", "--upgrade", "--user")

    def update(self, lib: Any, all: bool = False):
        """ライブラリのアップデート"""
        if not all:
            subprocess.run(f"{self.command[0]} {self.option[1]} {lib} {self.option[2]}", check=True)

    def install(self, lib: Any):
        """ライブラリのインストール"""
        subprocess.run(f"{self.command[0]} {lib} {self.option[2]}", check=True)

    def uninstall(self, lib: Any, all: bool = False):
        """ライブラリのアンインストール"""
        if not all:
            subprocess.run(f"{self.command[1]} {lib} {self.option[0]}")


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
