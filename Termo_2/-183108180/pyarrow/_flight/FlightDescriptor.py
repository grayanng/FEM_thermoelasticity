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


class FlightDescriptor(__pyarrow_lib._Weakrefable):
    """
    FlightDescriptor()
    A description of a data stream available from a Flight service.
    """
    @classmethod
    def deserialize(cls, type_cls, serialized): # real signature unknown; restored from __doc__
        """
        FlightDescriptor.deserialize(type cls, serialized)
        Parse the wire-format representation of this type.
        
                Useful when interoperating with non-Flight systems (e.g. REST
                services) that may want to return Flight types.
        """
        pass

    def for_command(self, command): # real signature unknown; restored from __doc__
        """
        FlightDescriptor.for_command(command)
        Create a FlightDescriptor for an opaque command.
        """
        pass

    def for_path(self, *path): # real signature unknown; restored from __doc__
        """
        FlightDescriptor.for_path(*path)
        Create a FlightDescriptor for a resource path.
        """
        pass

    def serialize(self): # real signature unknown; restored from __doc__
        """
        FlightDescriptor.serialize(self)
        Get the wire-format representation of this type.
        
                Useful when interoperating with non-Flight systems (e.g. REST
                services) that may want to return Flight types.
        """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
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

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ FlightDescriptor.__reduce_cython__(self) """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ FlightDescriptor.__setstate_cython__(self, __pyx_state) """
        pass

    command = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get the command for this descriptor."""

    descriptor_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get the type of this descriptor."""

    path = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get the path for this descriptor."""


    __hash__ = None
    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000002441812E780>'


