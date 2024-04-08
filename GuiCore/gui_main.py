import sys
import traceback as tb
from tkinter import messagebox

from PyQt6.QtWidgets import QApplication

from .window import MainWindow

def exception_hook(exctype, value, traceback):
    s = "\n".join(tb.format_exception(exctype, value, traceback))
    messagebox.showerror("Exception detected!", s)
    sys.exit(1)


def GuiMain(names: [str, str]):
    sys.excepthook = exception_hook

    app = QApplication(sys.argv)
    widget = MainWindow(names)
    sys.exit(app.exec())
