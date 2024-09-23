from PyQt5.QtCore import QThread, pyqtSignal

class CaptureThread(QThread):
  result_ready = pyqtSignal(tuple) 

