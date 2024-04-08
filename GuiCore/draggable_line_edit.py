import os

from PyQt6.QtGui import QDragEnterEvent, QDragMoveEvent, QDropEvent
from PyQt6.QtWidgets import QLineEdit


class DraggableLineEdit(QLineEdit):
    def __init__(self, parent=...):
        super(DraggableLineEdit, self).__init__(parent)

    def dragEnterEvent(self, a0: QDragEnterEvent) -> None:
        if a0.mimeData().hasUrls():
            a0.acceptProposedAction()
        else:
            a0.ignore()

    def dragMoveEvent(self, e: QDragMoveEvent) -> None:
        pass

    def dropEvent(self, a0: QDropEvent) -> None:
        mime_data = a0.mimeData()
        if mime_data.hasUrls():
            urls = mime_data.urls()
            file_name = urls[0].toLocalFile()
            self.setText(file_name.replace('/', os.path.sep).replace('\\', os.path.sep))
            a0.accept()
        else:
            a0.ignore()
