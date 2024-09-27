from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QFrame, QGraphicsDropShadowEffect, QHBoxLayout, QGridLayout, QHeaderView, QPushButton, QSpacerItem, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget

import modules.biometrics.controller as biometrics_controller
import modules.students.controller as students_controller

from components.biometrics import Biometrics
from components.button import Button
from components.combo_box import ComboBox
from components.message_box import MessageBox

from handlers.biometrics_handler import BiometricsHandler
from handlers.validations_handler import ValidationHandler

from modules.biometrics.model import Biometric, StudentBiometrics
from modules.students.model import Student

from assets.styles.styles import content_frame_style

class BiometricsPage(QWidget):
  def __init__(self, pages_handler):
    super().__init__()
    self.setStyleSheet(content_frame_style)
    self.pages_handler = pages_handler
    self.biometrics_handler: BiometricsHandler = BiometricsHandler()
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

    self.students_combo_box: ComboBox = ComboBox(label_text="Student List")
    self.biometrics_component: Biometrics = Biometrics()

    self.biometrics_button: Button = Button("Start Fingerprint Reader")
    self.biometrics_button.connect_signal(self.__enable_biometrics_scanner)

    self.save_biometric_button: Button = Button("Save Student Biometric")
    self.save_biometric_button.connect_signal(self.save_biometrics)

    left_content_layout.addWidget(self.students_combo_box)
    left_content_layout.addWidget(self.biometrics_component)
    left_content_layout.addWidget(self.biometrics_button)
    left_content_layout.addWidget(self.save_biometric_button)

    self.table_widget: QTableWidget = QTableWidget()
    self.table_widget.setColumnCount(3)
    self.table_widget.setHorizontalHeaderLabels(["ID", "Student Name", "Actions"])
    self.table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
    self.table_widget.verticalHeader().setVisible(False)
    self.table_widget.setFixedWidth(500)

    content_layout.addLayout(left_content_layout)
    content_layout.addWidget(self.table_widget)
    content_layout.setContentsMargins(50, 50, 50, 50)

    self.main_layout.addWidget(content_frame)
    self.setLayout(self.main_layout)

    self.save_biometric_button.set_disabled()
    self.load_biometrics()

  def load_students_to_combo_box(self):
    self.students = students_controller.get_students("status = 'active'", "select")

    if not self.students:
      return
    
    items = [(student.full_name, student.id) for student in self.students]
    self.students_combo_box.set_items(items)

  def save_biometrics(self):
    student_id = self.students_combo_box.get_selected_value()
    fingerprint_data = self.biometrics_component.fingerprint_data

    if not student_id:
      self.message_box.show_message("Warning", "Please select a student.", "warning")
      return
    
    if not fingerprint_data:
      self.message_box.show_message("Warning", "No Fingerprint Data.", "warning")
      return 

  def load_biometrics(self):
    self.biometrics = biometrics_controller.get_biometrics_with_students("all")
    self.biometrics_component.load_biometric_devices_to_combo_box()

    if not self.biometrics:
      return
    
    for biometric in self.biometrics:
      row_position = self.table_widget.rowCount()
      self.table_widget.insertRow(row_position)

      self.table_widget.setItem(row_position, 0, QTableWidgetItem(str(biometric.biometrics_id)))
      self.table_widget.setItem(row_position, 1, QTableWidgetItem(str(biometric.full_name)))

      delete_button: QPushButton = QPushButton("Delete")

      button_layout: QHBoxLayout = QHBoxLayout()
      button_layout.addWidget(delete_button)
      button_layout.setContentsMargins(0, 0, 0, 0)

      button_widget: QWidget = QWidget()
      button_widget.setLayout(button_layout)

      self.table_widget.setCellWidget(row_position, 4, button_widget)

  def __enable_biometrics_scanner(self):
    self.biometrics_component.start_scanner()
    self.biometrics_button.set_button_text("Stop Fingerprint Reader")
    self.biometrics_button.disconnect_signal(self.__enable_biometrics_scanner)
    self.biometrics_button.connect_signal(self.__disable_biometrics_scanner)
    self.save_biometric_button.set_enabled()

  def __disable_biometrics_scanner(self):
    self.biometrics_component.stop_scanner()
    self.biometrics_button.set_button_text("Start Fingerprint Reader")
    self.biometrics_button.disconnect_signal(self.__disable_biometrics_scanner)
    self.biometrics_button.connect_signal(self.__enable_biometrics_scanner)
    self.save_biometric_button.set_disabled()

    
    