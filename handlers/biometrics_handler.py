from com.digitalpersona.uareu import UareUGlobal, Reader, UareUException # type: ignore

class BiometricsHandler:
  def __init__(self):
    self.initialize()

  def initialize(self):
    pass

  def get_version(self):
    pass

  def get_devices(self) -> list[str]:
    try: 
      readers = UareUGlobal.GetReaderCollection()
      readers.GetReaders()

      devices = []

      if len(readers) == 0:
        print("No fingerprint readers found.")

      else:
        for i in range(len(readers)):
          reader = readers.get(i)

      return devices
    
    except UareUException as err:
      print(f"Biometrics SDK failed to initialized: {err}")

  def capture_fingerprint(self):
    pass

  def verify_fingerprints(self, fingerprint_1, fingerprint_2) -> bool:
    pass