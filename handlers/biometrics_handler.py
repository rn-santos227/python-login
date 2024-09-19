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
    features_1 = (ctypes.c_ubyte * 100000)()
    features_2 = (ctypes.c_ubyte * 100000)()

    self.dpfj.dpfj_create_feature_set(byref(fingerprint_1), byref(features_1))
    self.dpfj.dpfj_create_feature_set(byref(fingerprint_2), byref(features_2))

    score = ctypes.c_int()
    result =  self.dpfj.dpfj_verify(byref(features_1), byref(features_2), byref(score))

    if result == DPFPDD_SUCCESS and score.value > 0:
      print(f"Fingerprints matched with score: {score.value}")
      return True

    else:
      print(f"Fingerprints did not match.")
      return False