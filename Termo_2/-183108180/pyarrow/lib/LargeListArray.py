# encoding: utf-8
# module pyarrow.lib
# from C:\Users\akharin\PycharmProjects\pythonProject\venv\lib\site-packages\pyarrow\lib.cp39-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import datetime as datetime # C:\Users\akharin\AppData\Local\Programs\Python\Python39\lib\datetime.py
import decimal as _pydecimal # C:\Users\akharin\AppData\Local\Programs\Python\Python39\lib\decimal.py
import numpy as np # C:\Users\akharin\PycharmProjects\pythonProject\venv\lib\site-packages\numpy\__init__.py
import os as os # C:\Users\akharin\AppData\Local\Programs\Python\Python39\lib\os.py
import sys as sys # <module 'sys' (built-in)>
import pickle as builtin_pickle # C:\Users\akharin\AppData\Local\Programs\Python\Python39\lib\pickle.py
import pickle as pickle # C:\Users\akharin\AppData\Local\Programs\Python\Python39\lib\pickle.py
import signal as signal # C:\Users\akharin\AppData\Local\Programs\Python\Python39\lib\signal.py
import threading as threading # C:\Users\akharin\AppData\Local\Programs\Python\Python39\lib\threading.py
import warnings as warnings # C:\Users\akharin\AppData\Local\Programs\Python\Python39\lib\warnings.py
import atexit as atexit # <module 'atexit' (built-in)>
import re as re # C:\Users\akharin\AppData\Local\Programs\Python\Python39\lib\re.py
import collections as collections # C:\Users\akharin\AppData\Local\Programs\Python\Python39\lib\collections\__init__.py
import codecs as codecs # C:\Users\akharin\AppData\Local\Programs\Python\Python39\lib\codecs.py
import time as time # <module 'time' (built-in)>
from _queue import QueueEmpty

import collections.abc as __collections_abc
import enum as __enum
import importlib._bootstrap as __importlib__bootstrap
import io as __io
import _io as ___io


from .BaseListArray import BaseListArray

class LargeListArray(BaseListArray):
    """
    Concrete class for Arrow arrays of a large list data type.
    
        Identical to ListArray, but 64-bit offsets.
    """
    def from_arrays(self, offsets, values, DataType_type=None, MemoryPool_pool=None, mask=None): # real signature unknown; restored from __doc__
        """
        LargeListArray.from_arrays(offsets, values, DataType type=None, MemoryPool pool=None, mask=None)
        
                Construct LargeListArray from arrays of int64 offsets and values.
        
                Parameters
                ----------
                offsets : Array (int64 type)
                values : Array (any type)
                type : DataType, optional
                    If not specified, a default ListType with the values' type is
                    used.
                pool : MemoryPool, optional
                mask : Array (boolean type), optional
                    Indicate which values are null (True) or not null (False).
        
                Returns
                -------
                list_array : LargeListArray
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    offsets = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Return the list offsets as an int64 array.

        The returned array will not have a validity bitmap, so you cannot
        expect to pass it to `LargeListArray.from_arrays` and get back the
        same list array if the original one has nulls.

        Returns
        -------
        offsets : Int64Array
        """

    values = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001970BCC5B40>'


