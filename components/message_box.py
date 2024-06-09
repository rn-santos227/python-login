from PyQt5.QtWidgets import QMessageBox

class MessageBox:
  def __init__(self, parent=None):
    self.parent = parent

  def show_message(self, title, message, message_type="information"):
    msg_box = QMessageBox(self.parent)