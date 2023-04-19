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


from .Exception import Exception

class FlightError(Exception):
    """
    FlightError(message=u'', extra_info=b'')
    
        The base class for Flight-specific errors.
    
        A server may raise this class or one of its subclasses to provide
        a more detailed error to clients.
    
        Parameters
        ----------
        message : str, optional
            The error message.
        extra_info : bytes, optional
            Extra binary error details that were provided by the
            server/will be sent to the client.
    
        Attributes
        ----------
        extra_info : bytes
            Extra binary error details that were provided by the
            server/will be sent to the client.
    """
    def __init__(self, message=None, extra_info=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce_cython__(self): # real signature unknown; restored from __doc__
        """ FlightError.__reduce_cython__(self) """
        pass

    def __setstate_cython__(self, __pyx_state): # real signature unknown; restored from __doc__
        """ FlightError.__setstate_cython__(self, __pyx_state) """
        pass

    __dict__ = None # (!) real value is 'mappingproxy({\'__init__\': <slot wrapper \'__init__\' of \'pyarrow._flight.FlightError\' objects>, \'__new__\': <built-in method __new__ of type object at 0x00007FFC337B9780>, \'__reduce_cython__\': <method \'__reduce_cython__\' of \'pyarrow._flight.FlightError\' objects>, \'__setstate_cython__\': <method \'__setstate_cython__\' of \'pyarrow._flight.FlightError\' objects>, \'__dict__\': <attribute \'__dict__\' of \'pyarrow._flight.FlightError\' objects>, \'__doc__\': "FlightError(message=u\'\', extra_info=b\'\')\\n\\n    The base class for Flight-specific errors.\\n\\n    A server may raise this class or one of its subclasses to provide\\n    a more detailed error to clients.\\n\\n    Parameters\\n    ----------\\n    message : str, optional\\n        The error message.\\n    extra_info : bytes, optional\\n        Extra binary error details that were provided by the\\n        server/will be sent to the client.\\n\\n    Attributes\\n    ----------\\n    extra_info : bytes\\n        Extra binary error details that were provided by the\\n        server/will be sent to the client.\\n  ", \'__pyx_vtable__\': <capsule object NULL at 0x000002441812E660>})'
    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000002441812E660>'


