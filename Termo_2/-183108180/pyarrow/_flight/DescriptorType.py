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


class DescriptorType(__enum.Enum):
    """
    The type of a FlightDescriptor.
    
        Attributes
        ----------
    
        UNKNOWN
            An unknown descriptor type.
    
        PATH
            A Flight stream represented by a path.
    
        CMD
            A Flight stream represented by an application-defined command.
    """
    def _generate_next_value_(name, start, count, last_values): # reliably restored by inspect
        """
        Generate the next value when not given.
        
                name: the name of the member
                start: the initial start value or None
                count: the number of existing members
                last_value: the last value assigned or None
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(cls, value): # reliably restored by inspect
        # no doc
        pass

    CMD = None # (!) real value is '<DescriptorType.CMD: 2>'
    PATH = None # (!) real value is '<DescriptorType.PATH: 1>'
    UNKNOWN = None # (!) real value is '<DescriptorType.UNKNOWN: 0>'
    _member_map_ = {
        'CMD': None, # (!) real value is '<DescriptorType.CMD: 2>'
        'PATH': None, # (!) real value is '<DescriptorType.PATH: 1>'
        'UNKNOWN': None, # (!) real value is '<DescriptorType.UNKNOWN: 0>'
    }
    _member_names_ = [
        'UNKNOWN',
        'PATH',
        'CMD',
    ]
    _member_type_ = object
    _value2member_map_ = {
        0: None, # (!) real value is '<DescriptorType.UNKNOWN: 0>'
        1: None, # (!) real value is '<DescriptorType.PATH: 1>'
        2: None, # (!) real value is '<DescriptorType.CMD: 2>'
    }


