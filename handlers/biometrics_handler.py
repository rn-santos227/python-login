import win32com.client

class BiometricsHandler:
  def __init__(self):
    try:
      self.device_control = win32com.client.Dispatch("DPFPDevX.DeviceControl")

    except Exception as e:
      print(f"Failed to initialize fingerprint scanner: {e}")
      self.device = None