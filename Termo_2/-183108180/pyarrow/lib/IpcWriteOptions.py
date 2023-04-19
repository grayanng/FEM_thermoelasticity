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

class IpcWriteOptions(_Weakrefable):
    """
    IpcWriteOptions(metadata_version=MetadataVersion.V5, *, bool allow_64bit=False, use_legacy_format=False, compression=None, bool use_threads=True, bool emit_dictionary_deltas=False, bool unify_dictionaries=False)
    
        Serialization options for the IPC format.
    
        Parameters
        ----------
        metadata_version : MetadataVersion, default MetadataVersion.V5
            The metadata version to write.  V5 is the current and latest,
            V4 is the pre-1.0 metadata version (with incompatible Union layout).
        allow_64bit : bool, default False
            If true, allow field lengths that don't fit in a signed 32-bit int.
        use_legacy_format : bool, default False
            Whether to use the pre-Arrow 0.15 IPC format.
        compression : str, Codec, or None
            compression codec to use for record batch buffers.
            If None then batch buffers will be uncompressed.
            Must be "lz4", "zstd" or None.
            To specify a compression_level use `pyarrow.Codec`
        use_threads : bool
            Whether to use the global CPU thread pool to parallelize any
            computational tasks like compression.
        emit_dictionary_deltas : bool
            Whether to emit dictionary deltas.  Default is false for maximum
            stream compatibility.
        unify_dictionaries : bool
            If true then calls to write_table will attempt to unify dictionaries
            across all batches in the table.  This can help avoid the need for
            replacement dictionaries (which the file format does not support)
            but requires computing the unified dictionary and then remapping
            the indices arrays.
    
            This parameter is ignored when writing to the IPC stream format as
            the IPC stream format can support replacement dictionaries.
    """
    def __init__(self, metadata_version=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ IpcWriteOptions.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ IpcWriteOptions.__setstate_cython__(self, __pyx_state) """
        pass

    allow_64bit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    compression = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    emit_dictionary_deltas = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    metadata_version = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    unify_dictionaries = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    use_legacy_format = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    use_threads = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __slots__ = ()


