import ctypes

from config.config import dpfj_url

class BiometricsHandler:
  def __init__(self):
    self.fingerjet_lib = ctypes.WinDLL(dpfj_url)