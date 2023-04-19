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

class _RecordBatchFileReader(_Weakrefable):
    # no doc
    def get_batch(self, int_i): # real signature unknown; restored from __doc__
        """
        _RecordBatchFileReader.get_batch(self, int i)
        
                Read the record batch with the given index.
        
                Parameters
                ----------
                i : int
                    The index of the record batch in the IPC file.
        
                Returns
                -------
                batch : RecordBatch
        """
        pass

    def get_batch_with_custom_metadata(self, int_i): # real signature unknown; restored from __doc__
        """
        _RecordBatchFileReader.get_batch_with_custom_metadata(self, int i)
        
                Read the record batch with the given index along with 
                its custom metadata
        
                Parameters
                ----------
                i : int
                    The index of the record batch in the IPC file.
        
                Returns
                -------
                batch : RecordBatch
                custom_metadata : KeyValueMetadata
        """
        pass

    def get_record_batch(self, *args, **kwargs): # real signature unknown
        """
        _RecordBatchFileReader.get_batch(self, int i)
        
                Read the record batch with the given index.
        
                Parameters
                ----------
                i : int
                    The index of the record batch in the IPC file.
        
                Returns
                -------
                batch : RecordBatch
        """
        pass

    def read_all(self): # real signature unknown; restored from __doc__
        """
        _RecordBatchFileReader.read_all(self)
        
                Read all record batches as a pyarrow.Table
        """
        pass

    def read_pandas(self, **options): # real signature unknown; restored from __doc__
        """
        _ReadPandasMixin.read_pandas(self, **options)
        
                Read contents of stream to a pandas.DataFrame.
        
                Read all record batches as a pyarrow.Table then convert it to a
                pandas.DataFrame using Table.to_pandas.
        
                Parameters
                ----------
                **options
                    Arguments to forward to :meth:`Table.to_pandas`.
        
                Returns
                -------
                df : pandas.DataFrame
        """
        pass

    def _open(self, source, footer_offset=None, IpcReadOptions_options=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ _RecordBatchFileReader._open(self, source, footer_offset=None, IpcReadOptions options=IpcReadOptions(), MemoryPool memory_pool=None) """
        pass

    def __enter__(self): # real signature unknown; restored from __doc__
        """ _RecordBatchFileReader.__enter__(self) """
        pass

    def __exit__(self, exc_type, exc_value, traceback): # real signature unknown; restored from __doc__
        """ _RecordBatchFileReader.__exit__(self, exc_type, exc_value, traceback) """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ _RecordBatchFileReader.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ _RecordBatchFileReader.__setstate_cython__(self, __pyx_state) """
        pass

    num_record_batches = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        The number of record batches in the IPC file.
        """

    schema = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    stats = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Current IPC read statistics.
        """



