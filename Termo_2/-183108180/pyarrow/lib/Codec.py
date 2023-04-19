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

class Codec(_Weakrefable):
    """
    Codec(unicode compression, compression_level=None)
    
        Compression codec.
    
        Parameters
        ----------
        compression : str
            Type of compression codec to initialize, valid values are: 'gzip',
            'bz2', 'brotli', 'lz4' (or 'lz4_frame'), 'lz4_raw', 'zstd' and
            'snappy'.
        compression_level : int, None
            Optional parameter specifying how aggressively to compress.  The
            possible ranges and effect of this parameter depend on the specific
            codec chosen.  Higher values compress more but typically use more
            resources (CPU/RAM).  Some codecs support negative values.
    
            gzip
                The compression_level maps to the memlevel parameter of
                deflateInit2.  Higher levels use more RAM but are faster
                and should have higher compression ratios.
    
            bz2
                The compression level maps to the blockSize100k parameter of
                the BZ2_bzCompressInit function.  Higher levels use more RAM
                but are faster and should have higher compression ratios.
    
            brotli
                The compression level maps to the BROTLI_PARAM_QUALITY
                parameter.  Higher values are slower and should have higher
                compression ratios.
    
            lz4/lz4_frame/lz4_raw
                The compression level parameter is not supported and must
                be None
    
            zstd
                The compression level maps to the compressionLevel parameter
                of ZSTD_initCStream.  Negative values are supported.  Higher
                values are slower and should have higher compression ratios.
    
            snappy
                The compression level parameter is not supported and must
                be None
    
    
        Raises
        ------
        ValueError
            If invalid compression value is passed.
    
        Examples
        --------
        >>> import pyarrow as pa
        >>> pa.Codec.is_available('gzip')
        True
        >>> codec = pa.Codec('gzip')
        >>> codec.name
        'gzip'
        >>> codec.compression_level
        9
    """
    def compress(self, buf, asbytes=False, memory_pool=None): # real signature unknown; restored from __doc__
        """
        Codec.compress(self, buf, asbytes=False, memory_pool=None)
        
                Compress data from buffer-like object.
        
                Parameters
                ----------
                buf : pyarrow.Buffer, bytes, or other object supporting buffer protocol
                asbytes : bool, default False
                    Return result as Python bytes object, otherwise Buffer
                memory_pool : MemoryPool, default None
                    Memory pool to use for buffer allocations, if any
        
                Returns
                -------
                compressed : pyarrow.Buffer or bytes (if asbytes=True)
        """
        pass

    def decompress(self, buf, decompressed_size=None, asbytes=False, memory_pool=None): # real signature unknown; restored from __doc__
        """
        Codec.decompress(self, buf, decompressed_size=None, asbytes=False, memory_pool=None)
        
                Decompress data from buffer-like object.
        
                Parameters
                ----------
                buf : pyarrow.Buffer, bytes, or memoryview-compatible object
                decompressed_size : int, default None
                    Size of the decompressed result
                asbytes : boolean, default False
                    Return result as Python bytes object, otherwise Buffer
                memory_pool : MemoryPool, default None
                    Memory pool to use for buffer allocations, if any.
        
                Returns
                -------
                uncompressed : pyarrow.Buffer or bytes (if asbytes=True)
        """
        pass

    def default_compression_level(self, unicode_compression): # real signature unknown; restored from __doc__
        """
        Codec.default_compression_level(unicode compression)
        
                Returns the compression level that Arrow will use for the codec if
                None is specified.
        
                Parameters
                ----------
                compression : str
                    Type of compression codec,
                    refer to Codec docstring for a list of supported ones.
        """
        pass

    def detect(self, path): # real signature unknown; restored from __doc__
        """
        Codec.detect(path)
        
                Detect and instantiate compression codec based on file extension.
        
                Parameters
                ----------
                path : str, path-like
                    File-path to detect compression from.
        
                Raises
                ------
                TypeError
                    If the passed value is not path-like.
                ValueError
                    If the compression can't be detected from the path.
        
                Returns
                -------
                Codec
        """
        pass

    def is_available(self, unicode_compression): # real signature unknown; restored from __doc__
        """
        Codec.is_available(unicode compression)
        
                Returns whether the compression support has been built and enabled.
        
                Parameters
                ----------
                compression : str
                     Type of compression codec,
                     refer to Codec docstring for a list of supported ones.
        
                Returns
                -------
                bool
        """
        pass

    def maximum_compression_level(self, unicode_compression): # real signature unknown; restored from __doc__
        """
        Codec.maximum_compression_level(unicode compression)
        
                Returns the largest valid value for the compression level
        
                Parameters
                ----------
                compression : str
                    Type of compression codec,
                    refer to Codec docstring for a list of supported ones.
        """
        pass

    def minimum_compression_level(self, unicode_compression): # real signature unknown; restored from __doc__
        """
        Codec.minimum_compression_level(unicode compression)
        
                Returns the smallest valid value for the compression level
        
                Parameters
                ----------
                compression : str
                    Type of compression codec,
                    refer to Codec docstring for a list of supported ones.
        """
        pass

    def supports_compression_level(self, unicode_compression): # real signature unknown; restored from __doc__
        """
        Codec.supports_compression_level(unicode compression)
        
                Returns true if the compression level parameter is supported
                for the given codec.
        
                Parameters
                ----------
                compression : str
                    Type of compression codec,
                    refer to Codec docstring for a list of supported ones.
        """
        pass

    def __init__(self, unicode_compression, compression_level=None): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ Codec.__reduce_cython__(self) """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ Codec.__setstate_cython__(self, __pyx_state) """
        pass

    compression_level = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the compression level parameter of the codec"""

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the name of the codec"""


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001970BCC5480>'


