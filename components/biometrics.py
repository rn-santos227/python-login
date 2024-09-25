import re

import modules.biometrics.controller as biometrics_controller

from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QLabel, QVBoxLayout, QWidget

from components.combo_box import ComboBox
from components.message_box import MessageBox

from handlers.biometrics_handler import BiometricsHandler

from threads.capture_thread import CaptureThread

class Biometrics(QWidget):
  def __init__(self, parent=None):
    super().__init__(parent)
    self.biometrics_handler: BiometricsHandler = BiometricsHandler()
    self.capture_thread: CaptureThread = None 
    self.message_box: MessageBox = MessageBox(self)
    self.devices = []
    self.init_ui()

  def init_ui(self):
    self.layout: QVBoxLayout = QVBoxLayout(self)
    
    self.biometrics_combo_box: ComboBox = ComboBox(label_text="Biometrics List")

    self.label = QLabel(self)
    self.label.setAlignment(Qt.AlignCenter)

    self.layout.addWidget(self.biometrics_combo_box)
    self.layout.addWidget(self.label)

    self.cap = None
    self.timer = QTimer(self)
    self.timer.timeout.connect(self.update_frame)

  def load_biometric_devices_to_combo_box(self):
    self.devices = self.biometrics_handler.get_devices()
    if not self.devices:
      return
    
    pattern = r"\{(.*?)\}"
    items = []

    for device in self.devices:
      match = re.search(pattern, device)
      if match:
        items.append((match.group(1), device))

    self.biometrics_combo_box.set_items(items)

  def start_scanner(self):
    device = self.biometrics_combo_box.get_selected_value()

    if device:

      if self.capture_thread and self.capture_thread.isRunning():
        self.stop_scanner()

      self.capture_thread = CaptureThread(self.biometrics_handler, device)
      self.capture_thread.result_ready.connect(self.update_frame)
      self.capture_thread.start()

  def stop_scanner(self):
    if self.capture_thread:
      print("Stopping scanner...")
      self.capture_thread.stop()
      self.capture_thread = None
    
  def update_frame(self, capture_result):
    img_data, width, height = capture_result

    if img_data:
      self.display_image(img_data, width, height)
    
    else:
      self.message_box.show_message("Error", "Failed to capture fingerprint", "error")
  
  def display_image(self, img_data, width, height):
    img = QImage(img_data, width, height, QImage.Format_Grayscale8)
    pixmap = QPixmap.fromImage(img)
    
    self.label.setPixmap(pixmap.scaled(width, height, aspectRatioMode=Qt.KeepAspectRatio))

   