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


from ._PandasConvertible import _PandasConvertible

class RecordBatch(_PandasConvertible):
    """
    RecordBatch()
    
        Batch of rows of columns of equal length
    
        Warnings
        --------
        Do not call this class's constructor directly, use one of the
        ``RecordBatch.from_*`` functions instead.
    
        Examples
        --------
        >>> import pyarrow as pa
        >>> n_legs = pa.array([2, 2, 4, 4, 5, 100])
        >>> animals = pa.array(["Flamingo", "Parrot", "Dog", "Horse", "Brittle stars", "Centipede"])
        >>> names = ["n_legs", "animals"]
    
        Constructing a RecordBatch from arrays:
    
        >>> pa.RecordBatch.from_arrays([n_legs, animals], names=names)
        pyarrow.RecordBatch
        n_legs: int64
        animals: string
        >>> pa.RecordBatch.from_arrays([n_legs, animals], names=names).to_pandas()
           n_legs        animals
        0       2       Flamingo
        1       2         Parrot
        2       4            Dog
        3       4          Horse
        4       5  Brittle stars
        5     100      Centipede
    
        Constructing a RecordBatch from pandas DataFrame:
    
        >>> import pandas as pd
        >>> df = pd.DataFrame({'year': [2020, 2022, 2021, 2022],
        ...                    'month': [3, 5, 7, 9],
        ...                    'day': [1, 5, 9, 13],
        ...                    'n_legs': [2, 4, 5, 100],
        ...                    'animals': ["Flamingo", "Horse", "Brittle stars", "Centipede"]})
        >>> pa.RecordBatch.from_pandas(df)
        pyarrow.RecordBatch
        year: int64
        month: int64
        day: int64
        n_legs: int64
        animals: string
        >>> pa.RecordBatch.from_pandas(df).to_pandas()
           year  month  day  n_legs        animals
        0  2020      3    1       2       Flamingo
        1  2022      5    5       4          Horse
        2  2021      7    9       5  Brittle stars
        3  2022      9   13     100      Centipede
    
        Constructing a RecordBatch from pylist:
    
        >>> pylist = [{'n_legs': 2, 'animals': 'Flamingo'},
        ...           {'n_legs': 4, 'animals': 'Dog'}]
        >>> pa.RecordBatch.from_pylist(pylist).to_pandas()
           n_legs   animals
        0       2  Flamingo
        1       4       Dog
    
        You can also construct a RecordBatch using :func:`pyarrow.record_batch`:
    
        >>> pa.record_batch([n_legs, animals], names=names).to_pandas()
           n_legs        animals
        0       2       Flamingo
        1       2         Parrot
        2       4            Dog
        3       4          Horse
        4       5  Brittle stars
        5     100      Centipede
    
        >>> pa.record_batch(df)
        pyarrow.RecordBatch
        year: int64
        month: int64
        day: int64
        n_legs: int64
        animals: string
    """
    def column(self, i): # real signature unknown; restored from __doc__
        """
        RecordBatch.column(self, i)
        
                Select single column from record batch
        
                Parameters
                ----------
                i : int or string
                    The index or name of the column to retrieve.
        
                Returns
                -------
                column : pyarrow.Array
        
                Examples
                --------
                >>> import pyarrow as pa
                >>> n_legs = pa.array([2, 2, 4, 4, 5, 100])
                >>> animals = pa.array(["Flamingo", "Parrot", "Dog", "Horse", "Brittle stars", "Centipede"])
                >>> batch = pa.RecordBatch.from_arrays([n_legs, animals],
                ...                                     names=["n_legs", "animals"])
                >>> batch.column(1)
                <pyarrow.lib.StringArray object at ...>
                [
                  "Flamingo",
                  "Parrot",
                  "Dog",
                  "Horse",
                  "Brittle stars",
                  "Centipede"
                ]
        """
        pass

    def drop_null(self): # real signature unknown; restored from __doc__
        """
        RecordBatch.drop_null(self)
        
                Remove missing values from a RecordBatch.
                See :func:`pyarrow.compute.drop_null` for full usage.
        
                Examples
                --------
                >>> import pyarrow as pa
                >>> n_legs = pa.array([2, 2, 4, 4, 5, 100])
                >>> animals = pa.array(["Flamingo", "Parrot", "Dog", "Horse", None, "Centipede"])
                >>> batch = pa.RecordBatch.from_arrays([n_legs, animals],
                ...                                     names=["n_legs", "animals"])
                >>> batch.to_pandas()
                   n_legs    animals
                0       2   Flamingo
                1       2     Parrot
                2       4        Dog
                3       4      Horse
                4       5       None
                5     100  Centipede
                >>> batch.drop_null().to_pandas()
                   n_legs    animals
                0       2   Flamingo
                1       2     Parrot
                2       4        Dog
                3       4      Horse
                4     100  Centipede
        """
        pass

    def equals(self, other, bool_check_metadata=False): # real signature unknown; restored from __doc__
        """
        RecordBatch.equals(self, other, bool check_metadata=False)
        
                Check if contents of two record batches are equal.
        
                Parameters
                ----------
                other : pyarrow.RecordBatch
                    RecordBatch to compare against.
                check_metadata : bool, default False
                    Whether schema metadata equality should be checked as well.
        
                Returns
                -------
                are_equal : bool
        
                Examples
                --------
                >>> import pyarrow as pa
                >>> n_legs = pa.array([2, 2, 4, 4, 5, 100])
                >>> animals = pa.array(["Flamingo", "Parrot", "Dog", "Horse", "Brittle stars", "Centipede"])
                >>> batch = pa.RecordBatch.from_arrays([n_legs, animals],
                ...                                     names=["n_legs", "animals"])
                >>> batch_0 = pa.record_batch([])
                >>> batch_1 = pa.RecordBatch.from_arrays([n_legs, animals],
                ...                                       names=["n_legs", "animals"],
                ...                                       metadata={"n_legs": "Number of legs per animal"})
                >>> batch.equals(batch)
                True
                >>> batch.equals(batch_0)
                False
                >>> batch.equals(batch_1)
                True
                >>> batch.equals(batch_1, check_metadata=True)
                False
        """
        pass

    def field(self, i): # real signature unknown; restored from __doc__
        """
        RecordBatch.field(self, i)
        
                Select a schema field by its column name or numeric index
        
                Parameters
                ----------
                i : int or string
                    The index or name of the field to retrieve
        
                Returns
                -------
                pyarrow.Field
        
                Examples
                --------
                >>> import pyarrow as pa
                >>> n_legs = pa.array([2, 2, 4, 4, 5, 100])
                >>> animals = pa.array(["Flamingo", "Parrot", "Dog", "Horse", "Brittle stars", "Centipede"])
                >>> batch = pa.RecordBatch.from_arrays([n_legs, animals],
                ...                                     names=["n_legs", "animals"])
                >>> batch.field(0)
                pyarrow.Field<n_legs: int64>
                >>> batch.field(1)
                pyarrow.Field<animals: string>
        """
        pass

    def filter(self, mask, null_selection_behavior=None): # real signature unknown; restored from __doc__
        """
        RecordBatch.filter(self, mask, null_selection_behavior=u'drop')
        
                Select rows from the record batch.
        
                See :func:`pyarrow.compute.filter` for full usage.
        
                Parameters
                ----------
                mask : Array or array-like
                    The boolean mask to filter the record batch with.
                null_selection_behavior : str, default "drop"
                    How nulls in the mask should be handled.
        
                Returns
                -------
                filtered : RecordBatch
                    A record batch of the same schema, with only the rows selected
                    by the boolean mask.
        
                Examples
                --------
                >>> import pyarrow as pa
                >>> n_legs = pa.array([2, 2, 4, 4, 5, 100])
                >>> animals = pa.array(["Flamingo", "Parrot", "Dog", "Horse", "Brittle stars", "Centipede"])
                >>> batch = pa.RecordBatch.from_arrays([n_legs, animals],
                ...                                     names=["n_legs", "animals"])
                >>> batch.to_pandas()
                   n_legs        animals
                0       2       Flamingo
                1       2         Parrot
                2       4            Dog
                3       4          Horse
                4       5  Brittle stars
                5     100      Centipede
        
                Define a mask and select rows:
        
                >>> mask=[True, True, False, True, False, None]
                >>> batch.filter(mask).to_pandas()
                   n_legs   animals
                0       2  Flamingo
                1       2    Parrot
                2       4     Horse
                >>> batch.filter(mask, null_selection_behavior='emit_null').to_pandas()
                   n_legs   animals
                0     2.0  Flamingo
                1     2.0    Parrot
                2     4.0     Horse
                3     NaN      None
        """
        pass

    def from_arrays(self, list_arrays, names=None, schema=None, metadata=None): # real signature unknown; restored from __doc__
        """
        RecordBatch.from_arrays(list arrays, names=None, schema=None, metadata=None)
        
                Construct a RecordBatch from multiple pyarrow.Arrays
        
                Parameters
                ----------
                arrays : list of pyarrow.Array
                    One for each field in RecordBatch
                names : list of str, optional
                    Names for the batch fields. If not passed, schema must be passed
                schema : Schema, default None
                    Schema for the created batch. If not passed, names must be passed
                metadata : dict or Mapping, default None
                    Optional metadata for the schema (if inferred).
        
                Returns
                -------
                pyarrow.RecordBatch
        
                Examples
                --------
                >>> import pyarrow as pa
                >>> n_legs = pa.array([2, 2, 4, 4, 5, 100])
                >>> animals = pa.array(["Flamingo", "Parrot", "Dog", "Horse", "Brittle stars", "Centipede"])
                >>> names = ["n_legs", "animals"]
        
                Construct a RecordBartch from pyarrow Arrays using names:
        
                >>> pa.RecordBatch.from_arrays([n_legs, animals], names=names)
                pyarrow.RecordBatch
                n_legs: int64
                animals: string
                >>> pa.RecordBatch.from_arrays([n_legs, animals], names=names).to_pandas()
                   n_legs        animals
                0       2       Flamingo
                1       2         Parrot
                2       4            Dog
                3       4          Horse
                4       5  Brittle stars
                5     100      Centipede
        
                Construct a RecordBartch from pyarrow Arrays using schema:
        
                >>> my_schema = pa.schema([
                ...     pa.field('n_legs', pa.int64()),
                ...     pa.field('animals', pa.string())],
                ...     metadata={"n_legs": "Number of legs per animal"})
                >>> pa.RecordBatch.from_arrays([n_legs, animals], schema=my_schema).to_pandas()
                   n_legs        animals
                0       2       Flamingo
                1       2         Parrot
                2       4            Dog
                3       4          Horse
                4       5  Brittle stars
                5     100      Centipede
                >>> pa.RecordBatch.from_arrays([n_legs, animals], schema=my_schema).schema
                n_legs: int64
                animals: string
                -- schema metadata --
                n_legs: 'Number of legs per animal'
        """
        pass

    @classmethod
    def from_pandas(cls, type_cls, df, Schema_schema=None, preserve_index=None, nthreads=None, columns=None): # real signature unknown; restored from __doc__
        """
        RecordBatch.from_pandas(type cls, df, Schema schema=None, preserve_index=None, nthreads=None, columns=None)
        
                Convert pandas.DataFrame to an Arrow RecordBatch
        
                Parameters
                ----------
                df : pandas.DataFrame
                schema : pyarrow.Schema, optional
                    The expected schema of the RecordBatch. This can be used to
                    indicate the type of columns if we cannot infer it automatically.
                    If passed, the output will have exactly this schema. Columns
                    specified in the schema that are not found in the DataFrame columns
                    or its index will raise an error. Additional columns or index
                    levels in the DataFrame which are not specified in the schema will
                    be ignored.
                preserve_index : bool, optional
                    Whether to store the index as an additional column in the resulting
                    ``RecordBatch``. The default of None will store the index as a
                    column, except for RangeIndex which is stored as metadata only. Use
                    ``preserve_index=True`` to force it to be stored as a column.
                nthreads : int, default None
                    If greater than 1, convert columns to Arrow in parallel using
                    indicated number of threads. By default, this follows
                    :func:`pyarrow.cpu_count` (may use up to system CPU count threads).
                columns : list, optional
                   List of column to be converted. If None, use all columns.
        
                Returns
                -------
                pyarrow.RecordBatch
        
        
                Examples
                --------
                >>> import pandas as pd
                >>> df = pd.DataFrame({'year': [2020, 2022, 2021, 2022],
                ...                    'month': [3, 5, 7, 9],
                ...                    'day': [1, 5, 9, 13],
                ...                    'n_legs': [2, 4, 5, 100],
                ...                    'animals': ["Flamingo", "Horse", "Brittle stars", "Centipede"]})
        
                Convert pandas DataFrame to RecordBatch:
        
                >>> import pyarrow as pa
                >>> pa.RecordBatch.from_pandas(df)
                pyarrow.RecordBatch
                year: int64
                month: int64
                day: int64
                n_legs: int64
                animals: string
        
                Convert pandas DataFrame to RecordBatch using schema:
        
                >>> my_schema = pa.schema([
                ...     pa.field('n_legs', pa.int64()),
                ...     pa.field('animals', pa.string())],
                ...     metadata={"n_legs": "Number of legs per animal"})
                >>> pa.RecordBatch.from_pandas(df, schema=my_schema)
                pyarrow.RecordBatch
                n_legs: int64
                animals: string
        
                Convert pandas DataFrame to RecordBatch specifying columns:
        
                >>> pa.RecordBatch.from_pandas(df, columns=["n_legs"])
                pyarrow.RecordBatch
                n_legs: int64
        """
        pass

    def from_pydict(self, mapping, schema=None, metadata=None): # real signature unknown; restored from __doc__
        """
        RecordBatch.from_pydict(mapping, schema=None, metadata=None)
        
                Construct a RecordBatch from Arrow arrays or columns.
        
                Parameters
                ----------
                mapping : dict or Mapping
                    A mapping of strings to Arrays or Python lists.
                schema : Schema, default None
                    If not passed, will be inferred from the Mapping values.
                metadata : dict or Mapping, default None
                    Optional metadata for the schema (if inferred).
        
                Returns
                -------
                RecordBatch
        
                Examples
                --------
                >>> import pyarrow as pa
                >>> n_legs = [2, 2, 4, 4, 5, 100]
                >>> animals = ["Flamingo", "Parrot", "Dog", "Horse", "Brittle stars", "Centipede"]
                >>> pydict = {'n_legs': n_legs, 'animals': animals}
        
                Construct a RecordBatch from arrays:
        
                >>> pa.RecordBatch.from_pydict(pydict)
                pyarrow.RecordBatch
                n_legs: int64
                animals: string
                >>> pa.RecordBatch.from_pydict(pydict).to_pandas()
                   n_legs        animals
                0       2       Flamingo
                1       2         Parrot
                2       4            Dog
                3       4          Horse
                4       5  Brittle stars
                5     100      Centipede
        
                Construct a RecordBatch with schema:
        
                >>> my_schema = pa.schema([
                ...     pa.field('n_legs', pa.int64()),
                ...     pa.field('animals', pa.string())],
                ...     metadata={"n_legs": "Number of legs per animal"})
                >>> pa.RecordBatch.from_pydict(pydict, schema=my_schema).schema
                n_legs: int64
                animals: string
                -- schema metadata --
                n_legs: 'Number of legs per animal'
        """
        pass

    def from_pylist(self, mapping, schema=None, metadata=None): # real signature unknown; restored from __doc__
        """
        RecordBatch.from_pylist(mapping, schema=None, metadata=None)
        
                Construct a RecordBatch from list of rows / dictionaries.
        
                Parameters
                ----------
                mapping : list of dicts of rows
                    A mapping of strings to row values.
                schema : Schema, default None
                    If not passed, will be inferred from the first row of the
                    mapping values.
                metadata : dict or Mapping, default None
                    Optional metadata for the schema (if inferred).
        
                Returns
                -------
                RecordBatch
        
                Examples
                --------
                >>> import pyarrow as pa
                >>> pylist = [{'n_legs': 2, 'animals': 'Flamingo'},
                ...           {'n_legs': 4, 'animals': 'Dog'}]
                >>> pa.RecordBatch.from_pylist(pylist)
                pyarrow.RecordBatch
                n_legs: int64
                animals: string
                >>> pa.RecordBatch.from_pylist(pylist).to_pandas()
                   n_legs   animals
                0       2  Flamingo
                1       4       Dog
        
                Construct a RecordBatch with metadata:
        
                >>> my_metadata={"n_legs": "Number of legs per animal"}
                >>> pa.RecordBatch.from_pylist(pylist, metadata=my_metadata).schema
                n_legs: int64
                animals: string
                -- schema metadata --
                n_legs: 'Number of legs per animal'
        """
        pass

    def from_struct_array(self, StructArray_struct_array): # real signature unknown; restored from __doc__
        """
        RecordBatch.from_struct_array(StructArray struct_array)
        
                Construct a RecordBatch from a StructArray.
        
                Each field in the StructArray will become a column in the resulting
                ``RecordBatch``.
        
                Parameters
                ----------
                struct_array : StructArray
                    Array to construct the record batch from.
        
                Returns
                -------
                pyarrow.RecordBatch
        
                Examples
                --------
                >>> import pyarrow as pa
                >>> struct = pa.array([{'n_legs': 2, 'animals': 'Parrot'},
                ...                    {'year': 2022, 'n_legs': 4}])
                >>> pa.RecordBatch.from_struct_array(struct).to_pandas()
                  animals  n_legs    year
                0  Parrot       2     NaN
                1    None       4  2022.0
        """
        pass

    def get_total_buffer_size(self): # real signature unknown; restored from __doc__
        """
        RecordBatch.get_total_buffer_size(self)
        
                The sum of bytes in each buffer referenced by the record batch
        
                An array may only reference a portion of a buffer.
                This method will overestimate in this case and return the
                byte size of the entire buffer.
        
                If a buffer is referenced multiple times then it will
                only be counted once.
        
                Examples
                --------
                >>> import pyarrow as pa
                >>> n_legs = pa.array([2, 2, 4, 4, 5, 100])
                >>> animals = pa.array(["Flamingo", "Parrot", "Dog", "Horse", "Brittle stars", "Centipede"])
                >>> batch = pa.RecordBatch.from_arrays([n_legs, animals],
                ...                                     names=["n_legs", "animals"])
                >>> batch.get_total_buffer_size()
                120
        """
        pass

    def replace_schema_metadata(self, metadata=None): # real signature unknown; restored from __doc__
        """
        RecordBatch.replace_schema_metadata(self, metadata=None)
        
                Create shallow copy of record batch by replacing schema
                key-value metadata with the indicated new metadata (which may be None,
                which deletes any existing metadata
        
                Parameters
                ----------
                metadata : dict, default None
        
                Returns
                -------
                shallow_copy : RecordBatch
        
                Examples
                --------
                >>> import pyarrow as pa
                >>> n_legs = pa.array([2, 2, 4, 4, 5, 100])
        
                Constructing a RecordBatch with schema and metadata:
        
                >>> my_schema = pa.schema([
                ...     pa.field('n_legs', pa.int64())],
                ...     metadata={"n_legs": "Number of legs per animal"})
                >>> batch = pa.RecordBatch.from_arrays([n_legs], schema=my_schema)
                >>> batch.schema
                n_legs: int64
                -- schema metadata --
                n_legs: 'Number of legs per animal'
        
                Shallow copy of a RecordBatch with deleted schema metadata:
        
                >>> batch.replace_schema_metadata().schema
                n_legs: int64
        """
        pass

    def serialize(self, memory_pool=None): # real signature unknown; restored from __doc__
        """
        RecordBatch.serialize(self, memory_pool=None)
        
                Write RecordBatch to Buffer as encapsulated IPC message.
        
                Parameters
                ----------
                memory_pool : MemoryPool, default None
                    Uses default memory pool if not specified
        
                Returns
                -------
                serialized : Buffer
        
                Examples
                --------
                >>> import pyarrow as pa
                >>> n_legs = pa.array([2, 2, 4, 4, 5, 100])
                >>> animals = pa.array(["Flamingo", "Parrot", "Dog", "Horse", "Brittle stars", "Centipede"])
                >>> batch = pa.RecordBatch.from_arrays([n_legs, animals],
                ...                                     names=["n_legs", "animals"])
                >>> batch.serialize()
                <pyarrow.Buffer address=0x... size=... is_cpu=True is_mutable=True>
        """
        pass

    def slice(self, offset=0, length=None): # real signature unknown; restored from __doc__
        """
        RecordBatch.slice(self, offset=0, length=None)
        
                Compute zero-copy slice of this RecordBatch
        
                Parameters
                ----------
                offset : int, default 0
                    Offset from start of record batch to slice
                length : int, default None
                    Length of slice (default is until end of batch starting from
                    offset)
        
                Returns
                -------
                sliced : RecordBatch
        
                Examples
                --------
                >>> import pyarrow as pa
                >>> n_legs = pa.array([2, 2, 4, 4, 5, 100])
                >>> animals = pa.array(["Flamingo", "Parrot", "Dog", "Horse", "Brittle stars", "Centipede"])
                >>> batch = pa.RecordBatch.from_arrays([n_legs, animals],
                ...                                     names=["n_legs", "animals"])
                >>> batch.to_pandas()
                   n_legs        animals
                0       2       Flamingo
                1       2         Parrot
                2       4            Dog
                3       4          Horse
                4       5  Brittle stars
                5     100      Centipede
                >>> batch.slice(offset=3).to_pandas()
                   n_legs        animals
                0       4          Horse
                1       5  Brittle stars
                2     100      Centipede
                >>> batch.slice(length=2).to_pandas()
                   n_legs   animals
                0       2  Flamingo
                1       2    Parrot
                >>> batch.slice(offset=3, length=1).to_pandas()
                   n_legs animals
                0       4   Horse
        """
        pass

    def sort_by(self, sorting, **kwargs): # real signature unknown; restored from __doc__
        """
        RecordBatch.sort_by(self, sorting, **kwargs)
        
                Sort the RecordBatch by one or multiple columns.
        
                Parameters
                ----------
                sorting : str or list[tuple(name, order)]
                    Name of the column to use to sort (ascending), or
                    a list of multiple sorting conditions where
                    each entry is a tuple with column name
                    and sorting order ("ascending" or "descending")
                **kwargs : dict, optional
                    Additional sorting options.
                    As allowed by :class:`SortOptions`
        
                Returns
                -------
                RecordBatch
                    A new record batch sorted according to the sort keys.
        """
        pass

    def take(self, indices): # real signature unknown; restored from __doc__
        """
        RecordBatch.take(self, indices)
        
                Select rows from the record batch.
        
                See :func:`pyarrow.compute.take` for full usage.
        
                Parameters
                ----------
                indices : Array or array-like
                    The indices in the record batch whose rows will be returned.
        
                Returns
                -------
                taken : RecordBatch
                    A record batch with the same schema, containing the taken rows.
        
                Examples
                --------
                >>> import pyarrow as pa
                >>> n_legs = pa.array([2, 2, 4, 4, 5, 100])
                >>> animals = pa.array(["Flamingo", "Parrot", "Dog", "Horse", "Brittle stars", "Centipede"])
                >>> batch = pa.RecordBatch.from_arrays([n_legs, animals],
                ...                                     names=["n_legs", "animals"])
                >>> batch.take([1,3,4]).to_pandas()
                   n_legs        animals
                0       2         Parrot
                1       4          Horse
                2       5  Brittle stars
        """
        pass

    def to_pydict(self): # real signature unknown; restored from __doc__
        """
        RecordBatch.to_pydict(self)
        
                Convert the RecordBatch to a dict or OrderedDict.
        
                Returns
                -------
                dict
        
                Examples
                --------
                >>> import pyarrow as pa
                >>> n_legs = pa.array([2, 2, 4, 4, 5, 100])
                >>> animals = pa.array(["Flamingo", "Parrot", "Dog", "Horse", "Brittle stars", "Centipede"])
                >>> batch = pa.RecordBatch.from_arrays([n_legs, animals],
                ...                                     names=["n_legs", "animals"])
                >>> batch.to_pydict()
                {'n_legs': [2, 2, 4, 4, 5, 100], 'animals': ['Flamingo', 'Parrot', ..., 'Centipede']}
        """
        pass

    def to_pylist(self): # real signature unknown; restored from __doc__
        """
        RecordBatch.to_pylist(self)
        
                Convert the RecordBatch to a list of rows / dictionaries.
        
                Returns
                -------
                list
        
                Examples
                --------
                >>> import pyarrow as pa
                >>> n_legs = pa.array([2, 2, 4, 4, 5, 100])
                >>> animals = pa.array(["Flamingo", "Parrot", "Dog", "Horse", "Brittle stars", "Centipede"])
                >>> batch = pa.RecordBatch.from_arrays([n_legs, animals],
                ...                                     names=["n_legs", "animals"])
                >>> batch.to_pylist()
                [{'n_legs': 2, 'animals': 'Flamingo'}, {'n_legs': 2, ...}, {'n_legs': 100, 'animals': 'Centipede'}]
        """
        pass

    def to_string(self, show_metadata=False): # real signature unknown; restored from __doc__
        """ RecordBatch.to_string(self, show_metadata=False) """
        pass

    def validate(self, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        RecordBatch.validate(self, *, full=False)
        
                Perform validation checks.  An exception is raised if validation fails.
        
                By default only cheap validation checks are run.  Pass `full=True`
                for thorough validation checks (potentially O(n)).
        
                Parameters
                ----------
                full : bool, default False
                    If True, run expensive checks, otherwise cheap checks only.
        
                Raises
                ------
                ArrowInvalid
        """
        pass

    def _column(self, int_i): # real signature unknown; restored from __doc__
        """
        RecordBatch._column(self, int i)
        
                Select single column from record batch by its numeric index.
        
                Parameters
                ----------
                i : int
                    The index of the column to retrieve.
        
                Returns
                -------
                column : pyarrow.Array
        """
        pass

    def _ensure_integer_index(self, i): # real signature unknown; restored from __doc__
        """
        RecordBatch._ensure_integer_index(self, i)
        
                Ensure integer index (convert string column name to integer if needed).
        """
        pass

    def _export_to_c(self, out_ptr, out_schema_ptr=0): # real signature unknown; restored from __doc__
        """
        RecordBatch._export_to_c(self, out_ptr, out_schema_ptr=0)
        
                Export to a C ArrowArray struct, given its pointer.
        
                If a C ArrowSchema struct pointer is also given, the record batch
                schema is exported to it at the same time.
        
                Parameters
                ----------
                out_ptr: int
                    The raw pointer to a C ArrowArray struct.
                out_schema_ptr: int (optional)
                    The raw pointer to a C ArrowSchema struct.
        
                Be careful: if you don't pass the ArrowArray struct to a consumer,
                array memory will leak.  This is a low-level function intended for
                expert users.
        """
        pass

    def _import_from_c(self, in_ptr, schema): # real signature unknown; restored from __doc__
        """
        RecordBatch._import_from_c(in_ptr, schema)
        
                Import RecordBatch from a C ArrowArray struct, given its pointer
                and the imported schema.
        
                Parameters
                ----------
                in_ptr: int
                    The raw pointer to a C ArrowArray struct.
                type: Schema or int
                    Either a Schema object, or the raw pointer to a C ArrowSchema
                    struct.
        
                This is a low-level function intended for expert users.
        """
        pass

    def _to_pandas(self, options, **kwargs): # real signature unknown; restored from __doc__
        """ RecordBatch._to_pandas(self, options, **kwargs) """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __getitem__(self, *args, **kwargs): # real signature unknown
        """
        Slice or return column at given index or column name
        
                Parameters
                ----------
                key : integer, str, or slice
                    Slices with step not equal to 1 (or None) will produce a copy
                    rather than a zero-copy view
        
                Returns
                -------
                value : Array (index/column) or RecordBatch (slice)
        """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __reduce__(self): # real signature unknown; restored from __doc__
        """ RecordBatch.__reduce__(self) """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __sizeof__(self): # real signature unknown; restored from __doc__
        """ RecordBatch.__sizeof__(self) """
        pass

    columns = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        List of all columns in numerical order

        Returns
        -------
        list of pyarrow.Array

        Examples
        --------
        >>> import pyarrow as pa
        >>> n_legs = pa.array([2, 2, 4, 4, 5, 100])
        >>> animals = pa.array(["Flamingo", "Parrot", "Dog", "Horse", "Brittle stars", "Centipede"])
        >>> batch = pa.RecordBatch.from_arrays([n_legs, animals],
        ...                                     names=["n_legs", "animals"])
        >>> batch.columns
        [<pyarrow.lib.Int64Array object at ...>
        [
          2,
          2,
          4,
          4,
          5,
          100
        ], <pyarrow.lib.StringArray object at ...>
        [
          "Flamingo",
          "Parrot",
          "Dog",
          "Horse",
          "Brittle stars",
          "Centipede"
        ]]
        """

    nbytes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Total number of bytes consumed by the elements of the record batch.

        In other words, the sum of bytes from all buffer ranges referenced.

        Unlike `get_total_buffer_size` this method will account for array
        offsets.

        If buffers are shared between arrays then the shared
        portion will only be counted multiple times.

        The dictionary of dictionary arrays will always be counted in their
        entirety even if the array only references a portion of the dictionary.

        Examples
        --------
        >>> import pyarrow as pa
        >>> n_legs = pa.array([2, 2, 4, 4, 5, 100])
        >>> animals = pa.array(["Flamingo", "Parrot", "Dog", "Horse", "Brittle stars", "Centipede"])
        >>> batch = pa.RecordBatch.from_arrays([n_legs, animals],
        ...                                     names=["n_legs", "animals"])
        >>> batch.nbytes
        116
        """

    num_columns = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Number of columns

        Returns
        -------
        int

        Examples
        --------
        >>> import pyarrow as pa
        >>> n_legs = pa.array([2, 2, 4, 4, 5, 100])
        >>> animals = pa.array(["Flamingo", "Parrot", "Dog", "Horse", "Brittle stars", "Centipede"])
        >>> batch = pa.RecordBatch.from_arrays([n_legs, animals],
        ...                                     names=["n_legs", "animals"])
        >>> batch.num_columns
        2
        """

    num_rows = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Number of rows

        Due to the definition of a RecordBatch, all columns have the same
        number of rows.

        Returns
        -------
        int

        Examples
        --------
        >>> import pyarrow as pa
        >>> n_legs = pa.array([2, 2, 4, 4, 5, 100])
        >>> animals = pa.array(["Flamingo", "Parrot", "Dog", "Horse", "Brittle stars", "Centipede"])
        >>> batch = pa.RecordBatch.from_arrays([n_legs, animals],
        ...                                     names=["n_legs", "animals"])
        >>> batch.num_rows
        6
        """

    schema = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Schema of the RecordBatch and its columns

        Returns
        -------
        pyarrow.Schema

        Examples
        --------
        >>> import pyarrow as pa
        >>> n_legs = pa.array([2, 2, 4, 4, 5, 100])
        >>> animals = pa.array(["Flamingo", "Parrot", "Dog", "Horse", "Brittle stars", "Centipede"])
        >>> batch = pa.RecordBatch.from_arrays([n_legs, animals],
        ...                                     names=["n_legs", "animals"])
        >>> batch.schema
        n_legs: int64
        animals: string
        """


    __hash__ = None
    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001970BCC57E0>'


