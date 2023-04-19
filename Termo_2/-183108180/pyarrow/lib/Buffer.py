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

class Buffer(_Weakrefable):
    """
    Buffer()
    
        The base class for all Arrow buffers.
    
        A buffer represents a contiguous memory area.  Many buffers will own
        their memory, though not all of them do.
    """
    def equals(self, Buffer_other): # real signature unknown; restored from __doc__
        """
        Buffer.equals(self, Buffer other)
        
                Determine if two buffers contain exactly the same data.
        
                Parameters
                ----------
                other : Buffer
        
                Returns
                -------
                are_equal : bool
                    True if buffer contents and size are equal
        """
        pass

    def hex(self): # real signature unknown; restored from __doc__
        """
        Buffer.hex(self)
        
                Compute hexadecimal representation of the buffer.
        
                Returns
                -------
                : bytes
        """
        pass

    def slice(self, offset=0, length=None): # real signature unknown; restored from __doc__
        """
        Buffer.slice(self, offset=0, length=None)
        
                Slice this buffer.  Memory is not copied.
        
                You can also use the Python slice notation ``buffer[start:stop]``.
        
                Parameters
                ----------
                offset : int, default 0
                    Offset from start of buffer to slice.
                length : int, default None
                    Length of slice (default is until end of Buffer starting from
                    offset).
        
                Returns
                -------
                sliced : Buffer
                    A logical view over this buffer.
        """
        pass

    def to_pybytes(self): # real signature unknown; restored from __doc__
        """
        Buffer.to_pybytes(self)
        
                Return this buffer as a Python bytes object. Memory is copied.
        """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __getitem__(self, *args, **kwargs): # real signature unknown
        """ Return self[key]. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __reduce_ex__(self, protocol): # real signature unknown; restored from __doc__
        """ Buffer.__reduce_ex__(self, protocol) """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    address = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        The buffer's address, as an integer.

        The returned address may point to CPU or device memory.
        Use `is_cpu()` to disambiguate.
        """

    is_cpu = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Whether the buffer is CPU-accessible.
        """

    is_mutable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Whether the buffer is mutable.
        """

    parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        The buffer size in bytes.
        """


    __hash__ = None
    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001970BCC5780>'


