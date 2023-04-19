# encoding: utf-8
# module pyarrow._dataset
# from C:\Users\akharin\PycharmProjects\pythonProject\venv\lib\site-packages\pyarrow\_dataset.cp39-win_amd64.pyd
# by generator 1.147
""" Dataset is currently unstable. APIs subject to change without notice. """

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import codecs as codecs # C:\Users\akharin\AppData\Local\Programs\Python\Python39\lib\codecs.py
import collections as collections # C:\Users\akharin\AppData\Local\Programs\Python\Python39\lib\collections\__init__.py
import os as os # C:\Users\akharin\AppData\Local\Programs\Python\Python39\lib\os.py
import warnings as warnings # C:\Users\akharin\AppData\Local\Programs\Python\Python39\lib\warnings.py
import pyarrow as pa # C:\Users\akharin\PycharmProjects\pythonProject\venv\lib\site-packages\pyarrow\__init__.py
from pyarrow.lib import ArrowTypeError, _pc, frombytes, tobytes

import importlib._bootstrap as __importlib__bootstrap
import pyarrow.lib as __pyarrow_lib


class WrittenFile(__pyarrow_lib._Weakrefable):
    """
    WrittenFile(path, metadata, size)
    
        Metadata information about files written as
        part of a dataset write operation
    
        Parameters
        ----------
        path : str
            Path to the file.
        metadata : pyarrow.parquet.FileMetaData, optional
            For Parquet files, the Parquet file metadata.
        size : int
            The size of the file in bytes.
    """
    def __init__(self, path, metadata, size): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ WrittenFile.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ WrittenFile.__setstate_cython__(self, __pyx_state) """
        pass

    metadata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """metadata: object"""

    path = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """path: unicode"""

    size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """size: 'int64_t'"""



