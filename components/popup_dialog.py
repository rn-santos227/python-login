from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QFrame, QHBoxLayout, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget

from modules.students.model import Student
from modules.logs.model import Log

from assets.styles.styles import image_label_style
class PopupDialog(QWidget):
  def __init__(self, parent=None):
    super().__init__(parent)

  def init_ui(self, log: Log, student: Student):
    self.setWindowTitle("Information")
    self.layout = QVBoxLayout()
    self.setLayout(self.layout)

    self.image_label = QLabel(self)
    pixmap: QPixmap = QPixmap(student.face_url)
    self.image_label.setPixmap(pixmap)
    self.image_label.setFixedSize(100, 100)
    self.image_label.setStyleSheet(image_label_style)

    self.form_layout: QVBoxLayout = QVBoxLayout()

    self.name_label: QLabel= QLabel("Student Name:")
    self.name_input: QLineEdit = QLineEdit()
    self.name_input.setReadOnly(True) 
    self.name_input.setText(student.full_name)
    self.form_layout.addWidget(self.name_label)
    self.form_layout.addWidget(self.name_input)

    self.name_label: QLabel= QLabel("Student Course:")
    