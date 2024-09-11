from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QFrame, QGraphicsDropShadowEffect, QHBoxLayout, QGridLayout, QHeaderView, QSpacerItem, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget

import modules.biometrics.controller as biometrics_controller
import modules.students.controller as students_controller

from components.biometrics import Biometrics
from components.button import Button
from components.combo_box import ComboBox
from components.message_box import MessageBox

from modules.biometrics.model import Biometric, StudentBiometrics
from modules.students.model import Student

from assets.styles.styles import content_frame_style

class BiometricsPage(QWidget):
  def __init__(self, pages_handler):
    super().__init__()
    self.setStyleSheet(content_frame_style)
    self.pages_handler = pages_handler
    self.message_box: MessageBox = MessageBox(self)
    self.biometrics: list[StudentBiometrics] = []
    self.students: list[Student] = []
    self.__init_ui()

  def __init_ui(self):
    content_frame: QFrame = QFrame(self)
    content_frame.setObjectName("contentFrame")
    content_layout: QHBoxLayout = QHBoxLayout(content_frame)

    shadow_effect: QGraphicsDropShadowEffect = QGraphicsDropShadowEffect()
    shadow_effect.setBlurRadius(15)
    shadow_effect.setColor(QColor(0, 0, 0, 160))
    shadow_effect.setOffset(0, 5)

    content_frame.setGraphicsEffect(shadow_effect)
    
    self.main_layout: QHBoxLayout = QHBoxLayout()
    left_content_layout: QVBoxLayout = QVBoxLayout()

    self.student_combo_box: ComboBox = ComboBox(label_text="Student Names")
    self.biometrics_component: Biometrics = Biometrics()

    left_content_layout.addWidget(self.student_combo_box)
    left_content_layout.addWidget(self.biometrics_component)

    self.table_widget: QTableWidget = QTableWidget()
    self.table_widget.setColumnCount(3)
    self.table_widget.setHorizontalHeaderLabels(["ID", "Student Name", "Actions"])
    self.table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
    self.table_widget.verticalHeader().setVisible(False)
    self.table_widget.setFixedWidth(500)

    content_layout.addLayout(left_content_layout)
    content_layout.addWidget( self.table_widget)
    content_layout.setContentsMargins(50, 50, 50, 50)

    self.main_layout.addWidget(content_frame)
    self.setLayout(self.main_layout)

  def load_students_to_combo_box(self):
    self.students = students_controller.get_students("status = 'active'", "select")

    if not self.students:
      return
    
    items = [(student.full_name, student.id) for student in self.students]
    self.student_combo_box.set_items(items)

  def load_biometrics(self):
    self.biometrics = biometrics_controller.get_biometrics_with_students("all")
    if not self.biometrics:
      return
    
    for biometric in self.biometrics:
      row_position = self.table_widget.rowCount()
      self.table_widget.insertRow(row_position)

    
    