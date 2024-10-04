from PyQt5.QtWidgets import QDialog, QHBoxLayout, QLabel, QPushButton, QVBoxLayout, QLineEdit

class PromptDialog(QDialog):
  def __init__(self, title="Input Prompt", message="Please enter something:", parent=None):
    super().__init__(parent)
    self.setWindowTitle(title)
    self.parent = parent
    self.__user_input = None

  def init_ui(self, message):
    self.layout: QVBoxLayout = QVBoxLayout()

    self.message_label: QLabel = QLabel(message)
    self.layout.addWidget(self.message_label)

    self.input_field: QLineEdit = QLineEdit(self)
    self.layout.addWidget(self.input_field)

    self.button_layout: QHBoxLayout = QHBoxLayout()

    self.okay_button: QPushButton = QPushButton("Okay")
    self.okay_button.clicked.connect(self.on_okay_clicked)
    self.button_layout.addWidget(self.okay_button)

    self.cancel_button: QPushButton = QPushButton("Cancel")
    self.cancel_button.clicked.connect(self.reject)
    self.button_layout.addWidget(self.cancel_button)

    self.layout.addLayout(self.button_layout)
    self.setLayout(self.layout)

  def on_okay_clicked(self):
    self.__user_input = self.input_field.text()
    self.accept()

  def get_user_input(self):
    return self.__user_input
  
  def showEvent(self, event):
    if self.parent:
      parent_geometry = self.parent.frameGeometry()
      dialog_geometry = self.frameGeometry()
      center_point = parent_geometry.center()