from PyQt5.QtWidgets import QDialog, QHBoxLayout, QLabel, QPushButton, QVBoxLayout, QLineEdit

class PromptDialog(QDialog):
  def __init__(self, title="Input Prompt", message="Please enter something:", is_password=False, parent=None, fixed_width=400):
    super().__init__(parent)
    self.setWindowTitle(title)
    self.parent = parent
    self.is_password = is_password 
    self.fixed_width = fixed_width
    self.__user_input = None
    self.__init_ui(message)

  def __init_ui(self, message):
    self.setFixedWidth(self.fixed_width) 
    self.layout: QVBoxLayout = QVBoxLayout()

    self.message_label: QLabel = QLabel(message)
    self.layout.addWidget(self.message_label)

    self.input_field: QLineEdit = QLineEdit(self)
    
    if self.is_password:
      self.input_field.setEchoMode(QLineEdit.Password)
    
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
      dialog_geometry.moveCenter(center_point)
      self.move(dialog_geometry.topLeft())
    super().showEvent(event)