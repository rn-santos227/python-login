import ctypes
from ctypes import byref

from config.config import device_name

from library.biometrics import DPFPDD_SUCCESS, DPFPDD_CAPTURE_RESULT

class BiometricsHandler:
  def __init__(self):
    self.initialize()

  def initialize(self):
    self.dpfpdd = ctypes.CDLL("dpfpdd.dll") 
    dpfpdd_init  = self.dpfpdd.dpfpdd_init
    dpfpdd_init.restype = ctypes.c_int
    result = dpfpdd_init()

    if result != DPFPDD_SUCCESS:
      print(f"Error initializing SDK: {result}")

    else:
      print("SDK initialized successfully.")

  def get_version(self):
    dpfpdd_version  = self.dpfpdd.dpfpdd_init
    result = dpfpdd_version()

    if result != DPFPDD_SUCCESS:
      print(f"An Error has been Detected: {result}")

    else:
      print(f"SDK Version: {result}")

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