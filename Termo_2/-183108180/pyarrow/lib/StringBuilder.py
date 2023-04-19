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


from ._Weakrefable import _Weakrefable

class StringBuilder(_Weakrefable):
    """
    Builder class for UTF8 strings.
    
        This class exposes facilities for incrementally adding string values and
        building the null bitmap for a pyarrow.Array (type='string').
    """
    def append(self, value): # real signature unknown; restored from __doc__
        """
        StringBuilder.append(self, value)
        
                Append a single value to the builder.
        
                The value can either be a string/bytes object or a null value
                (np.nan or None).
        
                Parameters
                ----------
                value : string/bytes or np.nan/None
                    The value to append to the string array builder.
        """
        pass

    def append_values(self, values): # real signature unknown; restored from __doc__
        """
        StringBuilder.append_values(self, values)
        
                Append all the values from an iterable.
        
                Parameters
                ----------
                values : iterable of string/bytes or np.nan/None values
                    The values to append to the string array builder.
        """
        pass

    def finish(self): # real signature unknown; restored from __doc__
        """
        StringBuilder.finish(self)
        
                Return result of builder as an Array object; also resets the builder.
        
                Returns
                -------
                array : pyarrow.Array
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ StringBuilder.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ StringBuilder.__setstate_cython__(self, __pyx_state) """
        pass

    null_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



