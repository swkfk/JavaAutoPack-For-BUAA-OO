from PyQt6.QtCore import QSize, QRect
from PyQt6.QtWidgets import QMainWindow

from .draggable_line_edit import DraggableLineEdit
from .unit_item import UnitItem


class MainWindow(QMainWindow):
    def __init__(self, names: [str, str]):
        super().__init__()
        self.names = names
        self.deps_file = ""

        self.setWindowTitle("Java 自动打包机 For BUAA_OO by kai_Ker")
        self.setFixedSize(QSize(600, 120 + 75 * len(self.names)))

        self.m_line_deps = DraggableLineEdit(self)

        self.units = []
        for i, (ident, nick) in enumerate(self.names):
            unit = UnitItem(self, ident, nick, self.m_line_deps)
            unit.setGeometry(QRect(0, 120 + 75 * i, 600, 75))
            self.units.append(unit)

        self.show()
