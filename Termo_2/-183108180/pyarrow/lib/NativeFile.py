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

class NativeFile(_Weakrefable):
    """
    The base class for all Arrow streams.
    
        Streams are either readable, writable, or both.
        They optionally support seeking.
    
        While this class exposes methods to read or write data from Python, the
        primary intent of using a Arrow stream is to pass it to other Arrow
        facilities that will make use of it, such as Arrow IPC routines.
    
        Be aware that there are subtle differences with regular Python files,
        e.g. destroying a writable Arrow stream without closing it explicitly
        will not flush any pending data.
    """
    def close(self): # real signature unknown; restored from __doc__
        """ NativeFile.close(self) """
        pass

    def download(self, stream_or_path, buffer_size=None): # real signature unknown; restored from __doc__
        """
        NativeFile.download(self, stream_or_path, buffer_size=None)
        
                Read this file completely to a local path or destination stream.
        
                This method first seeks to the beginning of the file.
        
                Parameters
                ----------
                stream_or_path : str or file-like object
                    If a string, a local file path to write to; otherwise,
                    should be a writable stream.
                buffer_size : int, optional
                    The buffer size to use for data transfers.
        """
        pass

    def fileno(self): # real signature unknown; restored from __doc__
        """
        NativeFile.fileno(self)
        
                NOT IMPLEMENTED
        """
        pass

    def flush(self): # real signature unknown; restored from __doc__
        """
        NativeFile.flush(self)
        
                Flush the stream, if applicable.
        
                An error is raised if stream is not writable.
        """
        pass

    def get_stream(self, file_offset, nbytes): # real signature unknown; restored from __doc__
        """
        NativeFile.get_stream(self, file_offset, nbytes)
        
                Return an input stream that reads a file segment independent of the
                state of the file.
        
                Allows reading portions of a random access file as an input stream
                without interfering with each other.
        
                Parameters
                ----------
                file_offset : int
                nbytes : int
        
                Returns
                -------
                stream : NativeFile
        """
        pass

    def isatty(self): # real signature unknown; restored from __doc__
        """ NativeFile.isatty(self) """
        pass

    def metadata(self): # real signature unknown; restored from __doc__
        """
        NativeFile.metadata(self)
        
                Return file metadata
        """
        pass

    def read(self, nbytes=None): # real signature unknown; restored from __doc__
        """
        NativeFile.read(self, nbytes=None)
        
                Read and return up to n bytes.
        
                If *nbytes* is None, then the entire remaining file contents are read.
        
                Parameters
                ----------
                nbytes : int, default None
        
                Returns
                -------
                data : bytes
        """
        pass

    def read1(self, nbytes=None): # real signature unknown; restored from __doc__
        """
        NativeFile.read1(self, nbytes=None)
        Read and return up to n bytes.
        
                Unlike read(), if *nbytes* is None then a chunk is read, not the
                entire file.
        
                Parameters
                ----------
                nbytes : int, default None
                    The maximum number of bytes to read.
        
                Returns
                -------
                data : bytes
        """
        pass

    def readable(self): # real signature unknown; restored from __doc__
        """ NativeFile.readable(self) """
        pass

    def readall(self): # real signature unknown; restored from __doc__
        """ NativeFile.readall(self) """
        pass

    def readinto(self, b): # real signature unknown; restored from __doc__
        """
        NativeFile.readinto(self, b)
        
                Read into the supplied buffer
        
                Parameters
                ----------
                b : buffer-like object
                    A writable buffer object (such as a bytearray).
        
                Returns
                -------
                written : int
                    number of bytes written
        """
        pass

    def readline(self, size=None): # real signature unknown; restored from __doc__
        """
        NativeFile.readline(self, size=None)
        NOT IMPLEMENTED. Read and return a line of bytes from the file.
        
                If size is specified, read at most size bytes.
        
                Line terminator is always b"\n".
        
                Parameters
                ----------
                size : int
                    maximum number of bytes read
        """
        pass

    def readlines(self, hint=None): # real signature unknown; restored from __doc__
        """
        NativeFile.readlines(self, hint=None)
        NOT IMPLEMENTED. Read lines of the file
        
                Parameters
                ----------
                hint : int
                    maximum number of bytes read until we stop
        """
        pass

    def read_at(self, nbytes, offset): # real signature unknown; restored from __doc__
        """
        NativeFile.read_at(self, nbytes, offset)
        
                Read indicated number of bytes at offset from the file
        
                Parameters
                ----------
                nbytes : int
                offset : int
        
                Returns
                -------
                data : bytes
        """
        pass

    def read_buffer(self, nbytes=None): # real signature unknown; restored from __doc__
        """ NativeFile.read_buffer(self, nbytes=None) """
        pass

    def seek(self, int64_t_position, int_whence=0): # real signature unknown; restored from __doc__
        """
        NativeFile.seek(self, int64_t position, int whence=0)
        
                Change current file stream position
        
                Parameters
                ----------
                position : int
                    Byte offset, interpreted relative to value of whence argument
                whence : int, default 0
                    Point of reference for seek offset
        
                Notes
                -----
                Values of whence:
                * 0 -- start of stream (the default); offset should be zero or positive
                * 1 -- current stream position; offset may be negative
                * 2 -- end of stream; offset is usually negative
        
                Returns
                -------
                int
                    The new absolute stream position.
        """
        pass

    def seekable(self): # real signature unknown; restored from __doc__
        """ NativeFile.seekable(self) """
        pass

    def size(self): # real signature unknown; restored from __doc__
        """
        NativeFile.size(self)
        
                Return file size
        """
        pass

    def tell(self): # real signature unknown; restored from __doc__
        """
        NativeFile.tell(self)
        
                Return current stream position
        """
        pass

    def truncate(self): # real signature unknown; restored from __doc__
        """
        NativeFile.truncate(self)
        
                NOT IMPLEMENTED
        """
        pass

    def upload(self, stream, buffer_size=None): # real signature unknown; restored from __doc__
        """
        NativeFile.upload(self, stream, buffer_size=None)
        
                Write from a source stream to this file.
        
                Parameters
                ----------
                stream : file-like object
                    Source stream to pipe to this file.
                buffer_size : int, optional
                    The buffer size to use for data transfers.
        """
        pass

    def writable(self): # real signature unknown; restored from __doc__
        """ NativeFile.writable(self) """
        pass

    def write(self, data): # real signature unknown; restored from __doc__
        """
        NativeFile.write(self, data)
        
                Write data to the file.
        
                Parameters
                ----------
                data : bytes-like object or exporter of buffer protocol
        
                Returns
                -------
                int
                    nbytes: number of bytes written
        """
        pass

    def writelines(self, lines): # real signature unknown; restored from __doc__
        """ NativeFile.writelines(self, lines) """
        pass

    def _assert_open(self): # real signature unknown; restored from __doc__
        """ NativeFile._assert_open(self) """
        pass

    def _assert_readable(self): # real signature unknown; restored from __doc__
        """ NativeFile._assert_readable(self) """
        pass

    def _assert_seekable(self): # real signature unknown; restored from __doc__
        """ NativeFile._assert_seekable(self) """
        pass

    def _assert_writable(self): # real signature unknown; restored from __doc__
        """ NativeFile._assert_writable(self) """
        pass

    def __enter__(self): # real signature unknown; restored from __doc__
        """ NativeFile.__enter__(self) """
        pass

    def __exit__(self, exc_type, exc_value, tb): # real signature unknown; restored from __doc__
        """ NativeFile.__exit__(self, exc_type, exc_value, tb) """
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

    def __next__(self, *args, **kwargs): # real signature unknown
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ NativeFile.__reduce_cython__(self) """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ NativeFile.__setstate_cython__(self, __pyx_state) """
        pass

    closed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    mode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        The file mode. Currently instances of NativeFile may support:

        * rb: binary read
        * wb: binary write
        * rb+: binary read and write
        """


    _default_chunk_size = 262144
    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001970BCC56C0>'


