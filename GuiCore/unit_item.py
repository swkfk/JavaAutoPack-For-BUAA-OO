from PyQt6.QtWidgets import QWidget, QLabel


class UnitItem(QWidget):
    def __init__(self, parent, ident: str, nick: str):
        super().__init__(parent)
        self.ident = ident
        self.nick = nick

        self.m_label_name = QLabel(self.nick, self)
