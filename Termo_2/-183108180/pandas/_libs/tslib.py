# encoding: utf-8
# module pandas._libs.tslib
# from C:\Users\akharin\PycharmProjects\pythonProject\venv\lib\site-packages\pandas\_libs\tslib.cp39-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import warnings as warnings # C:\Users\akharin\AppData\Local\Programs\Python\Python39\lib\warnings.py
import numpy as np # C:\Users\akharin\PycharmProjects\pythonProject\venv\lib\site-packages\numpy\__init__.py
import pytz as pytz # C:\Users\akharin\PycharmProjects\pythonProject\venv\lib\site-packages\pytz\__init__.py
from pandas._libs.tslibs.dtypes import Resolution

from pandas._libs.tslibs.np_datetime import OutOfBoundsDatetime

from pandas._libs.tslibs.parsing import parse_datetime_string

from pandas._libs.tslibs.timestamps import Timestamp

from pandas._libs.tslibs.vectorized import get_resolution


# functions

def array_to_datetime(*args, **kwargs): # real signature unknown
    """
    Converts a 1D array of date-like values to a numpy array of either:
            1) datetime64[ns] data
            2) datetime.datetime objects, if OutOfBoundsDatetime or TypeError
               is encountered
    
        Also returns a pytz.FixedOffset if an array of strings with the same
        timezone offset is passed and utc=True is not passed. Otherwise, None
        is returned
    
        Handles datetime.date, datetime.datetime, np.datetime64 objects, numeric,
        strings
    
        Parameters
        ----------
        values : ndarray of object
             date-like objects to convert
        errors : str, default 'raise'
             error behavior when parsing
        dayfirst : bool, default False
             dayfirst parsing behavior when encountering datetime strings
        yearfirst : bool, default False
             yearfirst parsing behavior when encountering datetime strings
        utc : bool, default False
             indicator whether the dates should be UTC
        require_iso8601 : bool, default False
             indicator whether the datetime string should be iso8601
        allow_mixed : bool, default False
            Whether to allow mixed datetimes and integers.
    
        Returns
        -------
        np.ndarray
            May be datetime64[ns] or object dtype
        tzinfo or None
    """
    pass

def array_with_unit_to_datetime(*args, **kwargs): # real signature unknown
    """
    Convert the ndarray to datetime according to the time unit.
    
        This function converts an array of objects into a numpy array of
        datetime64[ns]. It returns the converted array
        and also returns the timezone offset
    
        if errors:
          - raise: return converted values or raise OutOfBoundsDatetime
              if out of range on the conversion or
              ValueError for other conversions (e.g. a string)
          - ignore: return non-convertible values as the same unit
          - coerce: NaT for non-convertibles
    
        Parameters
        ----------
        values : ndarray
             Date-like objects to convert.
        unit : str
             Time unit to use during conversion.
        errors : str, default 'raise'
             Error behavior when parsing.
    
        Returns
        -------
        result : ndarray of m8 values
        tz : parsed timezone offset or None
    """
    pass

def find_stack_level(): # reliably restored by inspect
    """
    Find the first place in the stack that is not inside pandas
        (tests notwithstanding).
    """
    pass

def format_array_from_datetime(*args, **kwargs): # real signature unknown
    """
    return a np object array of the string formatted values
    
        Parameters
        ----------
        values : a 1-d i8 array
        tz : tzinfo or None, default None
        format : str or None, default None
              a strftime capable string
        na_rep : optional, default is None
              a nat format
        reso : NPY_DATETIMEUNIT, default NPY_FR_ns
    
        Returns
        -------
        np.ndarray[object]
    """
    pass

def _test_parse_iso8601(*args, **kwargs): # real signature unknown
    """
    TESTING ONLY: Parse string into Timestamp using iso8601 parser. Used
        only for testing, actual construction uses `convert_str_to_tsobject`
    """
    pass

def __pyx_unpickle_Enum(*args, **kwargs): # real signature unknown
    pass

# no classes
# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x000001EBE1F8CB50>'

__spec__ = None # (!) real value is "ModuleSpec(name='pandas._libs.tslib', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x000001EBE1F8CB50>, origin='C:\\\\Users\\\\akharin\\\\PycharmProjects\\\\pythonProject\\\\venv\\\\lib\\\\site-packages\\\\pandas\\\\_libs\\\\tslib.cp39-win_amd64.pyd')"

__test__ = {}

