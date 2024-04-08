import os

from PyQt6.QtCore import QSize, QRect, Qt
from PyQt6.QtWidgets import QMainWindow, QLabel

from .draggable_line_edit import DraggableLineEdit
from .unit_item import UnitItem

from AutoPackCore import set_jar, set_javac

class MainWindow(QMainWindow):
    def __init__(self, names: [str, str]):
        super().__init__()
        self.names = names
        self.deps_file = ""

        self.setWindowTitle("Java 自动打包机 For BUAA_OO by kai_Ker")
        self.setFixedSize(QSize(600, 110 + 75 * len(self.names)))

        self.m_label_javac = QLabel("Javac", self)
        self.m_label_javac.setGeometry(QRect(50, 75, 60, 30))
        self.m_label_javac.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.m_line_javac = DraggableLineEdit(self)
        self.m_line_javac.setGeometry(QRect(110, 75, 160, 30))
        self.m_line_javac.setPlaceholderText("可为 'javac'，可拖拽")

        self.m_label_jar = QLabel("Jar", self)
        self.m_label_jar.setGeometry(QRect(270, 75, 50, 30))
        self.m_label_jar.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.m_line_jar = DraggableLineEdit(self)
        self.m_line_jar.setGeometry(QRect(320, 75, 160, 30))
        self.m_line_jar.setPlaceholderText("可为 'jar'，可拖拽")

        self.m_label_deps = QLabel("依赖包", self)
        self.m_label_deps.setGeometry(QRect(5, 40, 60, 30))
        self.m_label_deps.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.m_line_deps = DraggableLineEdit(self)
        self.m_line_deps.setGeometry(QRect(65, 40, 415, 30))
        self.m_line_deps.setPlaceholderText("拖拽或者填写路径，可留空")

        self.m_label_cwd = QLabel("生成目录", self)
        self.m_label_cwd.setGeometry(QRect(5, 5, 60, 30))
        self.m_label_cwd.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.m_line_cwd = DraggableLineEdit(self)
        self.m_line_cwd.setText(os.getcwd())
        self.m_line_cwd.setGeometry(QRect(65, 5, 415, 30))
        self.m_line_cwd.setPlaceholderText("拖拽或者填写路径！")
        self.m_line_cwd.setReadOnly(True)

        self.m_label_gen = QLabel(os.path.sep + "Generated" + os.path.sep, self)
        self.m_label_gen.setGeometry(QRect(485, 5, 95, 30))
        self.m_label_gen.setAlignment(Qt.AlignmentFlag.AlignVCenter)

        self.units = []
        for i, (ident, nick) in enumerate(self.names):
            unit = UnitItem(self, ident, nick, self.m_line_deps)
            unit.setGeometry(QRect(0, 110 + 75 * i, 600, 75))
            self.units.append(unit)

        self.connect()

        self.show()

    def connect(self):
        self.m_line_javac.textChanged.connect(set_javac)
        self.m_line_jar.textChanged.connect(set_jar)
