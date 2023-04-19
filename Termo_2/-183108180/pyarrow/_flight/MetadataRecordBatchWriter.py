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


class MetadataRecordBatchWriter(__pyarrow_lib._CRecordBatchWriter):
    """
    A RecordBatchWriter that also allows writing application metadata.
    
        This class is a context manager; on exit, close() will be called.
    """
    def begin(self, Schema_schema, options=None): # real signature unknown; restored from __doc__
        """
        MetadataRecordBatchWriter.begin(self, Schema schema: Schema, options=None)
        Prepare to write data to this stream with the given schema.
        """
        pass

    def close(self): # real signature unknown; restored from __doc__
        """
        MetadataRecordBatchWriter.close(self)
        
                Close stream and write end-of-stream 0 marker.
        """
        pass

    def write_batch(self, RecordBatch_batch): # real signature unknown; restored from __doc__
        """
        MetadataRecordBatchWriter.write_batch(self, RecordBatch batch)
        
                Write RecordBatch to stream.
        
                Parameters
                ----------
                batch : RecordBatch
        """
        pass

    def write_metadata(self, buf): # real signature unknown; restored from __doc__
        """
        MetadataRecordBatchWriter.write_metadata(self, buf)
        Write Flight metadata by itself.
        """
        pass

    def write_table(self, Table_table, max_chunksize=None, **kwargs): # real signature unknown; restored from __doc__
        """
        MetadataRecordBatchWriter.write_table(self, Table table, max_chunksize=None, **kwargs)
        
                Write Table to stream in (contiguous) RecordBatch objects.
        
                Parameters
                ----------
                table : Table
                max_chunksize : int, default None
                    Maximum size for RecordBatch chunks. Individual chunks may be
                    smaller depending on the chunk layout of individual columns.
        """
        pass

    def write_with_metadata(self, RecordBatch_batch, buf): # real signature unknown; restored from __doc__
        """
        MetadataRecordBatchWriter.write_with_metadata(self, RecordBatch batch, buf)
        Write a RecordBatch along with Flight metadata.
        
                Parameters
                ----------
                batch : RecordBatch
                    The next RecordBatch in the stream.
                buf : Buffer
                    Application-specific metadata for the batch as defined by
                    Flight.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ MetadataRecordBatchWriter.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ MetadataRecordBatchWriter.__setstate_cython__(self, __pyx_state) """
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000002441812E930>'


