# encoding: utf-8
# module pyarrow._compute
# from C:\Users\akharin\PycharmProjects\pythonProject\venv\lib\site-packages\pyarrow\_compute.cp39-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import sys as sys # <module 'sys' (built-in)>
import pyarrow.lib as lib # C:\Users\akharin\PycharmProjects\pythonProject\venv\lib\site-packages\pyarrow\lib.cp39-win_amd64.pyd
import inspect as inspect # C:\Users\akharin\AppData\Local\Programs\Python\Python39\lib\inspect.py
import numpy as np # C:\Users\akharin\PycharmProjects\pythonProject\venv\lib\site-packages\numpy\__init__.py
from pyarrow.lib import ArrowInvalid, frombytes, tobytes

import pyarrow.lib as __pyarrow_lib


from .FunctionOptions import FunctionOptions

class _CastOptions(FunctionOptions):
    # no doc
    def is_safe(self): # real signature unknown; restored from __doc__
        """ _CastOptions.is_safe(self) """
        pass

    def _set_options(self, DataType_target_type, allow_int_overflow, allow_time_truncate, allow_time_overflow, allow_decimal_truncate, allow_float_truncate, allow_invalid_utf8): # real signature unknown; restored from __doc__
        """ _CastOptions._set_options(self, DataType target_type, allow_int_overflow, allow_time_truncate, allow_time_overflow, allow_decimal_truncate, allow_float_truncate, allow_invalid_utf8) """
        pass

    def _set_safe(self): # real signature unknown; restored from __doc__
        """ _CastOptions._set_safe(self) """
        pass

    def _set_type(self, target_type=None): # real signature unknown; restored from __doc__
        """ _CastOptions._set_type(self, target_type=None) """
        pass

    def _set_unsafe(self): # real signature unknown; restored from __doc__
        """ _CastOptions._set_unsafe(self) """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ _CastOptions.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ _CastOptions.__setstate_cython__(self, __pyx_state) """
        pass

    allow_decimal_truncate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    allow_float_truncate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    allow_int_overflow = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    allow_invalid_utf8 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    allow_time_overflow = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    allow_time_truncate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001FC28B43810>'


