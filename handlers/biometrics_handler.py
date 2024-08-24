import ctypes
from ctypes import byref

from config.config import dpfj_url, dpfpdd_url

from library.biometrics import DPFPDD_SUCCESS

class BiometricsHandler:
  def __init__(self):
    self.dpfj = ctypes.WinDLL(dpfj_url)
    self.dpfpdd = ctypes.WinDLL(dpfpdd_url) 
    result = self.dpfpdd.dpfpdd_init()

    if result != DPFPDD_SUCCESS:
      print(f"Error initializing SDK: {result}")

    else:
      print("SDK initialized successfully.")

  def capture_fingerprint(self):
    device = ctypes.c_void_p()
    result = self.dpfpdd.dpfpdd_open("Device1".encode('utf-8'), byref(device))

    if result != DPFPDD_SUCCESS:
      print(f"Error opening device: {result}")
      return None