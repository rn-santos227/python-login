from com.digitalpersona.uareu import UareUGlobal, Reader, UareUException # type: ignore

class BiometricsHandler:
  def __init__(self):
    print("SDK Initialized")

  def initialize(self):
    result = UareUGlobal.GetEngine()
    print(dir(result))

  def get_version(self):
    pass

  def get_devices(self):
    try: 
      readers = UareUGlobal.GetReaderCollection()
      readers.GetReaders()

      devices = []

      if len(readers) == 0:
        print("No fingerprint readers found.")
        return []

      else:
        for i in range(len(readers)):
          reader = readers.get(i)
          device_name = reader.GetDescription().name
          print(f"Using reader: {device_name}")
          python_string = str(device_name)
          devices.append(python_string)

        return devices
    
    except UareUException as err:
      print(f"Biometrics SDK failed to initialized: {err}")

  def capture_fingerprint(self):
    pass

  def verify_fingerprints(self, fingerprint_1, fingerprint_2) -> bool:
    pass