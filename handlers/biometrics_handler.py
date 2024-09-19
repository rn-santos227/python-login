from com.digitalpersona.uareu import UareUGlobal, Reader

class BiometricsHandler:
  def __init__(self):
    self.initialize()

  def initialize(self):
    pass

  def get_version(self):
    pass

  def get_devices(self):
    readers = UareUGlobal.GetReaderCollection()

  def capture_fingerprint(self):
    pass

  def verify_fingerprints(self, fingerprint_1, fingerprint_2) -> bool:
    pass