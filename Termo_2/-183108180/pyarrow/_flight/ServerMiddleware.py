# encoding: utf-8
# module pyarrow._flight
# from C:\Users\akharin\PycharmProjects\pythonProject\venv\lib\site-packages\pyarrow\_flight.cp39-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import collections as collections # C:\Users\akharin\AppData\Local\Programs\Python\Python39\lib\collections\__init__.py
import contextlib as contextlib # C:\Users\akharin\AppData\Local\Programs\Python\Python39\lib\contextlib.py
import enum as enum # C:\Users\akharin\AppData\Local\Programs\Python\Python39\lib\enum.py
import re as re # C:\Users\akharin\AppData\Local\Programs\Python\Python39\lib\re.py
import socket as socket # C:\Users\akharin\AppData\Local\Programs\Python\Python39\lib\socket.py
import time as time # <module 'time' (built-in)>
import threading as threading # C:\Users\akharin\AppData\Local\Programs\Python\Python39\lib\threading.py
import warnings as warnings # C:\Users\akharin\AppData\Local\Programs\Python\Python39\lib\warnings.py
import weakref as weakref # C:\Users\akharin\AppData\Local\Programs\Python\Python39\lib\weakref.py
import pyarrow.lib as lib # C:\Users\akharin\PycharmProjects\pythonProject\venv\lib\site-packages\pyarrow\lib.cp39-win_amd64.pyd
from pyarrow.lib import (ArrowCancelled, ArrowException, ArrowInvalid, 
    SignalStopHandler, _ReadPandasMixin, as_buffer, frombytes, tobytes)

import enum as __enum
import importlib._bootstrap as __importlib__bootstrap
import pyarrow.lib as __pyarrow_lib


class ServerMiddleware(__pyarrow_lib._Weakrefable):
    """
    Server-side middleware for a call, instantiated per RPC.
    
        Methods here should be fast and must be infalliable: they should
        not raise exceptions or stall indefinitely.
    """
    def call_completed(self, exception): # real signature unknown; restored from __doc__
        """
        ServerMiddleware.call_completed(self, exception)
        A callback when the call finishes.
        
                Parameters
                ----------
                exception : pyarrow.ArrowException
                    If the call errored, this is the equivalent
                    exception. Will be None if the call succeeded.
        """
        pass

    def sending_headers(self): # real signature unknown; restored from __doc__
        """
        ServerMiddleware.sending_headers(self)
        A callback before headers are sent.
        
                Returns
                -------
                headers : dict
                    A dictionary of header values to add to the response, or
                    None if no headers are to be added. The dictionary should
                    have string keys and string or list-of-string values.
        
                    Bytes values are allowed, but the underlying transport may
                    not support them or may restrict them. For gRPC, binary
                    values are only allowed on headers ending in "-bin".
        
                    Header names must be lowercase ASCII.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ ServerMiddleware.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ ServerMiddleware.__setstate_cython__(self, __pyx_state) """
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000002441812EF60>'


