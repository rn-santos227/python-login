from com.digitalpersona.uareu import UareUGlobal, Reader, UareUException # type: ignore

class BiometricsHandler:
  def __init__(self):
    self.initialize()

  def initialize(self):
    pass

  def get_version(self):
    pass

  def get_devices(self):
    try: 
      readers = UareUGlobal.GetReaderCollection()
      readers.GetReaders()

      devices = []

      if len(readers) == 0:
        print("No fingerprint readers found.")

      else:
        reader = readers.get(0)
        device_name = reader.GetDescription().name
        print(f"Using reader: {device_name}")
        devices.append(device_name)

      return devices
    
    except UareUException as err:
      print(f"Biometrics SDK failed to initialized: {err}")

  def capture_fingerprint(self):
    pass

  def verify_fingerprints(self, fingerprint_1, fingerprint_2) -> bool:
    pass