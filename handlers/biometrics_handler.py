import ctypes

from config.config import fingerjet_url

class BiometricsHandler:
  def __init__(self):
     self.fingerjet_lib = ctypes.WinDLL(fingerjet_url)