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


class Fragment(__pyarrow_lib._Weakrefable):
    """
    Fragment()
    Fragment of data from a Dataset.
    """
    def count_rows(self, **kwargs): # real signature unknown; restored from __doc__
        """
        Fragment.count_rows(self, **kwargs)
        
                Count rows matching the scanner filter.
        
                Parameters
                ----------
                **kwargs : dict, optional
                    Arguments for `Scanner.from_fragment`.
        
                Returns
                -------
                count : int
        """
        pass

    def head(self, int_num_rows, **kwargs): # real signature unknown; restored from __doc__
        """
        Fragment.head(self, int num_rows, **kwargs)
        
                Load the first N rows of the fragment.
        
                Parameters
                ----------
                num_rows : int
                    The number of rows to load.
                **kwargs : dict, optional
                    Arguments for `Scanner.from_fragment`.
        
                Returns
                -------
                Table
        """
        pass

    def scanner(self, Schema_schema=None, **kwargs): # real signature unknown; restored from __doc__
        """
        Fragment.scanner(self, Schema schema=None, **kwargs)
        
                Build a scan operation against the fragment.
        
                Data is not loaded immediately. Instead, this produces a Scanner,
                which exposes further operations (e.g. loading all data as a
                table, counting rows).
        
                Parameters
                ----------
                schema : Schema
                    Schema to use for scanning. This is used to unify a Fragment to
                    it's Dataset's schema. If not specified this will use the
                    Fragment's physical schema which might differ for each Fragment.
                **kwargs : dict, optional
                    Arguments for `Scanner.from_fragment`.
        
                Returns
                -------
                scanner : Scanner
        """
        pass

    def take(self, indices, **kwargs): # real signature unknown; restored from __doc__
        """
        Fragment.take(self, indices, **kwargs)
        
                Select rows of data by index.
        
                Parameters
                ----------
                indices : Array or array-like
                    The indices of row to select in the dataset.
                **kwargs : dict, optional
                    Arguments for `Scanner.from_fragment`.
        
                Returns
                -------
                Table
        """
        pass

    def to_batches(self, Schema_schema=None, **kwargs): # real signature unknown; restored from __doc__
        """
        Fragment.to_batches(self, Schema schema=None, **kwargs)
        
                Read the fragment as materialized record batches.
        
                Parameters
                ----------
                schema : Schema, optional
                    Concrete schema to use for scanning.
                **kwargs : dict, optional
                    Arguments for `Scanner.from_fragment`.
        
                Returns
                -------
                record_batches : iterator of RecordBatch
        """
        pass

    def to_table(self, Schema_schema=None, **kwargs): # real signature unknown; restored from __doc__
        """
        Fragment.to_table(self, Schema schema=None, **kwargs)
        
                Convert this Fragment into a Table.
        
                Use this convenience utility with care. This will serially materialize
                the Scan result in memory before creating the Table.
        
                Parameters
                ----------
                schema : Schema, optional
                    Concrete schema to use for scanning.
                **kwargs : dict, optional
                    Arguments for `Scanner.from_fragment`.
        
                Returns
                -------
                table : Table
        """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ Fragment.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ Fragment.__setstate_cython__(self, __pyx_state) """
        pass

    partition_expression = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """An Expression which evaluates to true for all data viewed by this
        Fragment.
        """

    physical_schema = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Return the physical schema of this Fragment. This schema can be
        different from the dataset read schema."""


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x00000187AB21E570>'


