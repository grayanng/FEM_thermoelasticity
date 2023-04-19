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


from .NativeFile import NativeFile

class PythonFile(NativeFile):
    """
    A stream backed by a Python file object.
    
        This class allows using Python file objects with arbitrary Arrow
        functions, including functions written in another language than Python.
    
        As a downside, there is a non-zero redirection cost in translating
        Arrow stream calls to Python method calls.  Furthermore, Python's
        Global Interpreter Lock may limit parallelism in some situations.
    
        Examples
        --------
        >>> import io
        >>> import pyarrow as pa
        >>> pa.PythonFile(io.BytesIO())
        <pyarrow.PythonFile closed=False own_file=False is_seekable=False is_writable=True is_readable=False>
    """
    def readline(self, size=None): # real signature unknown; restored from __doc__
        """ PythonFile.readline(self, size=None) """
        pass

    def readlines(self, hint=None): # real signature unknown; restored from __doc__
        """ PythonFile.readlines(self, hint=None) """
        pass

    def truncate(self, pos=None): # real signature unknown; restored from __doc__
        """ PythonFile.truncate(self, pos=None) """
        pass

    def __init__(self, io_BytesIO, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ PythonFile.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ PythonFile.__setstate_cython__(self, __pyx_state) """
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001970D9158A0>'


