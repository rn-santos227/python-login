import win32com.client

class BiometricsHandler:
  def __init__(self):
    try:
      self.device_control = win32com.client.Dispatch("DPFPDevX.DeviceControl")
      self.device = self.device_control.Devices(0)
      self.device.Open(1)
      print("Fingerprint scanner initialized successfully.")

    except Exception as e:
      print(f"Failed to initialize fingerprint scanner: {e}")
      self.device = None