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


from .object import object

class _PandasAPIShim(object):
    """
    _PandasAPIShim()
    
        Lazy pandas importer that isolates usages of pandas APIs and avoids
        importing pandas until it's actually needed
    """
    def assert_frame_equal(self, *args, **kwargs): # real signature unknown; restored from __doc__
        """ _PandasAPIShim.assert_frame_equal(self, *args, **kwargs) """
        pass

    def data_frame(self, *args, **kwargs): # real signature unknown; restored from __doc__
        """ _PandasAPIShim.data_frame(self, *args, **kwargs) """
        pass

    def get_rangeindex_attribute(self, level, name): # real signature unknown; restored from __doc__
        """ _PandasAPIShim.get_rangeindex_attribute(self, level, name) """
        pass

    def get_values(self, obj): # real signature unknown; restored from __doc__
        """
        _PandasAPIShim.get_values(self, obj)
        
                Get the underlying array values of a pandas Series or Index in the
                format (np.ndarray or pandas ExtensionArray) as we need them.
        
                Assumes obj is a pandas Series or Index.
        """
        pass

    def infer_dtype(self, obj): # real signature unknown; restored from __doc__
        """ _PandasAPIShim.infer_dtype(self, obj) """
        pass

    def is_array_like(self, obj): # real signature unknown; restored from __doc__
        """ _PandasAPIShim.is_array_like(self, obj) """
        pass

    def is_categorical(self, obj): # real signature unknown; restored from __doc__
        """ _PandasAPIShim.is_categorical(self, obj) """
        pass

    def is_data_frame(self, obj): # real signature unknown; restored from __doc__
        """ _PandasAPIShim.is_data_frame(self, obj) """
        pass

    def is_datetimetz(self, obj): # real signature unknown; restored from __doc__
        """ _PandasAPIShim.is_datetimetz(self, obj) """
        pass

    def is_extension_array_dtype(self, obj): # real signature unknown; restored from __doc__
        """ _PandasAPIShim.is_extension_array_dtype(self, obj) """
        pass

    def is_index(self, obj): # real signature unknown; restored from __doc__
        """ _PandasAPIShim.is_index(self, obj) """
        pass

    def is_series(self, obj): # real signature unknown; restored from __doc__
        """ _PandasAPIShim.is_series(self, obj) """
        pass

    def is_sparse(self, obj): # real signature unknown; restored from __doc__
        """ _PandasAPIShim.is_sparse(self, obj) """
        pass

    def pandas_dtype(self, dtype): # real signature unknown; restored from __doc__
        """ _PandasAPIShim.pandas_dtype(self, dtype) """
        pass

    def series(self, *args, **kwargs): # real signature unknown; restored from __doc__
        """ _PandasAPIShim.series(self, *args, **kwargs) """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ _PandasAPIShim.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ _PandasAPIShim.__setstate_cython__(self, __pyx_state) """
        pass

    categorical_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    compat = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    datetimetz_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    extension_dtype = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    has_sparse = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    have_pandas = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    loose_version = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pd = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    version = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _array_like_types = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _categorical_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _compat_module = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _data_frame = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _datetimetz_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _extension_array = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _extension_dtype = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _index = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _is_extension_array_dtype = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _loose_version = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _pd = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _pd024 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _series = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _types_api = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _version = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001970BCC5390>'


