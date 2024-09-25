import threading

from PyQt5.QtCore import QThread, pyqtSignal

from handlers.biometrics_handler import BiometricsHandler

class CaptureThread(QThread):
  result_ready = pyqtSignal(tuple) 
  stop_flag = False

  def __init__(self, biometrics_handler, device_name: str):
    super().__init__()
    self.biometrics_handler: BiometricsHandler = biometrics_handler
    self.device_name: str = device_name
    self._stop_flag = threading.Event() 

  def run(self):
    while not self.stop_flag:
      capture_result = self.biometrics_handler.capture_fingerprint(self.device_name) 
      if self._stop_flag:
        break

      if capture_result:
        self.result_ready.emit(capture_result)
      
      else:
        self.result_ready.emit((None, None, None))
      
      self.msleep(200)

  def stop(self):
    self.stop_flag = True
    self.wait(500)
