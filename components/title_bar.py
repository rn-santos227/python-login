from PyQt5.QtWidgets import QWidget, QHBoxLayout, QPushButton, QLabel
from PyQt5.QtCore import Qt

class TitleBar(QWidget):
  def __init__(self, parent=None):
    super().__init__(parent)
    self.init_ui()

  def init_ui(self):
    self.setFixedHeight(30)

    layout = QHBoxLayout()
    layout.setContentsMargins(0, 0, 0, 0)
    layout.setSpacing(0)

    self.title = QLabel("Attendance Logbook Application")
    self.title.setAlignment(Qt.AlignCenter)

    self.close_button = QPushButton("X")
    self.close_button.setFixedSize(30, 30)
    self.close_button.clicked.connect(self.close_window)

    layout.addWidget(self.title)
    layout.addWidget(self.close_button)