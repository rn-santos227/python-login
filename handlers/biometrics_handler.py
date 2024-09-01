import ctypes
from ctypes import byref

from config.config import dpfj_url, dpfpdd_url

from library.biometrics import DPFPDD_SUCCESS, DPFPDD_CAPTURE_RESULT

class BiometricsHandler:
  def __init__(self):
    self.dpfj = ctypes.WinDLL(dpfj_url)
    self.dpfpdd = ctypes.WinDLL(dpfpdd_url) 
    result = self.dpfpdd.dpfpdd_init()

    if result != DPFPDD_SUCCESS:
      print(f"Error initializing SDK: {result}")

    else:
      print("SDK initialized successfully.")

  def initialize(self):
    self.dpfj = ctypes.WinDLL(dpfj_url)
    self.dpfpdd = ctypes.WinDLL(dpfpdd_url) 
    result = self.dpfpdd.dpfpdd_init()

  def capture_fingerprint(self):
    device = ctypes.c_void_p()
    result = self.dpfpdd.dpfpdd_open("Device1".encode('utf-8'), byref(device))

    if result != DPFPDD_SUCCESS:
      print(f"Error opening device: {result}")
      return None
    
    capture_result = DPFPDD_CAPTURE_RESULT()
    capture_result.size = ctypes.sizeof(capture_result)

    image_buffer = (ctypes.c_ubyte * 100000)()
    fingerprint_data = bytes(image_buffer)

    if result != DPFPDD_SUCCESS:
      print(f"Error capturing fingerprint: {result}")
      return None
    
    print(f"Fingerprint captured successfully with quality: {capture_result.quality}")
    return fingerprint_data

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