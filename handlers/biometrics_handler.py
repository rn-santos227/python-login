from com.digitalpersona.uareu import UareUGlobal, Reader # type: ignore

class BiometricsHandler:
  def __init__(self):
    self.initialize()

  def initialize(self):
    pass

  def get_version(self):
    pass

  def get_devices(self):
    readers = UareUGlobal.GetReaderCollection()
    readers.GetReaders()

    devices = []

    if len(readers) == 0:
      print("No fingerprint readers found.")

    else:
      reader = readers.get(0)
      device_name = reader.GetDescription().name
      print(f"Using reader: {reader.GetDescription().name}")
      devices.append(reader)

    return devices

  def capture_fingerprint(self):
    pass

  def verify_fingerprints(self, fingerprint_1, fingerprint_2) -> bool:
    pass