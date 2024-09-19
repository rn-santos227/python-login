import ctypes
from ctypes import c_int, byref

from config.config import device_name

from library.biometrics import DPFPDD_SUCCESS, DPFPDD_VERSION

class BiometricsHandler:
  def __init__(self):
    self.initialize()

  def initialize(self):
    pass

  def get_version(self):
    pass

  def get_devices(self):
    pass

  def capture_fingerprint(self):
    pass


  def verify_fingerprints(self, fingerprint_1, fingerprint_2) -> bool:
    pass