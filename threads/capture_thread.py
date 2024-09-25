import threading

from PyQt5.QtCore import QThread, pyqtSignal

from handlers.biometrics_handler import BiometricsHandler

class CaptureThread(QThread):
  result_ready = pyqtSignal(tuple) 

  def __init__(self, biometrics_handler, device_name: str):
    super().__init__()
    self.biometrics_handler: BiometricsHandler = biometrics_handler
    self.device_name: str = device_name
    self._stop_flag = threading.Event() 

  def run(self):
    print("Fingerprint capture thread started.")
    while not self._stop_flag.is_set():
      capture_result = self.biometrics_handler.capture_fingerprint(self.device_name) 

      if capture_result:
        self.result_ready.emit(capture_result)
      
      else:
        self.result_ready.emit((None, None, None))
      
      self.msleep(500) 
      
    print("Thread exiting...")

  def stop(self):
    print("Stop method called for fingerprint scanner.")
    self._stop_flag.set() 
    self.wait(500) 
    print("Thread stopped")
