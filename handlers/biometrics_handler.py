import time

from PyQt5.QtCore import QObject
from PyQt5.QtGui import QImage

from com.digitalpersona.uareu import Fid, Reader, UareUGlobal, UareUException # type: ignore

class BiometricsHandler:
  def __init__(self):
    print("SDK Initialized.")
    self.readers = []
    self._reader = None

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
        self._reader = reader
        self._reader.Open(Reader.Priority.EXCLUSIVE)
        print(f"Selected reader: {device_name}")
        break

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

           view = capture_result.image.Views[0]
      
        else:
          print(f"Capture failed: {capture_result.quality}")
          return None
      
      except UareUException as err:
        print(f"Error initializing capture: {err}")

  def verify_fingerprints(self, fingerprint_1, fingerprint_2) -> bool:
    pass