from com.digitalpersona.uareu import UareUGlobal, Reader

class BiometricsHandler:
  def __init__(self):
    self.initialize()
    self.get_devices()

  def initialize(self):
    result = UareUGlobal.Init()

    if result == UareUGlobal.DPFPDD_SUCCESS:
      print("SDK initialized successfully.")
    
    else:
      print(f"SDK initialization failed with error code: {result}")

  def get_version(self):
    pass

  def get_devices(self):
    readers = UareUGlobal.GetReaderCollection()

    if len(readers) == 0:
      print("No fingerprint readers found.")

    else:
      reader = readers.get(0)
      print(f"Using reader: {reader.GetDescription().name}")

  def capture_fingerprint(self):
    pass

  def verify_fingerprints(self, fingerprint_1, fingerprint_2) -> bool:
    pass