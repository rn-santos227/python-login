from PyQt5.QtCore import QThread, pyqtSignal

class CaptureThread(QThread):
  result_ready = pyqtSignal(tuple) 

  def __init__(self, biometrics_handler, device_name):
    super().__init__()

