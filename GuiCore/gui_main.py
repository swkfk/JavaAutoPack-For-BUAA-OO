import shutil
import sys
import traceback as tb
from pathlib import Path
from tkinter import messagebox

from PyQt6.QtWidgets import QApplication

from .window import MainWindow

def exception_hook(exctype, value, traceback):
    s = "\n".join(tb.format_exception(exctype, value, traceback))
    messagebox.showerror("Exception detected!", s)
    sys.exit(1)


def GuiMain(names: [str, str]):
    sys.excepthook = exception_hook

    root_path = Path('Generated')
    root_path.mkdir(exist_ok=True)

    for ident, _ in names:
        person_root_path = root_path / ident
        if person_root_path.exists():
            shutil.rmtree(str(person_root_path))
        person_root_path.mkdir(exist_ok=False)
        (person_root_path / 'src').mkdir(exist_ok=False)

    app = QApplication(sys.argv)
    widget = MainWindow(names)
    sys.exit(app.exec())
