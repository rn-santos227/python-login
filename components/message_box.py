from PyQt5.QtWidgets import QMessageBox

class MessageBox:
  def __init__(self, parent=None):
    self.parent = parent

  def show_message(self, title, message, message_type="information"):
    msg_box = QMessageBox(self.parent)
    msg_box.setWindowTitle(title)
    msg_box.setText(message)

    if message_type == "information":
      msg_box.setIcon(QMessageBox.Information)
    elif message_type == "warning":
      msg_box.setIcon(QMessageBox.Warning)
    elif message_type == "error":
      msg_box.setIcon(QMessageBox.Critical)
    elif message_type == "question":
      msg_box.setIcon(QMessageBox.Question)

    msg_box.setStandardButtons(QMessageBox.Ok)
    msg_box.exec_()