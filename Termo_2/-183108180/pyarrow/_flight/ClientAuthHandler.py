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


class ClientAuthHandler(__pyarrow_lib._Weakrefable):
    """ Authentication plugin for a client. """
    def authenticate(self, outgoing, incoming): # real signature unknown; restored from __doc__
        """
        ClientAuthHandler.authenticate(self, outgoing, incoming)
        Conduct the handshake with the server.
        
                Parameters
                ----------
                outgoing : ClientAuthSender
                    A channel to send messages to the server.
                incoming : ClientAuthReader
                    A channel to read messages from the server.
        """
        pass

    def get_token(self): # real signature unknown; restored from __doc__
        """
        ClientAuthHandler.get_token(self)
        Get the auth token for a call.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ ClientAuthHandler.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ ClientAuthHandler.__setstate_cython__(self, __pyx_state) """
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000002441812EE10>'


