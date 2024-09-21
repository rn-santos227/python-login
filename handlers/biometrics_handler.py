from com.digitalpersona.uareu import  Fid, ImageProcessing, UareUGlobal, UareUException # type: ignore

class BiometricsHandler:
  def __init__(self):
    print("SDK Initialized.")
    self.readers = []
    self.selected_reader = None

  def get_version(self):
    pass

  def get_devices(self):
    try: 
      readers = UareUGlobal.GetReaderCollection()
      readers.GetReaders()

      self.readers = readers
      devices = []

      if len(readers) == 0:
        print("No fingerprint readers found.")

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
      return devices

  def capture_fingerprint(self, device_name):
    for i in range(len(self.readers)):
      reader = self.readers.get(i)
      if reader.GetDescription().name == device_name:
        self.selected_reader = reader
        break
    
    try:
      self.selected_reader.StartCapture()

    except UareUException as err:
      print(f"Error capturing fingerprint: {err}")
      return None

  def verify_fingerprints(self, fingerprint_1, fingerprint_2) -> bool:
    pass