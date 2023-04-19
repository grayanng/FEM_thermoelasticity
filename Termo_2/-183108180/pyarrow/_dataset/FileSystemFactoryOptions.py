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


class FileSystemFactoryOptions(__pyarrow_lib._Weakrefable):
    """
    FileSystemFactoryOptions(partition_base_dir=None, partitioning=None, exclude_invalid_files=None, list selector_ignore_prefixes=None)
    
        Influences the discovery of filesystem paths.
    
        Parameters
        ----------
        partition_base_dir : str, optional
            For the purposes of applying the partitioning, paths will be
            stripped of the partition_base_dir. Files not matching the
            partition_base_dir prefix will be skipped for partitioning discovery.
            The ignored files will still be part of the Dataset, but will not
            have partition information.
        partitioning : Partitioning/PartitioningFactory, optional
           Apply the Partitioning to every discovered Fragment. See Partitioning or
           PartitioningFactory documentation.
        exclude_invalid_files : bool, optional (default True)
            If True, invalid files will be excluded (file format specific check).
            This will incur IO for each files in a serial and single threaded
            fashion. Disabling this feature will skip the IO, but unsupported
            files may be present in the Dataset (resulting in an error at scan
            time).
        selector_ignore_prefixes : list, optional
            When discovering from a Selector (and not from an explicit file list),
            ignore files and directories matching any of these prefixes.
            By default this is ['.', '_'].
    """
    def __init__(self, partition_base_dir=None, partitioning=None, exclude_invalid_files=None, list_selector_ignore_prefixes=None): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ FileSystemFactoryOptions.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ FileSystemFactoryOptions.__setstate_cython__(self, __pyx_state) """
        pass

    exclude_invalid_files = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Whether to exclude invalid files."""

    partitioning = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Partitioning to apply to discovered files.

        NOTE: setting this property will overwrite partitioning_factory.
        """

    partitioning_factory = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PartitioningFactory to apply to discovered files and
        discover a Partitioning.

        NOTE: setting this property will overwrite partitioning.
        """

    partition_base_dir = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Base directory to strip paths before applying the partitioning.
        """

    selector_ignore_prefixes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        List of prefixes. Files matching one of those prefixes will be
        ignored by the discovery process.
        """


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x00000187AB21EC00>'
    __slots__ = ()


