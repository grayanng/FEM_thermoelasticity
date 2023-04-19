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

class Message(_Weakrefable):
    """
    Message()
    
        Container for an Arrow IPC message with metadata and optional body
    """
    def equals(self, Message_other): # real signature unknown; restored from __doc__
        """
        Message.equals(self, Message other)
        
                Returns True if the message contents (metadata and body) are identical
        
                Parameters
                ----------
                other : Message
        
                Returns
                -------
                are_equal : bool
        """
        pass

    def serialize(self, alignment=8, memory_pool=None): # real signature unknown; restored from __doc__
        """
        Message.serialize(self, alignment=8, memory_pool=None)
        
                Write message as encapsulated IPC message
        
                Parameters
                ----------
                alignment : int, default 8
                    Byte alignment for metadata and body
                memory_pool : MemoryPool, default None
                    Uses default memory pool if not specified
        
                Returns
                -------
                serialized : Buffer
        """
        pass

    def serialize_to(self, NativeFile_sink, alignment=8, memory_pool=None): # real signature unknown; restored from __doc__
        """
        Message.serialize_to(self, NativeFile sink, alignment=8, memory_pool=None)
        
                Write message to generic OutputStream
        
                Parameters
                ----------
                sink : NativeFile
                alignment : int, default 8
                    Byte alignment for metadata and body
                memory_pool : MemoryPool, default None
                    Uses default memory pool if not specified
        """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ Message.__reduce_cython__(self) """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ Message.__setstate_cython__(self, __pyx_state) """
        pass

    body = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    metadata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    metadata_version = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



