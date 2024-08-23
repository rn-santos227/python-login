import ctypes

DPFPDD_SUCCESS = 0
MAX_PATH = 260

class DPFPDD_DEV_INFO(ctypes.Structure):
  _fields_ = [("size", ctypes.c_int), ("name", ctypes.c_char * MAX_PATH)]