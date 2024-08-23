import ctypes

from config.config import dpfj_url, dpfpdd_url

class BiometricsHandler:
  def __init__(self):
    self.dpfj = ctypes.WinDLL(dpfj_url)