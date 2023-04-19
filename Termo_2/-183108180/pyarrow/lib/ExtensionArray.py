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


from .Array import Array

class ExtensionArray(Array):
    """ Concrete class for Arrow extension arrays. """
    def from_storage(self, BaseExtensionType_typ, Array_storage): # real signature unknown; restored from __doc__
        """
        ExtensionArray.from_storage(BaseExtensionType typ, Array storage)
        
                Construct ExtensionArray from type and storage array.
        
                Parameters
                ----------
                typ : DataType
                    The extension type for the result array.
                storage : Array
                    The underlying storage for the result array.
        
                Returns
                -------
                ext_array : ExtensionArray
        """
        pass

    def to_numpy(self, **kwargs): # real signature unknown; restored from __doc__
        """
        ExtensionArray.to_numpy(self, **kwargs)
        
                Convert extension array to a numpy ndarray.
        
                This method simply delegates to the underlying storage array.
        
                Parameters
                ----------
                **kwargs : dict, optional
                    See `Array.to_numpy` for parameter description.
        
                See Also
                --------
                Array.to_numpy
        """
        pass

    def _to_pandas(self, options, **kwargs): # real signature unknown; restored from __doc__
        """ ExtensionArray._to_pandas(self, options, **kwargs) """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    storage = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001970BCC5DE0>'


