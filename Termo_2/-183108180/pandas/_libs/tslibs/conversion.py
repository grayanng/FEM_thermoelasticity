# encoding: utf-8
# module pandas._libs.tslibs.conversion
# from C:\Users\akharin\PycharmProjects\pythonProject\venv\lib\site-packages\pandas\_libs\tslibs\conversion.cp39-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import warnings as warnings # C:\Users\akharin\AppData\Local\Programs\Python\Python39\lib\warnings.py
import numpy as np # C:\Users\akharin\PycharmProjects\pythonProject\venv\lib\site-packages\numpy\__init__.py
import pytz as pytz # C:\Users\akharin\PycharmProjects\pythonProject\venv\lib\site-packages\pytz\__init__.py
from pandas._libs.tslibs.np_datetime import (OutOfBoundsDatetime, 
    OutOfBoundsTimedelta)

from pandas._libs.tslibs.parsing import parse_datetime_string


# functions

def find_stack_level(): # reliably restored by inspect
    """
    Find the first place in the stack that is not inside pandas
        (tests notwithstanding).
    """
    pass

def localize_pydatetime(*args, **kwargs): # real signature unknown
    """
    Take a datetime/Timestamp in UTC and localizes to timezone tz.
    
        Parameters
        ----------
        dt : datetime or Timestamp
        tz : tzinfo or None
    
        Returns
        -------
        localized : datetime or Timestamp
    """
    pass

def precision_from_unit(*args, **kwargs): # real signature unknown
    """
    Return a casting of the unit represented to nanoseconds + the precision
        to round the fractional part.
    
        Notes
        -----
        The caller is responsible for ensuring that the default value of "ns"
        takes the place of None.
    """
    pass

def __pyx_unpickle_Enum(*args, **kwargs): # real signature unknown
    pass

# classes

class _TSObject(object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    dts = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    fold = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tzinfo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



# variables with complex values

DT64NS_DTYPE = None # (!) real value is "dtype('<M8[ns]')"

TD64NS_DTYPE = None # (!) real value is "dtype('<m8[ns]')"

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x0000021BC974C4F0>'

__pyx_capi__ = {
    'cast_from_unit': None, # (!) real value is '<capsule object "__pyx_t_5numpy_int64_t (PyObject *, PyObject *)" at 0x0000021BC97B1450>'
    'convert_datetime_to_tsobject': None, # (!) real value is '<capsule object "struct __pyx_obj_6pandas_5_libs_6tslibs_10conversion__TSObject *(PyDateTime_DateTime *, PyDateTime_TZInfo *, struct __pyx_opt_args_6pandas_5_libs_6tslibs_10conversion_convert_datetime_to_tsobject *__pyx_optional_args)" at 0x0000021BC97B13C0>'
    'convert_to_tsobject': None, # (!) real value is '<capsule object "struct __pyx_obj_6pandas_5_libs_6tslibs_10conversion__TSObject *(PyObject *, PyDateTime_TZInfo *, PyObject *, int, int, struct __pyx_opt_args_6pandas_5_libs_6tslibs_10conversion_convert_to_tsobject *__pyx_optional_args)" at 0x0000021BC97B1390>'
    'get_datetime64_nanos': None, # (!) real value is '<capsule object "__pyx_t_5numpy_int64_t (PyObject *)" at 0x0000021BC97B13F0>'
    'localize_pydatetime': None, # (!) real value is '<capsule object "PyDateTime_DateTime *(PyDateTime_DateTime *, PyDateTime_TZInfo *, int __pyx_skip_dispatch)" at 0x0000021BC97B1420>'
    'maybe_localize_tso': None, # (!) real value is '<capsule object "PyObject *(struct __pyx_obj_6pandas_5_libs_6tslibs_10conversion__TSObject *, PyDateTime_TZInfo *, NPY_DATETIMEUNIT)" at 0x0000021BC97B14B0>'
    'precision_from_unit': None, # (!) real value is '<capsule object "__pyx_ctuple___dunderpyx_t_5numpy_int64_t__and_int (PyObject *, int __pyx_skip_dispatch)" at 0x0000021BC97B1480>'
}

__spec__ = None # (!) real value is "ModuleSpec(name='pandas._libs.tslibs.conversion', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x0000021BC974C4F0>, origin='C:\\\\Users\\\\akharin\\\\PycharmProjects\\\\pythonProject\\\\venv\\\\lib\\\\site-packages\\\\pandas\\\\_libs\\\\tslibs\\\\conversion.cp39-win_amd64.pyd')"

__test__ = {}

