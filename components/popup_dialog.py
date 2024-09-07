from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QFrame, QLabel, QHBoxLayout, QPushButton, QVBoxLayout, QWidget

from modules.students.model import Student
from modules.logs.model import Log

from assets.styles.styles import image_label_style
class PopupDialog(QWidget):
  def __init__(self, parent=None):
    super().__init__(parent)

  def init_ui(self, student: Student, logged: str):
    self.setWindowTitle("Information")
    self.layout = QVBoxLayout()
    self.setLayout(self.layout)

    self.image_label = QLabel(self)
    pixmap: QPixmap = QPixmap(student.face_url)
    self.image_label.setPixmap(pixmap)
    self.image_label.setFixedSize(100, 100)
    self.image_label.setStyleSheet(image_label_style)

    self.form_layout: QVBoxLayout = QVBoxLayout()

    self.name_label: QLabel= QLabel("Name:")