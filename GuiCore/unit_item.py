import shutil
from pathlib import Path

from PyQt6.QtCore import QRect, Qt
from PyQt6.QtWidgets import QWidget, QLabel, QFrame, QLineEdit, QPushButton, QMessageBox

from .draggable_line_edit import DraggableLineEdit
from .settings import get_default_path
from AutoPackCore import (
    get_main_class, list_java, unzip, make_jar, copy_jar, extract_jar,
    MainClassDuplicatedException, MainClassNotFoundException, compile_java, CompileErrorException
)


class UnitItem(QWidget):
    def __init__(self, parent, ident: str, nick: str, deps_line: DraggableLineEdit):
        super().__init__(parent)
        self.parent = parent
        self.root_path = Path(get_default_path()) / ident
        self.ident = ident
        self.nick = nick
        self.p_line_deps = deps_line

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

        self.m_label_gen = QLabel("已生成", self)
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
        self.m_btn_gen.setEnabled(False)

        self.connect()

    def connect(self):
        self.m_line_zf.textChanged.connect(self.on_zf_change)
        self.m_line_mc.textChanged.connect(self.on_mc_change)
        self.m_btn_gen.clicked.connect(self.on_gen)

    def on_zf_change(self):
        self.m_line_zf.setText(self.m_line_zf.text().strip(' "\n\t\r'))
        zip_path = Path(self.m_line_zf.text())
        self.m_btn_gen.setEnabled(False)
        if not zip_path.is_file():
            self.m_label_iv.setText("无效文件！")
            self.m_line_mc.setText("")
            self.m_line_gen.setText("")
            return

        if self.root_path.exists():
            shutil.rmtree(str(self.root_path))
        self.root_path.mkdir(exist_ok=False)
        (self.root_path / 'src').mkdir(exist_ok=False)

        self.m_label_iv.setText("")
        try:
            unzip(str(zip_path), self.root_path / 'src')
            main_class = get_main_class(list_java(self.root_path / 'src'))
            self.m_line_mc.setText(main_class)
            self.on_gen()
        except (MainClassDuplicatedException, MainClassNotFoundException):
            self.m_line_mc.setText("")
        self.m_line_mc.disconnect()
        self.m_line_mc.textChanged.connect(self.on_mc_change)

    def on_mc_change(self):
        if self.m_line_mc.text().strip() != "":
            self.m_btn_gen.setEnabled(True)

    def on_gen(self):
        self.m_btn_gen.setEnabled(False)
        deps_file = self.p_line_deps.text().strip()

        try:
            (self.root_path / 'build').mkdir(exist_ok=False)
            compile_java(self.root_path, deps_file)
            if deps_file != "":
                extract_jar(deps_file, (self.root_path / 'build'))
            make_jar(self.root_path, self.ident, self.m_line_mc.text())
        except CompileErrorException as e:
            QMessageBox.critical(self, "编译错误", str(e))

        try:
            copy_jar(self.root_path, self.ident)
            self.m_line_gen.setText(str(self.root_path) + ".jar")
        except Exception as e:
            QMessageBox.critical(self, "复制错误", str(e))
