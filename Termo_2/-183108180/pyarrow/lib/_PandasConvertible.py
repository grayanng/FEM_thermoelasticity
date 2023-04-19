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

class _PandasConvertible(_Weakrefable):
    # no doc
    def to_pandas(self, memory_pool=None, categories=None, bool_strings_to_categorical=False, bool_zero_copy_only=False, bool_integer_object_nulls=False, bool_date_as_object=True, bool_timestamp_as_object=False, bool_use_threads=True, bool_deduplicate_objects=True, bool_ignore_metadata=False, bool_safe=True, bool_split_blocks=False, bool_self_destruct=False, types_mapper=None): # real signature unknown; restored from __doc__
        """
        _PandasConvertible.to_pandas(self, memory_pool=None, categories=None, bool strings_to_categorical=False, bool zero_copy_only=False, bool integer_object_nulls=False, bool date_as_object=True, bool timestamp_as_object=False, bool use_threads=True, bool deduplicate_objects=True, bool ignore_metadata=False, bool safe=True, bool split_blocks=False, bool self_destruct=False, types_mapper=None)
        
                Convert to a pandas-compatible NumPy array or DataFrame, as appropriate
        
                Parameters
                ----------
                memory_pool : MemoryPool, default None
                    Arrow MemoryPool to use for allocations. Uses the default memory
                    pool is not passed.
                categories : list, default empty
                    List of fields that should be returned as pandas.Categorical. Only
                    applies to table-like data structures.
                strings_to_categorical : bool, default False
                    Encode string (UTF8) and binary types to pandas.Categorical.
                zero_copy_only : bool, default False
                    Raise an ArrowException if this function call would require copying
                    the underlying data.
                integer_object_nulls : bool, default False
                    Cast integers with nulls to objects
                date_as_object : bool, default True
                    Cast dates to objects. If False, convert to datetime64[ns] dtype.
                timestamp_as_object : bool, default False
                    Cast non-nanosecond timestamps (np.datetime64) to objects. This is
                    useful if you have timestamps that don't fit in the normal date
                    range of nanosecond timestamps (1678 CE-2262 CE).
                    If False, all timestamps are converted to datetime64[ns] dtype.
                use_threads : bool, default True
                    Whether to parallelize the conversion using multiple threads.
                deduplicate_objects : bool, default False
                    Do not create multiple copies Python objects when created, to save
                    on memory use. Conversion will be slower.
                ignore_metadata : bool, default False
                    If True, do not use the 'pandas' metadata to reconstruct the
                    DataFrame index, if present
                safe : bool, default True
                    For certain data types, a cast is needed in order to store the
                    data in a pandas DataFrame or Series (e.g. timestamps are always
                    stored as nanoseconds in pandas). This option controls whether it
                    is a safe cast or not.
                split_blocks : bool, default False
                    If True, generate one internal "block" for each column when
                    creating a pandas.DataFrame from a RecordBatch or Table. While this
                    can temporarily reduce memory note that various pandas operations
                    can trigger "consolidation" which may balloon memory use.
                self_destruct : bool, default False
                    EXPERIMENTAL: If True, attempt to deallocate the originating Arrow
                    memory while converting the Arrow object to pandas. If you use the
                    object after calling to_pandas with this option it will crash your
                    program.
        
                    Note that you may not see always memory usage improvements. For
                    example, if multiple columns share an underlying allocation,
                    memory can't be freed until all columns are converted.
                types_mapper : function, default None
                    A function mapping a pyarrow DataType to a pandas ExtensionDtype.
                    This can be used to override the default pandas type for conversion
                    of built-in pyarrow types or in absence of pandas_metadata in the
                    Table schema. The function receives a pyarrow DataType and is
                    expected to return a pandas ExtensionDtype or ``None`` if the
                    default conversion should be used for that type. If you have
                    a dictionary mapping, you can pass ``dict.get`` as function.
        
                Returns
                -------
                pandas.Series or pandas.DataFrame depending on type of object
        
                Examples
                --------
                >>> import pyarrow as pa
                >>> import pandas as pd
        
                Convert a Table to pandas DataFrame:
        
                >>> table = pa.table([
                ...    pa.array([2, 4, 5, 100]),
                ...    pa.array(["Flamingo", "Horse", "Brittle stars", "Centipede"])
                ...    ], names=['n_legs', 'animals'])
                >>> table.to_pandas()
                   n_legs        animals
                0       2       Flamingo
                1       4          Horse
                2       5  Brittle stars
                3     100      Centipede
                >>> isinstance(table.to_pandas(), pd.DataFrame)
                True
        
                Convert a RecordBatch to pandas DataFrame:
        
                >>> import pyarrow as pa
                >>> n_legs = pa.array([2, 4, 5, 100])
                >>> animals = pa.array(["Flamingo", "Horse", "Brittle stars", "Centipede"])
                >>> batch = pa.record_batch([n_legs, animals],
                ...                         names=["n_legs", "animals"])
                >>> batch
                pyarrow.RecordBatch
                n_legs: int64
                animals: string
                >>> batch.to_pandas()
                   n_legs        animals
                0       2       Flamingo
                1       4          Horse
                2       5  Brittle stars
                3     100      Centipede
                >>> isinstance(batch.to_pandas(), pd.DataFrame)
                True
        
                Convert a Chunked Array to pandas Series:
        
                >>> import pyarrow as pa
                >>> n_legs = pa.chunked_array([[2, 2, 4], [4, 5, 100]])
                >>> n_legs.to_pandas()
                0      2
                1      2
                2      4
                3      4
                4      5
                5    100
                dtype: int64
                >>> isinstance(n_legs.to_pandas(), pd.Series)
                True
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ _PandasConvertible.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ _PandasConvertible.__setstate_cython__(self, __pyx_state) """
        pass


