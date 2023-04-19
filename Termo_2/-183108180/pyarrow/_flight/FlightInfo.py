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


class FlightInfo(__pyarrow_lib._Weakrefable):
    """
    FlightInfo(Schema schema, FlightDescriptor descriptor, endpoints, total_records, total_bytes)
    A description of a Flight stream.
    """
    @classmethod
    def deserialize(cls, type_cls, serialized): # real signature unknown; restored from __doc__
        """
        FlightInfo.deserialize(type cls, serialized)
        Parse the wire-format representation of this type.
        
                Useful when interoperating with non-Flight systems (e.g. REST
                services) that may want to return Flight types.
        """
        pass

    def serialize(self): # real signature unknown; restored from __doc__
        """
        FlightInfo.serialize(self)
        Get the wire-format representation of this type.
        
                Useful when interoperating with non-Flight systems (e.g. REST
                services) that may want to return Flight types.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        """
        Create a FlightInfo object from a schema, descriptor, and endpoints.
        
                Parameters
                ----------
                schema : Schema
                    the schema of the data in this flight.
                descriptor : FlightDescriptor
                    the descriptor for this flight.
                endpoints : list of FlightEndpoint
                    a list of endpoints where this flight is available.
                total_records : int
                    the total records in this flight, or -1 if unknown
                total_bytes : int
                    the total bytes in this flight, or -1 if unknown
        """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ FlightInfo.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ FlightInfo.__setstate_cython__(self, __pyx_state) """
        pass

    descriptor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The descriptor of the data in this flight."""

    endpoints = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The endpoints where this flight is available."""

    schema = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The schema of the data in this flight."""

    total_bytes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The size in bytes of the data in this flight, or -1 if unknown."""

    total_records = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The total record count of this flight, or -1 if unknown."""



