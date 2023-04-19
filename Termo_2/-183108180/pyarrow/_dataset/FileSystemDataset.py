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


from .Dataset import Dataset

class FileSystemDataset(Dataset):
    """
    FileSystemDataset(fragments, Schema schema, FileFormat format, FileSystem filesystem=None, root_partition=None)
    
        A Dataset of file fragments.
    
        A FileSystemDataset is composed of one or more FileFragment.
    
        Parameters
        ----------
        fragments : list[Fragments]
            List of fragments to consume.
        schema : Schema
            The top-level schema of the Dataset.
        format : FileFormat
            File format of the fragments, currently only ParquetFileFormat,
            IpcFileFormat, and CsvFileFormat are supported.
        filesystem : FileSystem
            FileSystem of the fragments.
        root_partition : Expression, optional
            The top-level partition of the DataDataset.
    """
    @classmethod
    def from_paths(cls, type_cls, paths, schema=None, format=None, filesystem=None, partitions=None, root_partition=None): # real signature unknown; restored from __doc__
        """
        FileSystemDataset.from_paths(type cls, paths, schema=None, format=None, filesystem=None, partitions=None, root_partition=None)
        A Dataset created from a list of paths on a particular filesystem.
        
                Parameters
                ----------
                paths : list of str
                    List of file paths to create the fragments from.
                schema : Schema
                    The top-level schema of the DataDataset.
                format : FileFormat
                    File format to create fragments from, currently only
                    ParquetFileFormat, IpcFileFormat, and CsvFileFormat are supported.
                filesystem : FileSystem
                    The filesystem which files are from.
                partitions : list[Expression], optional
                    Attach additional partition information for the file paths.
                root_partition : Expression, optional
                    The top-level partition of the DataDataset.
        """
        pass

    def __init__(self, fragments, Schema_schema, FileFormat_format, FileSystem_filesystem=None, root_partition=None): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self): # real signature unknown; restored from __doc__
        """ FileSystemDataset.__reduce__(self) """
        pass

    files = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """List of the files"""

    filesystem = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    format = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The FileFormat of this source."""

    partitioning = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        The partitioning of the Dataset source, if discovered.

        If the FileSystemDataset is created using the ``dataset()`` factory
        function with a partitioning specified, this will return the
        finalized Partitioning object from the dataset discovery. In all
        other cases, this returns None.
        """


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x00000187AB21E7E0>'


