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


from .DatasetFactory import DatasetFactory

class FileSystemDatasetFactory(DatasetFactory):
    """
    FileSystemDatasetFactory(FileSystem filesystem, paths_or_selector, FileFormat format, FileSystemFactoryOptions options=None)
    
        Create a DatasetFactory from a list of paths with schema inspection.
    
        Parameters
        ----------
        filesystem : pyarrow.fs.FileSystem
            Filesystem to discover.
        paths_or_selector : pyarrow.fs.FileSelector or list of path-likes
            Either a Selector object or a list of path-like objects.
        format : FileFormat
            Currently only ParquetFileFormat and IpcFileFormat are supported.
        options : FileSystemFactoryOptions, optional
            Various flags influencing the discovery of filesystem paths.
    """
    def __init__(self, FileSystem_filesystem, paths_or_selector, FileFormat_format, FileSystemFactoryOptions_options=None): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ FileSystemDatasetFactory.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ FileSystemDatasetFactory.__setstate_cython__(self, __pyx_state) """
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x00000187AB21EC60>'


