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


class _MetadataRecordBatchReader(__pyarrow_lib._Weakrefable, __pyarrow_lib._ReadPandasMixin):
    """ A reader for Flight streams. """
    def read_all(self): # real signature unknown; restored from __doc__
        """
        _MetadataRecordBatchReader.read_all(self)
        Read the entire contents of the stream as a Table.
        """
        pass

    def read_chunk(self): # real signature unknown; restored from __doc__
        """
        _MetadataRecordBatchReader.read_chunk(self)
        Read the next RecordBatch along with any metadata.
        
                Returns
                -------
                data : RecordBatch
                    The next RecordBatch in the stream.
                app_metadata : Buffer or None
                    Application-specific metadata for the batch as defined by
                    Flight.
        
                Raises
                ------
                StopIteration
                    when the stream is finished
        """
        pass

    def to_reader(self): # real signature unknown; restored from __doc__
        """
        _MetadataRecordBatchReader.to_reader(self)
        Convert this reader into a regular RecordBatchReader.
        
                This may fail if the schema cannot be read from the remote end.
        
                Returns
                -------
                RecordBatchReader
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __iter__(self, *args, **kwargs): # real signature unknown
        """ Implement iter(self). """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ _MetadataRecordBatchReader.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ _MetadataRecordBatchReader.__setstate_cython__(self, __pyx_state) """
        pass

    schema = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get the schema for this reader."""


    __dict__ = None # (!) real value is "mappingproxy({'__iter__': <slot wrapper '__iter__' of 'pyarrow._flight._MetadataRecordBatchReader' objects>, '__new__': <built-in method __new__ of type object at 0x00007FFC337AE3E0>, 'read_all': <method 'read_all' of 'pyarrow._flight._MetadataRecordBatchReader' objects>, 'read_chunk': <method 'read_chunk' of 'pyarrow._flight._MetadataRecordBatchReader' objects>, 'to_reader': <method 'to_reader' of 'pyarrow._flight._MetadataRecordBatchReader' objects>, 'schema': <attribute 'schema' of 'pyarrow._flight._MetadataRecordBatchReader' objects>, '__dict__': <attribute '__dict__' of 'pyarrow._flight._MetadataRecordBatchReader' objects>, '__doc__': 'A reader for Flight streams.', '__reduce__': <method '__reduce_cython__' of 'pyarrow._flight._MetadataRecordBatchReader' objects>, '__setstate__': <method '__setstate_cython__' of 'pyarrow._flight._MetadataRecordBatchReader' objects>})"


