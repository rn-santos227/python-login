import comtypes.client

from config.config import dpfj_url, dpfpdd_url

from library.biometrics import DPFPDD_SUCCESS, DPFPDD_CAPTURE_RESULT

class BiometricsHandler:
  def __init__(self):
    self.initialize()

  def initialize(self):
    try:
      self.dp_sdk = comtypes.client.CreateObject("DPFPDev.DPFPReader")
      status = self.dp_sdk.Status

      print("Fingerprint reader initialized. Status:", status)

    except Exception as e:
      print(f"Error initializing fingerprint reader: {e}")

  def capture_fingerprint(self):
    pass

  def verify_fingerprints(self, fingerprint_1, fingerprint_2) -> bool:
    return False