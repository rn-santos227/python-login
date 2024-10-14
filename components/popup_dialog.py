from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtWidgets import QApplication, QDialog, QHBoxLayout, QGridLayout, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget

from modules.students.model import Student

from components.text_field import TextField

from assets.styles.styles import image_label_style, popup_dialog_style
class PopupDialog(QDialog):
  def __init__(self, parent=None, student: Student = None, logged: str = ""):
    super().__init__(parent)
    self.setWindowTitle("Information")
    self.init_ui()
    self.parent = parent
    self.timer: QTimer = QTimer(self)
    self.student: Student = student
    self.logged: str = logged
    # self.timer.timeout.connect(self.close_popup)
    self.timer.start(10000) 

  def init_ui(self):
    self.layout: QVBoxLayout = QVBoxLayout()
    self.setLayout(self.layout)

    self.image_label: QLabel = QLabel(self)

    if self.student and self.student.face_url:
      pixmap: QPixmap = QPixmap(self.student.face_url)
      scaled_pixmap = pixmap.scaled(self.image_label.size(), aspectMode=Qt.KeepAspectRatio)
      self.image_label.setPixmap(scaled_pixmap)

    else:
      self.image_label.setText("No Image Available") 
      self.image_label.setFixedSize(250, 250)
      self.image_label.setStyleSheet(image_label_style)

    self.form_layout: QGridLayout = QGridLayout()

    self.student_name_field: TextField = TextField(label_text="Student Name:", placeholder_text="Enter student name.")
    self.student_name_field.set_text(self.student.full_name)
    self.student_name_field.set_read_only(True)

    self.student_course_field: TextField = TextField(label_text="Student Course:", placeholder_text="Enter student course.")
    self.student_course_field.set_text(self.student.course)
    self.student_course_field.set_read_only(True)

    self.student_logged_field: TextField = TextField(label_text="Logged Time:", placeholder_text="Enter logged time.")
    self.student_logged_field.set_text(self.logged)
    self.student_logged_field.set_read_only(True)

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

  def close_popup(self):
    self.close()

  def showEvent(self, event):
    if self.parent:
      parent_geometry = self.parent.frameGeometry()
      dialog_geometry = self.frameGeometry()
      center_point = parent_geometry.center()
      dialog_geometry.moveCenter(center_point)
      self.move(dialog_geometry.topLeft())