from PyQt5.QtWidgets import QDialog, QHBoxLayout, QLabel, QPushButton, QVBoxLayout, QLineEdit

class PromptDialog(QDialog):
  def __init__(self, title="Input Prompt", message="Please enter something:", parent=None):
    super().__init__(parent)
    self.setWindowTitle(title)
    self.parent = parent
    self.user_input = None

  def init_ui(self, message):
    self.layout: QVBoxLayout = QVBoxLayout()

    self.message_label = QLabel(message)
    self.layout.addWidget(self.message_label)

    self.input_field = QLineEdit(self)
    self.layout.addWidget(self.input_field)

    self.button_layout = QHBoxLayout()

  def on_okay_clicked(self):
    self.user_input = self.input_field.text()