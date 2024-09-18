import ctypes
from ctypes import Structure, c_int, c_char_p, byref

DPFPDD_SUCCESS = 0
MAX_PATH = 260

class DPFPDD_DEV_INFO(ctypes.Structure):
  _fields_ = [("size", ctypes.c_int), ("name", ctypes.c_char * MAX_PATH)]

class DPFPDD_CAPTURE_RESULT(ctypes.Structure):
  _fields_ = [("quality", ctypes.c_int), ("size", ctypes.c_int)]

class DPFPDD_IMAGE(ctypes.Structure):
  _fields_ = [("width", ctypes.c_int), ("height", ctypes.c_int), ("image", ctypes.POINTER(ctypes.c_ubyte))]

class DPFPDD_VERSION(Structure):
  _fields_ = [("major", c_int),
    ("minor", c_int),
    ("maintenance", c_int),
    ("build", c_int)
  ]
