from PyQt6.QtCore import QRect, Qt
from PyQt6.QtWidgets import QWidget, QLabel, QFrame, QLineEdit, QPushButton

from .draggable_line_edit import DraggableLineEdit


class UnitItem(QWidget):
    def __init__(self, parent, ident: str, nick: str):
        super().__init__(parent)
        self.ident = ident
        self.nick = nick

        self.m_frame_sp = QFrame(self)
        self.m_frame_sp.setFrameShape(QFrame.Shape.VLine)
        self.m_frame_sp.setGeometry(QRect(50, 5, 2, 65))

        self.m_label_name = QLabel(self.nick, self)
        self.m_label_name.setGeometry(5, 0, 40, 75)
        self.m_label_name.setAlignment(Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignRight)

        self.m_label_zf = QLabel("压缩包", self)
        self.m_label_zf.setGeometry(QRect(50, 5, 60, 30))
        self.m_label_zf.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.m_label_mc = QLabel("主类", self)
        self.m_label_mc.setGeometry(QRect(50, 40, 60, 30))
        self.m_label_mc.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.m_line_zf = DraggableLineEdit(self)
        self.m_line_zf.setGeometry(QRect(110, 5, 370, 30))
        self.m_line_zf.setPlaceholderText("拖拽或者填写路径！")

        self.m_line_mc = QLineEdit(self)
        self.m_line_mc.setGeometry(QRect(110, 40, 160, 30))
        self.m_line_mc.setPlaceholderText("如无法识别请手动填写")

        self.m_label_gen = QLabel("生成", self)
        self.m_label_gen.setGeometry(QRect(270, 40, 50, 30))
        self.m_label_gen.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.m_line_gen = QLineEdit(self)
        self.m_line_gen.setGeometry(QRect(320, 40, 160, 30))
        self.m_line_gen.setReadOnly(True)

        self.m_label_iv = QLabel(self)
        self.m_label_iv.setGeometry(QRect(480, 5, 120, 30))
        self.m_label_iv.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.m_btn_gen = QPushButton("生成", self)
        self.m_btn_gen.setGeometry(QRect(500, 40, 80, 30))

        self.connect()

    def connect(self):
        self.m_line_zf.textChanged.connect(self.on_zf_change)
        self.m_line_mc.textChanged.connect(self.on_mc_change)
        self.m_btn_gen.clicked.connect(self.on_gen)

    def on_zf_change(self):
        pass

    def on_mc_change(self):
        pass

    def on_gen(self):
        pass
