from PyQt5.QtCore import  QTimer
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtWidgets import QDialog, QHBoxLayout, QGridLayout, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget

from modules.students.model import Student

from components.text_field import TextField

from assets.styles.styles import image_label_style, popup_dialog_style
class PopupDialog(QDialog):
  def __init__(self, parent=None):
    super().__init__(parent)
    self.setWindowTitle("Information")
    self.timer: QTimer = QTimer(self)
    self.timer.timeout.connect(self.close_popup)
    self.student: Student = None
    self.logged: str = ""
    self.init_ui()

  def show(self):
    self.update_ui()
    self.reset_timer()
    self.center_to_parent()
    super().exec_()  

  def init_ui(self):
    self.layout: QVBoxLayout = QVBoxLayout()
    self.setLayout(self.layout)

    self.image_label: QLabel = QLabel(self)

    if self.student and self.student.face_url:
      pixmap: QPixmap = QPixmap(self.student.face_url)
      self.image_label.setPixmap(pixmap)

    self.image_label.setText("No Image Available") 
    self.image_label.setFixedSize(250, 250)
    self.image_label.setStyleSheet(image_label_style)

    self.form_layout: QGridLayout = QGridLayout()

    self.student_name_field: TextField = TextField(label_text="Student Name:", placeholder_text="Enter student name.")
    self.student_name_field.set_text("No Student")

    self.student_course_field: TextField = TextField(label_text="Student Course:", placeholder_text="Enter student course.")
    self.student_course_field.set_text("No Student")

    self.student_logged_field: TextField = TextField(label_text="Logged Time:", placeholder_text="Enter logged time.")
    self.student_logged_field.set_text("No Student")

    self.close_button: QPushButton = QPushButton("Close")
    self.close_button.clicked.connect(self.close_popup)

    self.form_layout.addWidget(self.student_name_field, 0, 0, 1, 2)
    self.form_layout.addWidget(self.student_course_field, 1, 0, 1, 2)
    self.form_layout.addWidget(self.student_logged_field, 2, 0, 1, 2)

    self.image_and_form_layout: QHBoxLayout = QHBoxLayout()
    self.image_and_form_layout.addWidget(self.image_label)
    self.image_and_form_layout.addLayout(self.form_layout)

    self.layout.addLayout(self.image_and_form_layout)
    self.layout.addWidget(self.close_button)

    self.setStyleSheet(popup_dialog_style)
    self.setGeometry(600, 600, 800, 400)

  def update_ui(self):
    if self.student and self.student.face_url:
      pixmap: QPixmap = QPixmap(self.student.face_url)
      self.image_label.setPixmap(pixmap)
    
    else:
      self.image_label.setText("No Image Available")

    if self.student:
      self.student_name_field.set_text(self.student.full_name)
      self.student_course_field.set_text(self.student.course)
      self.student_logged_field.set_text(self.logged)

  def close_popup(self):
    self.close()
    
  def set_student(self, student: Student):
    self.student = student

  def set_logged_time(self, logged: str):
    self.logged = logged

  def reset_timer(self):
    if self.timer.isActive():
      self.timer.stop()
    self.timer.start(10000) 

  def center_to_parent(self):
    parent_geometry = self.parent().geometry()
    dialog_geometry = self.geometry()
  
    x: int = parent_geometry.x() + (parent_geometry.width() - dialog_geometry.width()) // 2
    y: int = parent_geometry.y() + (parent_geometry.height() - dialog_geometry.height()) // 2

    self.move(x, y)
