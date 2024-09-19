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
    dpfpdd_version_func = self.dpfpdd.dpfpdd_get_version
    dpfpdd_version_func.argtypes = [ctypes.POINTER(DPFPDD_VERSION)]
    dpfpdd_version_func.restype = c_int

    version_info = DPFPDD_VERSION()
    result = dpfpdd_version_func(byref(version_info))

    if result == DPFPDD_SUCCESS:
      print(f"SDK Version: {version_info.major}.{version_info.minor}.{version_info.maintenance}.{version_info.build}")

    else:
      print(f"An error occurred: {result}")

  def get_devices(self):
    pass

  def capture_fingerprint(self):
    dpfpdd_open = self.dpfpdd.dpfpdd_open
    dpfpdd_open.restype = ctypes.c_int
    dpfpdd_open.argtypes = [ctypes.c_char_p, ctypes.POINTER(ctypes.c_void_p)]

    p1 = ctypes.c_char_p(device_name.encode("utf-8"))
    p2 = ctypes.c_void_p()

    result = dpfpdd_open(p1, ctypes.pointer(p2))

    if result != DPFPDD_SUCCESS:
      print(f"Error opening device: {result}")
      return None


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