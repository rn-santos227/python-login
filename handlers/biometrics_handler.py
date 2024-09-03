import comtypes.client

from config.config import dpfj_url, dpfpdd_url

from library.biometrics import DPFPDD_SUCCESS, DPFPDD_CAPTURE_RESULT

class BiometricsHandler:
  def __init__(self):
    self.initialize()

  def initialize(self):
    pass

  def capture_fingerprint(self):
    pass

  def verify_fingerprints(self, fingerprint_1, fingerprint_2) -> bool:
    return False