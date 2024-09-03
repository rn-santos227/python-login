import ctypes
from ctypes import byref

from config.config import dpfpdd_url

from library.biometrics import DPFPDD_SUCCESS, DPFPDD_CAPTURE_RESULT

class BiometricsHandler:
  def __init__(self):
    self.initialize()

  def initialize(self):
    dp_sdk = ctypes.CDLL(dpfpdd_url)

  def capture_fingerprint(self):
    pass

  def verify_fingerprints(self, fingerprint_1, fingerprint_2) -> bool:
    return False