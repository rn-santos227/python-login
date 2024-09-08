from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QFrame, QHBoxLayout, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget

from modules.students.model import Student
from modules.logs.model import Log

from assets.styles.styles import image_label_style
class PopupDialog(QWidget):
  def __init__(self, parent=None, log: Log = None, student: Student = None):
    super().__init__(parent)
    self.log = log
    self.student = student
    self.init_ui(log=log, student=student)

  def init_ui(self, log: Log, student: Student):
    self.setWindowTitle("Information")
    self.layout: QVBoxLayout = QVBoxLayout()
    self.setLayout(self.layout)

    self.image_label: QLabel = QLabel(self)
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

    self.course_label: QLabel= QLabel("Student Course:")
    self.course_input: QLineEdit = QLineEdit()
    self.course_input.setReadOnly(True) 
    self.course_input.setText(student.course)
    self.form_layout.addWidget(self.course_label)
    self.form_layout.addWidget(self.course_input)

    self.time_layout: QHBoxLayout = QHBoxLayout()
    self.time_label: QLabel = QLabel("Time:")
    self.time_input: QLineEdit = QLineEdit()
    self.time_layout.addWidget(self.time_label)
    self.time_layout.addWidget(self.time_input)
    self.form_layout.addLayout(self.time_layout)

    self.close_button: QPushButton = QPushButton("Close")

    self.image_and_form_layout: QHBoxLayout = QHBoxLayout()
    