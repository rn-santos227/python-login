import ctypes

from config.config import dpfj_url, dpfpdd_url

from library.biometrics import DPFPDD_SUCCESS

class BiometricsHandler:
  def __init__(self):
    self.dpfj = ctypes.WinDLL(dpfj_url)
    self.dpfpdd = ctypes.WinDLL(dpfpdd_url) 
    result = self.dpfpdd.dpfpdd_init()

    if result != DPFPDD_SUCCESS:
      print(f"Error initializing SDK: {result}")