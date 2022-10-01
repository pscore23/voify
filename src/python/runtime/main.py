import gc
import subprocess
import sys
from tkinter import SEL_FIRST
from typing import NoReturn

import PySimpleGUI as sg


class MainProcess:
    def __init__(self):
        sg.theme("Dark Black")

        # autopep8: off
        self._layout = [
            [[sg.Text(lib)] for lib in [name.split("==")[0] for name in subprocess.run("pip freeze", capture_output=True, text=True).stdout.split("\n")]]
        ]
        # autopep8: on
        self._window = sg.Window("voify", self._layout)

    def run(self) -> None:
        while True:
            event, values = self._window.read()  # type: ignore

            if event in (sg.WIN_CLOSED,):
                break

        self._window.close()
        sys.exit(gc.collect())


if __name__ == "__main__":
    mp = MainProcess()

    mp.run()
