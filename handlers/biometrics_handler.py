from com.digitalpersona.uareu import  Fid, ImageProcessing, UareUGlobal, UareUException # type: ignore

class BiometricsHandler:
  def __init__(self):
    print("SDK Initialized.")
    self.devices = []

  def get_version(self):
    pass

  def get_devices(self):
    try: 
      readers = UareUGlobal.GetReaderCollection()
      readers.GetReaders()

      self.device = []

      if len(readers) == 0:
        print("No fingerprint readers found.")
        return []

      else:
        for i in range(len(readers)):
          reader = readers.get(i)
          device_name = reader.GetDescription().name
          print(f"Using reader: {device_name}")
          python_string = str(device_name)
    
    except UareUException as err:
      print(f"Biometrics SDK failed to initialized: {err}")

  def capture_fingerprint(self, device):
    pass

  def verify_fingerprints(self, fingerprint_1, fingerprint_2) -> bool:
    pass