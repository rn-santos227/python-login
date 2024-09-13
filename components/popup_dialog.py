from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QDialog, QHBoxLayout, QLabel, QLineEdit, QPushButton, QVBoxLayout

from modules.students.model import Student

from assets.styles.styles import image_label_style, popup_dialog_style
class PopupDialog(QDialog):
  def __init__(self, parent=None, student: Student = None, logged: str = ""):
    super().__init__(parent)
    self.logged = logged
    self.student = student
    self.init_ui()

    # self.timer: QTimer = QTimer(self)
    # self.timer.timeout.connect(self.close_popup)
    # self.timer.start(5000)

  def show(self):
    self.init_ui()
    super().exec_()  

  def init_ui(self):
    self.setWindowTitle("Information")
    self.layout: QVBoxLayout = QVBoxLayout()
    self.setLayout(self.layout)

    self.image_label: QLabel = QLabel(self)
    pixmap: QPixmap = QPixmap(self.student.face_url)
    self.image_label.setPixmap(pixmap)
    self.image_label.setFixedSize(250, 250)
    self.image_label.setStyleSheet(image_label_style)

    self.form_layout: QVBoxLayout = QVBoxLayout()

    self.name_label: QLabel= QLabel("Student Name:")
    self.name_input: QLineEdit = QLineEdit()
    self.name_input.setReadOnly(True) 
    self.name_input.setText(self.student.full_name)
    self.form_layout.addWidget(self.name_label)
    self.form_layout.addWidget(self.name_input)

    self.course_label: QLabel= QLabel("Student Course:")
    self.course_input: QLineEdit = QLineEdit()
    self.course_input.setReadOnly(True) 
    self.course_input.setText(self.student.course)
    self.form_layout.addWidget(self.course_label)
    self.form_layout.addWidget(self.course_input)

    self.time_layout: QHBoxLayout = QHBoxLayout()
    self.time_label: QLabel = QLabel("Time:")
    self.time_input: QLineEdit = QLineEdit()
    self.time_input.setReadOnly(True)
    self.time_input.setText(self.logged) 
    self.time_layout.addWidget(self.time_label)
    self.time_layout.addWidget(self.time_input)
    self.form_layout.addLayout(self.time_layout)

    self.close_button: QPushButton = QPushButton("Close")
    self.close_button.clicked.connect(self.close_popup)

    self.image_and_form_layout: QHBoxLayout = QHBoxLayout()
    self.image_and_form_layout.addWidget(self.image_label)
    self.image_and_form_layout.addLayout(self.form_layout)

    self.layout.addLayout(self.image_and_form_layout)
    self.layout.addWidget(self.close_button)

    self.setStyleSheet(popup_dialog_style)
    self.setGeometry(300, 300, 400, 200)

  def close_popup(self):
    self.close()
    
  def set_student(self, student: Student):
    pass