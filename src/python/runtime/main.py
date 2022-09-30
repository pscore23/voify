import sys

import PySimpleGUI as sg


class MainProcess:
    def __init__(self):
        sg.theme("Dark Black")

        self._layout = [[sg.Text("テスト")]]
        self._window = sg.Window("voify", self._layout)

    def run(self):
        while True:
            event, values = self._window.read()  # type: ignore

            if event in (sg.WIN_CLOSED,):
                break

        sys.exit(self._window.close())


if __name__ == "__main__":
    mp = MainProcess()

    mp.run()
