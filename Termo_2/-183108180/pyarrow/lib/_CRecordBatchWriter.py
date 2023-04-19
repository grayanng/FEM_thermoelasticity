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

class _CRecordBatchWriter(_Weakrefable):
    """
    The base RecordBatchWriter wrapper.
    
        Provides common implementations of convenience methods. Should not
        be instantiated directly by user code.
    """
    def close(self): # real signature unknown; restored from __doc__
        """
        _CRecordBatchWriter.close(self)
        
                Close stream and write end-of-stream 0 marker.
        """
        pass

    def write(self, table_or_batch): # real signature unknown; restored from __doc__
        """
        _CRecordBatchWriter.write(self, table_or_batch)
        
                Write RecordBatch or Table to stream.
        
                Parameters
                ----------
                table_or_batch : {RecordBatch, Table}
        """
        pass

    def write_batch(self, RecordBatch_batch, custom_metadata=None): # real signature unknown; restored from __doc__
        """
        _CRecordBatchWriter.write_batch(self, RecordBatch batch, custom_metadata=None)
        
                Write RecordBatch to stream.
        
                Parameters
                ----------
                batch : RecordBatch
                custom_metadata : mapping or KeyValueMetadata
                    Keys and values must be string-like / coercible to bytes
        """
        pass

    def write_table(self, Table_table, max_chunksize=None): # real signature unknown; restored from __doc__
        """
        _CRecordBatchWriter.write_table(self, Table table, max_chunksize=None)
        
                Write Table to stream in (contiguous) RecordBatch objects.
        
                Parameters
                ----------
                table : Table
                max_chunksize : int, default None
                    Maximum size for RecordBatch chunks. Individual chunks may be
                    smaller depending on the chunk layout of individual columns.
        """
        pass

    def __enter__(self): # real signature unknown; restored from __doc__
        """ _CRecordBatchWriter.__enter__(self) """
        pass

    def __exit__(self, exc_type, exc_val, exc_tb): # real signature unknown; restored from __doc__
        """ _CRecordBatchWriter.__exit__(self, exc_type, exc_val, exc_tb) """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ _CRecordBatchWriter.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ _CRecordBatchWriter.__setstate_cython__(self, __pyx_state) """
        pass

    stats = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Current IPC write statistics.
        """



