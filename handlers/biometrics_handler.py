import time

from com.digitalpersona.uareu import Engine, Fid, Reader, UareUGlobal, UareUException # type: ignore

class BiometricsHandler:
  def __init__(self):
    print("SDK Initialized.")
    self.readers = []
    self._reader = None
    self._engine = UareUGlobal.GetEngine() 

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
    self.__set_device(device_name)

    if self._reader:
      try:
        img_format = Fid.Format.ANSI_381_2004
        img_proc = Reader.ImageProcessing.IMG_PROC_DEFAULT

        while True:
          status = self._reader.GetStatus()

          if status.status == Reader.ReaderStatus.READY:
            break

          elif status.status in [Reader.ReaderStatus.READY, Reader.ReaderStatus.NEED_CALIBRATION]:
             time.sleep(0.1)

          else:
            print(f"Reader error: {status.status}")
            return None
          
        capture_result = self._reader.Capture(img_format, img_proc, self._reader.GetCapabilities().resolutions[0], -1)

        if capture_result.quality == Reader.CaptureQuality.GOOD and capture_result.image is not None:
          print("Fingerprint captured successfully.")
          image = capture_result.image
          views = image.getViews()

          if len(views) > 0:
            first_view = views[0]
            image_data = first_view.getData()
            width = first_view.getWidth()
            height = first_view.getHeight()
            raw_data = bytes(image_data)

            self.close_reader()
            return raw_data, width, height 
        else:
          print(f"Capture failed: {capture_result.quality}")
          self.close_reader()
          return None
      
      except UareUException as err:
        print(f"Error initializing capture: {err}")
        self.close_reader()
        return None

  def verify_fingerprints(self, capture_result, student_fingerprint_data) -> bool:
    
    try:      
      if capture_result is None:
        print("Failed to capture fingerprint for verification.")
        return False
      
      result = self.engine.Compare(
        Engine.Candidate(capture_result),
        Engine.Candidate(student_fingerprint_data)
      )

    except UareUException as err:
      print(f"Error during fingerprint verification: {err}")
      return False

  def close_reader(self):
    if self._reader:
      try:
        self._reader.Close()
        print("Reader closed successfully.")

      except UareUException as err:
        print(f"Error closing reader: {err}")

  def __set_device(self, device_name):
    for i in range(len(self.readers)):
      reader = self.readers.get(i)

      if reader.GetDescription().name == device_name:
        self._reader = reader
        try:
          self._reader.Open(Reader.Priority.EXCLUSIVE)
          print(f"Selected reader: {device_name}")

        except UareUException as err:
          print(f"Failed to open reader: {err}")
          return None
        break