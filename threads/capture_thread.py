from PyQt5.QtCore import QThread, pyqtSignal

from handlers.biometrics_handler import BiometricsHandler

class CaptureThread(QThread):
  result_ready = pyqtSignal(tuple) 

  def __init__(self, biometrics_handler, device_name: str):
    super().__init__()
    self.biometrics_handler: BiometricsHandler = biometrics_handler
    self.device_name: str = device_name

  def run(self):
    capture_result = self.biometrics_handler.capture_fingerprint(self.device_name)
    if capture_result:
      self.result_ready.emit(capture_result)
