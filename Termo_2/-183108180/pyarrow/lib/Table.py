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

class Table(_PandasConvertible):
    """
    Table()
    
        A collection of top-level named, equal length Arrow arrays.
    
        Warnings
        --------
        Do not call this class's constructor directly, use one of the ``from_*``
        methods instead.
    
        Examples
        --------
        >>> import pyarrow as pa
        >>> n_legs = pa.array([2, 4, 5, 100])
        >>> animals = pa.array(["Flamingo", "Horse", "Brittle stars", "Centipede"])
        >>> names = ["n_legs", "animals"]
    
        Construct a Table from arrays:
    
        >>> pa.Table.from_arrays([n_legs, animals], names=names)
        pyarrow.Table
        n_legs: int64
        animals: string
        ----
        n_legs: [[2,4,5,100]]
        animals: [["Flamingo","Horse","Brittle stars","Centipede"]]
    
        Construct a Table from a RecordBatch:
    
        >>> batch = pa.record_batch([n_legs, animals], names=names)
        >>> pa.Table.from_batches([batch])
        pyarrow.Table
        n_legs: int64
        animals: string
        ----
        n_legs: [[2,4,5,100]]
        animals: [["Flamingo","Horse","Brittle stars","Centipede"]]
    
        Construct a Table from pandas DataFrame:
    
        >>> import pandas as pd
        >>> df = pd.DataFrame({'year': [2020, 2022, 2019, 2021],
        ...                    'n_legs': [2, 4, 5, 100],
        ...                    'animals': ["Flamingo", "Horse", "Brittle stars", "Centipede"]})
        >>> pa.Table.from_pandas(df)
        pyarrow.Table
        year: int64
        n_legs: int64
        animals: string
        ----
        year: [[2020,2022,2019,2021]]
        n_legs: [[2,4,5,100]]
        animals: [["Flamingo","Horse","Brittle stars","Centipede"]]
    
        Construct a Table from a dictionary of arrays:
    
        >>> pydict = {'n_legs': n_legs, 'animals': animals}
        >>> pa.Table.from_pydict(pydict)
        pyarrow.Table
        n_legs: int64
        animals: string
        ----
        n_legs: [[2,4,5,100]]
        animals: [["Flamingo","Horse","Brittle stars","Centipede"]]
        >>> pa.Table.from_pydict(pydict).schema
        n_legs: int64
        animals: string
    
        Construct a Table from a dictionary of arrays with metadata:
    
        >>> my_metadata={"n_legs": "Number of legs per animal"}
        >>> pa.Table.from_pydict(pydict, metadata=my_metadata).schema
        n_legs: int64
        animals: string
        -- schema metadata --
        n_legs: 'Number of legs per animal'
    
        Construct a Table from a list of rows:
    
        >>> pylist = [{'n_legs': 2, 'animals': 'Flamingo'}, {'year': 2021, 'animals': 'Centipede'}]
        >>> pa.Table.from_pylist(pylist)
        pyarrow.Table
        n_legs: int64
        animals: string
        ----
        n_legs: [[2,null]]
        animals: [["Flamingo","Centipede"]]
    
        Construct a Table from a list of rows with pyarrow schema:
    
        >>> my_schema = pa.schema([
        ...     pa.field('year', pa.int64()),
        ...     pa.field('n_legs', pa.int64()),
        ...     pa.field('animals', pa.string())],
        ...     metadata={"year": "Year of entry"})
        >>> pa.Table.from_pylist(pylist, schema=my_schema).schema
        year: int64
        n_legs: int64
        animals: string
        -- schema metadata --
        year: 'Year of entry'
    
        Construct a Table with :func:`pyarrow.table`:
    
        >>> pa.table([n_legs, animals], names=names)
        pyarrow.Table
        n_legs: int64
        animals: string
        ----
        n_legs: [[2,4,5,100]]
        animals: [["Flamingo","Horse","Brittle stars","Centipede"]]
    """
    def add_column(self, int_i, field_, column): # real signature unknown; restored from __doc__
        """
        Table.add_column(self, int i, field_, column)
        
                Add column to Table at position.
        
                A new table is returned with the column added, the original table
                object is left unchanged.
        
                Parameters
                ----------
                i : int
                    Index to place the column at.
                field_ : str or Field
                    If a string is passed then the type is deduced from the column
                    data.
                column : Array, list of Array, or values coercible to arrays
                    Column data.
        
                Returns
                -------
                Table
                    New table with the passed column added.
        
                Examples
                --------
                >>> import pyarrow as pa
                >>> import pandas as pd
                >>> df = pd.DataFrame({'n_legs': [2, 4, 5, 100],
                ...                    'animals': ["Flamingo", "Horse", "Brittle stars", "Centipede"]})
                >>> table = pa.Table.from_pandas(df)
        
                Add column:
        
                >>> year = [2021, 2022, 2019, 2021]
                >>> table.add_column(0,"year", [year])
                pyarrow.Table
                year: int64
                n_legs: int64
                animals: string
                ----
                year: [[2021,2022,2019,2021]]
                n_legs: [[2,4,5,100]]
                animals: [["Flamingo","Horse","Brittle stars","Centipede"]]
        
                Original table is left unchanged:
        
                >>> table
                pyarrow.Table
                n_legs: int64
                animals: string
                ----
                n_legs: [[2,4,5,100]]
                animals: [["Flamingo","Horse","Brittle stars","Centipede"]]
        """
        pass

    def append_column(self, field_, column): # real signature unknown; restored from __doc__
        """
        Table.append_column(self, field_, column)
        
                Append column at end of columns.
        
                Parameters
                ----------
                field_ : str or Field
                    If a string is passed then the type is deduced from the column
                    data.
                column : Array, list of Array, or values coercible to arrays
                    Column data.
        
                Returns
                -------
                Table
                    New table with the passed column added.
        
                Examples
                --------
                >>> import pyarrow as pa
                >>> import pandas as pd
                >>> df = pd.DataFrame({'n_legs': [2, 4, 5, 100],
                ...                    'animals': ["Flamingo", "Horse", "Brittle stars", "Centipede"]})
                >>> table = pa.Table.from_pandas(df)
        
                Append column at the end:
        
                >>> year = [2021, 2022, 2019, 2021]
                >>> table.append_column('year', [year])
                pyarrow.Table
                n_legs: int64
                animals: string
                year: int64
                ----
                n_legs: [[2,4,5,100]]
                animals: [["Flamingo","Horse","Brittle stars","Centipede"]]
                year: [[2021,2022,2019,2021]]
        """
        pass

    def cast(self, Schema_target_schema, safe=None, options=None): # real signature unknown; restored from __doc__
        """
        Table.cast(self, Schema target_schema, safe=None, options=None)
        
                Cast table values to another schema.
        
                Parameters
                ----------
                target_schema : Schema
                    Schema to cast to, the names and order of fields must match.
                safe : bool, default True
                    Check for overflows or other unsafe conversions.
                options : CastOptions, default None
                    Additional checks pass by CastOptions
        
                Returns
                -------
                Table
        
                Examples
                --------
                >>> import pyarrow as pa
                >>> import pandas as pd
                >>> df = pd.DataFrame({'n_legs': [2, 4, 5, 100],
                ...                    'animals': ["Flamingo", "Horse", "Brittle stars", "Centipede"]})
                >>> table = pa.Table.from_pandas(df)
                >>> table.schema
                n_legs: int64
                animals: string
                -- schema metadata --
                pandas: '{"index_columns": [{"kind": "range", "name": null, "start": 0, ...
        
                Define new schema and cast table values:
        
                >>> my_schema = pa.schema([
                ...     pa.field('n_legs', pa.duration('s')),
                ...     pa.field('animals', pa.string())]
                ...     )
                >>> table.cast(target_schema=my_schema)
                pyarrow.Table
                n_legs: duration[s]
                animals: string
                ----
                n_legs: [[2,4,5,100]]
                animals: [["Flamingo","Horse","Brittle stars","Centipede"]]
        """
        pass

    def column(self, i): # real signature unknown; restored from __doc__
        """
        Table.column(self, i)
        
                Select a column by its column name, or numeric index.
        
                Parameters
                ----------
                i : int or string
                    The index or name of the column to retrieve.
        
                Returns
                -------
                ChunkedArray
        
                Examples
                --------
                >>> import pyarrow as pa
                >>> import pandas as pd
                >>> df = pd.DataFrame({'n_legs': [2, 4, 5, 100],
                ...                    'animals': ["Flamingo", "Horse", "Brittle stars", "Centipede"]})
                >>> table = pa.Table.from_pandas(df)
        
                Select a column by numeric index:
        
                >>> table.column(0)
                <pyarrow.lib.ChunkedArray object at ...>
                [
                  [
                    2,
                    4,
                    5,
                    100
                  ]
                ]
        
                Select a column by its name:
        
                >>> table.column("animals")
                <pyarrow.lib.ChunkedArray object at ...>
                [
                  [
                    "Flamingo",
                    "Horse",
                    "Brittle stars",
                    "Centipede"
                  ]
                ]
        """
        pass

    def combine_chunks(self, MemoryPool_memory_pool=None): # real signature unknown; restored from __doc__
        """
        Table.combine_chunks(self, MemoryPool memory_pool=None)
        
                Make a new table by combining the chunks this table has.
        
                All the underlying chunks in the ChunkedArray of each column are
                concatenated into zero or one chunk.
        
                Parameters
                ----------
                memory_pool : MemoryPool, default None
                    For memory allocations, if required, otherwise use default pool.
        
                Returns
                -------
                Table
        
                Examples
                --------
                >>> import pyarrow as pa
                >>> n_legs = pa.chunked_array([[2, 2, 4], [4, 5, 100]])
                >>> animals = pa.chunked_array([["Flamingo", "Parrot", "Dog"], ["Horse", "Brittle stars", "Centipede"]])
                >>> names = ["n_legs", "animals"]
                >>> table = pa.table([n_legs, animals], names=names)
                >>> table
                pyarrow.Table
                n_legs: int64
                animals: string
                ----
                n_legs: [[2,2,4],[4,5,100]]
                animals: [["Flamingo","Parrot","Dog"],["Horse","Brittle stars","Centipede"]]
                >>> table.combine_chunks()
                pyarrow.Table
                n_legs: int64
                animals: string
                ----
                n_legs: [[2,2,4,4,5,100]]
                animals: [["Flamingo","Parrot","Dog","Horse","Brittle stars","Centipede"]]
        """
        pass

    def drop(self, columns): # real signature unknown; restored from __doc__
        """
        Table.drop(self, columns)
        
                Drop one or more columns and return a new table.
        
                Parameters
                ----------
                columns : list of str
                    List of field names referencing existing columns.
        
                Raises
                ------
                KeyError
                    If any of the passed columns name are not existing.
        
                Returns
                -------
                Table
                    New table without the columns.
        
                Examples
                --------
                >>> import pyarrow as pa
                >>> import pandas as pd
                >>> df = pd.DataFrame({'n_legs': [2, 4, 5, 100],
                ...                    'animals': ["Flamingo", "Horse", "Brittle stars", "Centipede"]})
                >>> table = pa.Table.from_pandas(df)
        
                Drop one column:
        
                >>> table.drop(["animals"])
                pyarrow.Table
                n_legs: int64
                ----
                n_legs: [[2,4,5,100]]
        
                Drop more columns:
        
                >>> table.drop(["n_legs", "animals"])
                pyarrow.Table
                ...
                ----
        """
        pass

    def drop_null(self): # real signature unknown; restored from __doc__
        """
        Table.drop_null(self)
        
                Remove missing values from a Table.
                See :func:`pyarrow.compute.drop_null` for full usage.
        
                Examples
                --------
                >>> import pyarrow as pa
                >>> import pandas as pd
                >>> df = pd.DataFrame({'year': [None, 2022, 2019, 2021],
                ...                   'n_legs': [2, 4, 5, 100],
                ...                   'animals': ["Flamingo", "Horse", None, "Centipede"]})
                >>> table = pa.Table.from_pandas(df)
                >>> table.drop_null()
                pyarrow.Table
                year: double
                n_legs: int64
                animals: string
                ----
                year: [[2022,2021]]
                n_legs: [[4,100]]
                animals: [["Horse","Centipede"]]
        """
        pass

    def equals(self, Table_other, bool_check_metadata=False): # real signature unknown; restored from __doc__
        """
        Table.equals(self, Table other, bool check_metadata=False)
        
                Check if contents of two tables are equal.
        
                Parameters
                ----------
                other : pyarrow.Table
                    Table to compare against.
                check_metadata : bool, default False
                    Whether schema metadata equality should be checked as well.
        
                Returns
                -------
                bool
        
                Examples
                --------
                >>> import pyarrow as pa
                >>> n_legs = pa.array([2, 2, 4, 4, 5, 100])
                >>> animals = pa.array(["Flamingo", "Parrot", "Dog", "Horse", "Brittle stars", "Centipede"])
                >>> names=["n_legs", "animals"]
                >>> table = pa.Table.from_arrays([n_legs, animals], names=names)
                >>> table_0 = pa.Table.from_arrays([])
                >>> table_1 = pa.Table.from_arrays([n_legs, animals],
                ...                                 names=names,
                ...                                 metadata={"n_legs": "Number of legs per animal"})
                >>> table.equals(table)
                True
                >>> table.equals(table_0)
                False
                >>> table.equals(table_1)
                True
                >>> table.equals(table_1, check_metadata=True)
                False
        """
        pass

    def field(self, i): # real signature unknown; restored from __doc__
        """
        Table.field(self, i)
        
                Select a schema field by its column name or numeric index.
        
                Parameters
                ----------
                i : int or string
                    The index or name of the field to retrieve.
        
                Returns
                -------
                Field
        
                Examples
                --------
                >>> import pyarrow as pa
                >>> import pandas as pd
                >>> df = pd.DataFrame({'n_legs': [2, 4, 5, 100],
                ...                    'animals': ["Flamingo", "Horse", "Brittle stars", "Centipede"]})
                >>> table = pa.Table.from_pandas(df)
                >>> table.field(0)
                pyarrow.Field<n_legs: int64>
                >>> table.field(1)
                pyarrow.Field<animals: string>
        """
        pass

    def filter(self, mask, null_selection_behavior=None): # real signature unknown; restored from __doc__
        """
        Table.filter(self, mask, null_selection_behavior=u'drop')
        
                Select rows from the table.
        
                The Table can be filtered based on a mask, which will be passed to
                :func:`pyarrow.compute.filter` to perform the filtering, or it can
                be filtered through a boolean :class:`.Expression`
        
                Parameters
                ----------
                mask : Array or array-like or .Expression
                    The boolean mask or the :class:`.Expression` to filter the table with.
                null_selection_behavior : str, default "drop"
                    How nulls in the mask should be handled, does nothing if
                    an :class:`.Expression` is used.
        
                Returns
                -------
                filtered : Table
                    A table of the same schema, with only the rows selected
                    by applied filtering
        
                Examples
                --------
                >>> import pyarrow as pa
                >>> import pandas as pd
                >>> df = pd.DataFrame({'year': [2020, 2022, 2019, 2021],
                ...                    'n_legs': [2, 4, 5, 100],
                ...                    'animals': ["Flamingo", "Horse", "Brittle stars", "Centipede"]})
                >>> table = pa.Table.from_pandas(df)
        
                Define an expression and select rows:
        
                >>> import pyarrow.compute as pc
                >>> expr = pc.field("year") <= 2020
                >>> table.filter(expr)
                pyarrow.Table
                year: int64
                n_legs: int64
                animals: string
                ----
                year: [[2020,2019]]
                n_legs: [[2,5]]
                animals: [["Flamingo","Brittle stars"]]
        
                Define a mask and select rows:
        
                >>> mask=[True, True, False, None]
                >>> table.filter(mask)
                pyarrow.Table
                year: int64
                n_legs: int64
                animals: string
                ----
                year: [[2020,2022]]
                n_legs: [[2,4]]
                animals: [["Flamingo","Horse"]]
                >>> table.filter(mask, null_selection_behavior='emit_null')
                pyarrow.Table
                year: int64
                n_legs: int64
                animals: string
                ----
                year: [[2020,2022,null]]
                n_legs: [[2,4,null]]
                animals: [["Flamingo","Horse",null]]
        """
        pass

    def flatten(self, MemoryPool_memory_pool=None): # real signature unknown; restored from __doc__
        """
        Table.flatten(self, MemoryPool memory_pool=None)
        
                Flatten this Table.
        
                Each column with a struct type is flattened
                into one column per struct field.  Other columns are left unchanged.
        
                Parameters
                ----------
                memory_pool : MemoryPool, default None
                    For memory allocations, if required, otherwise use default pool
        
                Returns
                -------
                Table
        
                Examples
                --------
                >>> import pyarrow as pa
                >>> struct = pa.array([{'n_legs': 2, 'animals': 'Parrot'},
                ...                    {'year': 2022, 'n_legs': 4}])
                >>> month = pa.array([4, 6])
                >>> table = pa.Table.from_arrays([struct,month],
                ...                              names = ["a", "month"])
                >>> table
                pyarrow.Table
                a: struct<animals: string, n_legs: int64, year: int64>
                  child 0, animals: string
                  child 1, n_legs: int64
                  child 2, year: int64
                month: int64
                ----
                a: [
                  -- is_valid: all not null
                  -- child 0 type: string
                ["Parrot",null]
                  -- child 1 type: int64
                [2,4]
                  -- child 2 type: int64
                [null,2022]]
                month: [[4,6]]
        
                Flatten the columns with struct field:
        
                >>> table.flatten()
                pyarrow.Table
                a.animals: string
                a.n_legs: int64
                a.year: int64
                month: int64
                ----
                a.animals: [["Parrot",null]]
                a.n_legs: [[2,4]]
                a.year: [[null,2022]]
                month: [[4,6]]
        """
        pass

    def from_arrays(self, arrays, names=None, schema=None, metadata=None): # real signature unknown; restored from __doc__
        """
        Table.from_arrays(arrays, names=None, schema=None, metadata=None)
        
                Construct a Table from Arrow arrays.
        
                Parameters
                ----------
                arrays : list of pyarrow.Array or pyarrow.ChunkedArray
                    Equal-length arrays that should form the table.
                names : list of str, optional
                    Names for the table columns. If not passed, schema must be passed.
                schema : Schema, default None
                    Schema for the created table. If not passed, names must be passed.
                metadata : dict or Mapping, default None
                    Optional metadata for the schema (if inferred).
        
                Returns
                -------
                Table
        
                Examples
                --------
                >>> import pyarrow as pa
                >>> n_legs = pa.array([2, 4, 5, 100])
                >>> animals = pa.array(["Flamingo", "Horse", "Brittle stars", "Centipede"])
                >>> names = ["n_legs", "animals"]
        
                Construct a Table from arrays:
        
                >>> pa.Table.from_arrays([n_legs, animals], names=names)
                pyarrow.Table
                n_legs: int64
                animals: string
                ----
                n_legs: [[2,4,5,100]]
                animals: [["Flamingo","Horse","Brittle stars","Centipede"]]
        
                Construct a Table from arrays with metadata:
        
                >>> my_metadata={"n_legs": "Number of legs per animal"}
                >>> pa.Table.from_arrays([n_legs, animals],
                ...                       names=names,
                ...                       metadata=my_metadata)
                pyarrow.Table
                n_legs: int64
                animals: string
                ----
                n_legs: [[2,4,5,100]]
                animals: [["Flamingo","Horse","Brittle stars","Centipede"]]
                >>> pa.Table.from_arrays([n_legs, animals],
                ...                       names=names,
                ...                       metadata=my_metadata).schema
                n_legs: int64
                animals: string
                -- schema metadata --
                n_legs: 'Number of legs per animal'
        
                Construct a Table from arrays with pyarrow schema:
        
                >>> my_schema = pa.schema([
                ...     pa.field('n_legs', pa.int64()),
                ...     pa.field('animals', pa.string())],
                ...     metadata={"animals": "Name of the animal species"})
                >>> pa.Table.from_arrays([n_legs, animals],
                ...                       schema=my_schema)
                pyarrow.Table
                n_legs: int64
                animals: string
                ----
                n_legs: [[2,4,5,100]]
                animals: [["Flamingo","Horse","Brittle stars","Centipede"]]
                >>> pa.Table.from_arrays([n_legs, animals],
                ...                       schema=my_schema).schema
                n_legs: int64
                animals: string
                -- schema metadata --
                animals: 'Name of the animal species'
        """
        pass

    def from_batches(self, batches, Schema_schema=None): # real signature unknown; restored from __doc__
        """
        Table.from_batches(batches, Schema schema=None)
        
                Construct a Table from a sequence or iterator of Arrow RecordBatches.
        
                Parameters
                ----------
                batches : sequence or iterator of RecordBatch
                    Sequence of RecordBatch to be converted, all schemas must be equal.
                schema : Schema, default None
                    If not passed, will be inferred from the first RecordBatch.
        
                Returns
                -------
                Table
        
                Examples
                --------
                >>> import pyarrow as pa
                >>> n_legs = pa.array([2, 4, 5, 100])
                >>> animals = pa.array(["Flamingo", "Horse", "Brittle stars", "Centipede"])
                >>> names = ["n_legs", "animals"]
                >>> batch = pa.record_batch([n_legs, animals], names=names)
                >>> batch.to_pandas()
                   n_legs        animals
                0       2       Flamingo
                1       4          Horse
                2       5  Brittle stars
                3     100      Centipede
        
                Construct a Table from a RecordBatch:
        
                >>> pa.Table.from_batches([batch])
                pyarrow.Table
                n_legs: int64
                animals: string
                ----
                n_legs: [[2,4,5,100]]
                animals: [["Flamingo","Horse","Brittle stars","Centipede"]]
        
                Construct a Table from a sequence of RecordBatches:
        
                >>> pa.Table.from_batches([batch, batch])
                pyarrow.Table
                n_legs: int64
                animals: string
                ----
                n_legs: [[2,4,5,100],[2,4,5,100]]
                animals: [["Flamingo","Horse","Brittle stars","Centipede"],["Flamingo","Horse","Brittle stars","Centipede"]]
        """
        pass

    @classmethod
    def from_pandas(cls, type_cls, df, Schema_schema=None, preserve_index=None, nthreads=None, columns=None, bool_safe=True): # real signature unknown; restored from __doc__
        """
        Table.from_pandas(type cls, df, Schema schema=None, preserve_index=None, nthreads=None, columns=None, bool safe=True)
        
                Convert pandas.DataFrame to an Arrow Table.
        
                The column types in the resulting Arrow Table are inferred from the
                dtypes of the pandas.Series in the DataFrame. In the case of non-object
                Series, the NumPy dtype is translated to its Arrow equivalent. In the
                case of `object`, we need to guess the datatype by looking at the
                Python objects in this Series.
        
                Be aware that Series of the `object` dtype don't carry enough
                information to always lead to a meaningful Arrow type. In the case that
                we cannot infer a type, e.g. because the DataFrame is of length 0 or
                the Series only contains None/nan objects, the type is set to
                null. This behavior can be avoided by constructing an explicit schema
                and passing it to this function.
        
                Parameters
                ----------
                df : pandas.DataFrame
                schema : pyarrow.Schema, optional
                    The expected schema of the Arrow Table. This can be used to
                    indicate the type of columns if we cannot infer it automatically.
                    If passed, the output will have exactly this schema. Columns
                    specified in the schema that are not found in the DataFrame columns
                    or its index will raise an error. Additional columns or index
                    levels in the DataFrame which are not specified in the schema will
                    be ignored.
                preserve_index : bool, optional
                    Whether to store the index as an additional column in the resulting
                    ``Table``. The default of None will store the index as a column,
                    except for RangeIndex which is stored as metadata only. Use
                    ``preserve_index=True`` to force it to be stored as a column.
                nthreads : int, default None
                    If greater than 1, convert columns to Arrow in parallel using
                    indicated number of threads. By default, this follows
                    :func:`pyarrow.cpu_count` (may use up to system CPU count threads).
                columns : list, optional
                   List of column to be converted. If None, use all columns.
                safe : bool, default True
                   Check for overflows or other unsafe conversions.
        
                Returns
                -------
                Table
        
                Examples
                --------
                >>> import pyarrow as pa
                >>> import pandas as pd
                >>> df = pd.DataFrame({'n_legs': [2, 4, 5, 100],
                ...                    'animals': ["Flamingo", "Horse", "Brittle stars", "Centipede"]})
                >>> pa.Table.from_pandas(df)
                pyarrow.Table
                n_legs: int64
                animals: string
                ----
                n_legs: [[2,4,5,100]]
                animals: [["Flamingo","Horse","Brittle stars","Centipede"]]
        """
        pass

    def from_pydict(self, mapping, schema=None, metadata=None): # real signature unknown; restored from __doc__
        """
        Table.from_pydict(mapping, schema=None, metadata=None)
        
                Construct a Table from Arrow arrays or columns.
        
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
                Table
        
                Examples
                --------
                >>> import pyarrow as pa
                >>> n_legs = pa.array([2, 4, 5, 100])
                >>> animals = pa.array(["Flamingo", "Horse", "Brittle stars", "Centipede"])
                >>> pydict = {'n_legs': n_legs, 'animals': animals}
        
                Construct a Table from a dictionary of arrays:
        
                >>> pa.Table.from_pydict(pydict)
                pyarrow.Table
                n_legs: int64
                animals: string
                ----
                n_legs: [[2,4,5,100]]
                animals: [["Flamingo","Horse","Brittle stars","Centipede"]]
                >>> pa.Table.from_pydict(pydict).schema
                n_legs: int64
                animals: string
        
                Construct a Table from a dictionary of arrays with metadata:
        
                >>> my_metadata={"n_legs": "Number of legs per animal"}
                >>> pa.Table.from_pydict(pydict, metadata=my_metadata).schema
                n_legs: int64
                animals: string
                -- schema metadata --
                n_legs: 'Number of legs per animal'
        """
        pass

    def from_pylist(self, mapping, schema=None, metadata=None): # real signature unknown; restored from __doc__
        """
        Table.from_pylist(mapping, schema=None, metadata=None)
        
                Construct a Table from list of rows / dictionaries.
        
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
                Table
        
                Examples
                --------
                >>> import pyarrow as pa
                >>> n_legs = pa.array([2, 4, 5, 100])
                >>> animals = pa.array(["Flamingo", "Horse", "Brittle stars", "Centipede"])
                >>> pylist = [{'n_legs': 2, 'animals': 'Flamingo'},
                ...           {'year': 2021, 'animals': 'Centipede'}]
        
                Construct a Table from a list of rows:
        
                >>> pa.Table.from_pylist(pylist)
                pyarrow.Table
                n_legs: int64
                animals: string
                ----
                n_legs: [[2,null]]
                animals: [["Flamingo","Centipede"]]
        
                Construct a Table from a list of rows with pyarrow schema:
        
                >>> my_schema = pa.schema([
                ...     pa.field('year', pa.int64()),
                ...     pa.field('n_legs', pa.int64()),
                ...     pa.field('animals', pa.string())],
                ...     metadata={"year": "Year of entry"})
                >>> pa.Table.from_pylist(pylist, schema=my_schema).schema
                year: int64
                n_legs: int64
                animals: string
                -- schema metadata --
                year: 'Year of entry'
        """
        pass

    def get_total_buffer_size(self): # real signature unknown; restored from __doc__
        """
        Table.get_total_buffer_size(self)
        
                The sum of bytes in each buffer referenced by the table.
        
                An array may only reference a portion of a buffer.
                This method will overestimate in this case and return the
                byte size of the entire buffer.
        
                If a buffer is referenced multiple times then it will
                only be counted once.
        
                Examples
                --------
                >>> import pyarrow as pa
                >>> import pandas as pd
                >>> df = pd.DataFrame({'n_legs': [None, 4, 5, None],
                ...                    'animals': ["Flamingo", "Horse", None, "Centipede"]})
                >>> table = pa.Table.from_pandas(df)
                >>> table.get_total_buffer_size()
                76
        """
        pass

    def group_by(self, keys): # real signature unknown; restored from __doc__
        """
        Table.group_by(self, keys)
        Declare a grouping over the columns of the table.
        
                Resulting grouping can then be used to perform aggregations
                with a subsequent ``aggregate()`` method.
        
                Parameters
                ----------
                keys : str or list[str]
                    Name of the columns that should be used as the grouping key.
        
                Returns
                -------
                TableGroupBy
        
                See Also
                --------
                TableGroupBy.aggregate
        
                Examples
                --------
                >>> import pandas as pd
                >>> import pyarrow as pa
                >>> df = pd.DataFrame({'year': [2020, 2022, 2021, 2022, 2019, 2021],
                ...                    'n_legs': [2, 2, 4, 4, 5, 100],
                ...                    'animal': ["Flamingo", "Parrot", "Dog", "Horse",
                ...                    "Brittle stars", "Centipede"]})
                >>> table = pa.Table.from_pandas(df)
                >>> table.group_by('year').aggregate([('n_legs', 'sum')])
                pyarrow.Table
                n_legs_sum: int64
                year: int64
                ----
                n_legs_sum: [[2,6,104,5]]
                year: [[2020,2022,2021,2019]]
        """
        pass

    def itercolumns(self): # real signature unknown; restored from __doc__
        """
        Table.itercolumns(self)
        
                Iterator over all columns in their numerical order.
        
                Yields
                ------
                ChunkedArray
        
                Examples
                --------
                >>> import pyarrow as pa
                >>> import pandas as pd
                >>> df = pd.DataFrame({'n_legs': [None, 4, 5, None],
                ...                    'animals': ["Flamingo", "Horse", None, "Centipede"]})
                >>> table = pa.Table.from_pandas(df)
                >>> for i in table.itercolumns():
                ...     print(i.null_count)
                ...
                2
                1
        """
        pass

    def join(self, right_table, keys, right_keys=None, join_type=None, left_suffix=None, right_suffix=None, coalesce_keys=True, use_threads=True): # real signature unknown; restored from __doc__
        """
        Table.join(self, right_table, keys, right_keys=None, join_type=u'left outer', left_suffix=None, right_suffix=None, coalesce_keys=True, use_threads=True)
        
                Perform a join between this table and another one.
        
                Result of the join will be a new Table, where further
                operations can be applied.
        
                Parameters
                ----------
                right_table : Table
                    The table to join to the current one, acting as the right table
                    in the join operation.
                keys : str or list[str]
                    The columns from current table that should be used as keys
                    of the join operation left side.
                right_keys : str or list[str], default None
                    The columns from the right_table that should be used as keys
                    on the join operation right side.
                    When ``None`` use the same key names as the left table.
                join_type : str, default "left outer"
                    The kind of join that should be performed, one of
                    ("left semi", "right semi", "left anti", "right anti",
                    "inner", "left outer", "right outer", "full outer")
                left_suffix : str, default None
                    Which suffix to add to left column names. This prevents confusion
                    when the columns in left and right tables have colliding names.
                right_suffix : str, default None
                    Which suffix to add to the right column names. This prevents confusion
                    when the columns in left and right tables have colliding names.
                coalesce_keys : bool, default True
                    If the duplicated keys should be omitted from one of the sides
                    in the join result.
                use_threads : bool, default True
                    Whether to use multithreading or not.
        
                Returns
                -------
                Table
        
                Examples
                --------
                >>> import pandas as pd
                >>> import pyarrow as pa
                >>> df1 = pd.DataFrame({'id': [1, 2, 3],
                ...                     'year': [2020, 2022, 2019]})
                >>> df2 = pd.DataFrame({'id': [3, 4],
                ...                     'n_legs': [5, 100],
                ...                     'animal': ["Brittle stars", "Centipede"]})
                >>> t1 = pa.Table.from_pandas(df1)
                >>> t2 = pa.Table.from_pandas(df2)
        
                Left outer join:
        
                >>> t1.join(t2, 'id').combine_chunks().sort_by('year')
                pyarrow.Table
                id: int64
                year: int64
                n_legs: int64
                animal: string
                ----
                id: [[3,1,2]]
                year: [[2019,2020,2022]]
                n_legs: [[5,null,null]]
                animal: [["Brittle stars",null,null]]
        
                Full outer join:
        
                >>> t1.join(t2, 'id', join_type="full outer").combine_chunks().sort_by('year')
                pyarrow.Table
                id: int64
                year: int64
                n_legs: int64
                animal: string
                ----
                id: [[3,1,2,4]]
                year: [[2019,2020,2022,null]]
                n_legs: [[5,null,null,100]]
                animal: [["Brittle stars",null,null,"Centipede"]]
        
                Right outer join:
        
                >>> t1.join(t2, 'id', join_type="right outer").combine_chunks().sort_by('year')
                pyarrow.Table
                year: int64
                id: int64
                n_legs: int64
                animal: string
                ----
                year: [[2019,null]]
                id: [[3,4]]
                n_legs: [[5,100]]
                animal: [["Brittle stars","Centipede"]]
        
                Right anti join
        
                >>> t1.join(t2, 'id', join_type="right anti")
                pyarrow.Table
                id: int64
                n_legs: int64
                animal: string
                ----
                id: [[4]]
                n_legs: [[100]]
                animal: [["Centipede"]]
        """
        pass

    def remove_column(self, int_i): # real signature unknown; restored from __doc__
        """
        Table.remove_column(self, int i)
        
                Create new Table with the indicated column removed.
        
                Parameters
                ----------
                i : int
                    Index of column to remove.
        
                Returns
                -------
                Table
                    New table without the column.
        
                Examples
                --------
                >>> import pyarrow as pa
                >>> import pandas as pd
                >>> df = pd.DataFrame({'n_legs': [2, 4, 5, 100],
                ...                    'animals': ["Flamingo", "Horse", "Brittle stars", "Centipede"]})
                >>> table = pa.Table.from_pandas(df)
                >>> table.remove_column(1)
                pyarrow.Table
                n_legs: int64
                ----
                n_legs: [[2,4,5,100]]
        """
        pass

    def rename_columns(self, names): # real signature unknown; restored from __doc__
        """
        Table.rename_columns(self, names)
        
                Create new table with columns renamed to provided names.
        
                Parameters
                ----------
                names : list of str
                    List of new column names.
        
                Returns
                -------
                Table
        
                Examples
                --------
                >>> import pyarrow as pa
                >>> import pandas as pd
                >>> df = pd.DataFrame({'n_legs': [2, 4, 5, 100],
                ...                    'animals': ["Flamingo", "Horse", "Brittle stars", "Centipede"]})
                >>> table = pa.Table.from_pandas(df)
                >>> new_names = ["n", "name"]
                >>> table.rename_columns(new_names)
                pyarrow.Table
                n: int64
                name: string
                ----
                n: [[2,4,5,100]]
                name: [["Flamingo","Horse","Brittle stars","Centipede"]]
        """
        pass

    def replace_schema_metadata(self, metadata=None): # real signature unknown; restored from __doc__
        """
        Table.replace_schema_metadata(self, metadata=None)
        
                Create shallow copy of table by replacing schema
                key-value metadata with the indicated new metadata (which may be None),
                which deletes any existing metadata.
        
                Parameters
                ----------
                metadata : dict, default None
        
                Returns
                -------
                Table
        
                Examples
                --------
                >>> import pyarrow as pa
                >>> import pandas as pd
                >>> df = pd.DataFrame({'year': [2020, 2022, 2019, 2021],
                ...                    'n_legs': [2, 4, 5, 100],
                ...                    'animals': ["Flamingo", "Horse", "Brittle stars", "Centipede"]})
                >>> table = pa.Table.from_pandas(df)
        
                Constructing a Table with pyarrow schema and metadata:
        
                >>> my_schema = pa.schema([
                ...     pa.field('n_legs', pa.int64()),
                ...     pa.field('animals', pa.string())],
                ...     metadata={"n_legs": "Number of legs per animal"})
                >>> table= pa.table(df, my_schema)
                >>> table.schema
                n_legs: int64
                animals: string
                -- schema metadata --
                n_legs: 'Number of legs per animal'
                pandas: ...
        
                Create a shallow copy of a Table with deleted schema metadata:
        
                >>> table.replace_schema_metadata().schema
                n_legs: int64
                animals: string
        
                Create a shallow copy of a Table with new schema metadata:
        
                >>> metadata={"animals": "Which animal"}
                >>> table.replace_schema_metadata(metadata = metadata).schema
                n_legs: int64
                animals: string
                -- schema metadata --
                animals: 'Which animal'
        """
        pass

    def select(self, columns): # real signature unknown; restored from __doc__
        """
        Table.select(self, columns)
        
                Select columns of the Table.
        
                Returns a new Table with the specified columns, and metadata
                preserved.
        
                Parameters
                ----------
                columns : list-like
                    The column names or integer indices to select.
        
                Returns
                -------
                Table
        
                Examples
                --------
                >>> import pyarrow as pa
                >>> import pandas as pd
                >>> df = pd.DataFrame({'year': [2020, 2022, 2019, 2021],
                ...                    'n_legs': [2, 4, 5, 100],
                ...                    'animals': ["Flamingo", "Horse", "Brittle stars", "Centipede"]})
                >>> table = pa.Table.from_pandas(df)
                >>> table.select([0,1])
                pyarrow.Table
                year: int64
                n_legs: int64
                ----
                year: [[2020,2022,2019,2021]]
                n_legs: [[2,4,5,100]]
                >>> table.select(["year"])
                pyarrow.Table
                year: int64
                ----
                year: [[2020,2022,2019,2021]]
        """
        pass

    def set_column(self, int_i, field_, column): # real signature unknown; restored from __doc__
        """
        Table.set_column(self, int i, field_, column)
        
                Replace column in Table at position.
        
                Parameters
                ----------
                i : int
                    Index to place the column at.
                field_ : str or Field
                    If a string is passed then the type is deduced from the column
                    data.
                column : Array, list of Array, or values coercible to arrays
                    Column data.
        
                Returns
                -------
                Table
                    New table with the passed column set.
        
                Examples
                --------
                >>> import pyarrow as pa
                >>> import pandas as pd
                >>> df = pd.DataFrame({'n_legs': [2, 4, 5, 100],
                ...                    'animals': ["Flamingo", "Horse", "Brittle stars", "Centipede"]})
                >>> table = pa.Table.from_pandas(df)
        
                Replace a column:
        
                >>> year = [2021, 2022, 2019, 2021]
                >>> table.set_column(1,'year', [year])
                pyarrow.Table
                n_legs: int64
                year: int64
                ----
                n_legs: [[2,4,5,100]]
                year: [[2021,2022,2019,2021]]
        """
        pass

    def slice(self, offset=0, length=None): # real signature unknown; restored from __doc__
        """
        Table.slice(self, offset=0, length=None)
        
                Compute zero-copy slice of this Table.
        
                Parameters
                ----------
                offset : int, default 0
                    Offset from start of table to slice.
                length : int, default None
                    Length of slice (default is until end of table starting from
                    offset).
        
                Returns
                -------
                Table
        
                Examples
                --------
                >>> import pyarrow as pa
                >>> import pandas as pd
                >>> df = pd.DataFrame({'year': [2020, 2022, 2019, 2021],
                ...                    'n_legs': [2, 4, 5, 100],
                ...                    'animals': ["Flamingo", "Horse", "Brittle stars", "Centipede"]})
                >>> table = pa.Table.from_pandas(df)
                >>> table.slice(length=3)
                pyarrow.Table
                year: int64
                n_legs: int64
                animals: string
                ----
                year: [[2020,2022,2019]]
                n_legs: [[2,4,5]]
                animals: [["Flamingo","Horse","Brittle stars"]]
                >>> table.slice(offset=2)
                pyarrow.Table
                year: int64
                n_legs: int64
                animals: string
                ----
                year: [[2019,2021]]
                n_legs: [[5,100]]
                animals: [["Brittle stars","Centipede"]]
                >>> table.slice(offset=2, length=1)
                pyarrow.Table
                year: int64
                n_legs: int64
                animals: string
                ----
                year: [[2019]]
                n_legs: [[5]]
                animals: [["Brittle stars"]]
        """
        pass

    def sort_by(self, sorting, **kwargs): # real signature unknown; restored from __doc__
        """
        Table.sort_by(self, sorting, **kwargs)
        
                Sort the table by one or multiple columns.
        
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
                Table
                    A new table sorted according to the sort keys.
        
                Examples
                --------
                >>> import pandas as pd
                >>> import pyarrow as pa
                >>> df = pd.DataFrame({'year': [2020, 2022, 2021, 2022, 2019, 2021],
                ...                    'n_legs': [2, 2, 4, 4, 5, 100],
                ...                    'animal': ["Flamingo", "Parrot", "Dog", "Horse",
                ...                    "Brittle stars", "Centipede"]})
                >>> table = pa.Table.from_pandas(df)
                >>> table.sort_by('animal')
                pyarrow.Table
                year: int64
                n_legs: int64
                animal: string
                ----
                year: [[2019,2021,2021,2020,2022,2022]]
                n_legs: [[5,100,4,2,4,2]]
                animal: [["Brittle stars","Centipede","Dog","Flamingo","Horse","Parrot"]]
        """
        pass

    def take(self, indices): # real signature unknown; restored from __doc__
        """
        Table.take(self, indices)
        
                Select rows from the table.
        
                See :func:`pyarrow.compute.take` for full usage.
        
                Parameters
                ----------
                indices : Array or array-like
                    The indices in the table whose rows will be returned.
        
                Returns
                -------
                taken : Table
                    A table with the same schema, containing the taken rows.
        
                Examples
                --------
                >>> import pyarrow as pa
                >>> import pandas as pd
                >>> df = pd.DataFrame({'year': [2020, 2022, 2019, 2021],
                ...                    'n_legs': [2, 4, 5, 100],
                ...                    'animals': ["Flamingo", "Horse", "Brittle stars", "Centipede"]})
                >>> table = pa.Table.from_pandas(df)
                >>> table.take([1,3])
                pyarrow.Table
                year: int64
                n_legs: int64
                animals: string
                ----
                year: [[2022,2021]]
                n_legs: [[4,100]]
                animals: [["Horse","Centipede"]]
        """
        pass

    def to_batches(self, max_chunksize=None): # real signature unknown; restored from __doc__
        """
        Table.to_batches(self, max_chunksize=None)
        
                Convert Table to a list of RecordBatch objects.
        
                Note that this method is zero-copy, it merely exposes the same data
                under a different API.
        
                Parameters
                ----------
                max_chunksize : int, default None
                    Maximum size for RecordBatch chunks. Individual chunks may be
                    smaller depending on the chunk layout of individual columns.
        
                Returns
                -------
                list[RecordBatch]
        
                Examples
                --------
                >>> import pyarrow as pa
                >>> import pandas as pd
                >>> df = pd.DataFrame({'n_legs': [2, 4, 5, 100],
                ...                    'animals': ["Flamingo", "Horse", "Brittle stars", "Centipede"]})
                >>> table = pa.Table.from_pandas(df)
        
                Convert a Table to a RecordBatch:
        
                >>> table.to_batches()[0].to_pandas()
                   n_legs        animals
                0       2       Flamingo
                1       4          Horse
                2       5  Brittle stars
                3     100      Centipede
        
                Convert a Table to a list of RecordBatches:
        
                >>> table.to_batches(max_chunksize=2)[0].to_pandas()
                   n_legs   animals
                0       2  Flamingo
                1       4     Horse
                >>> table.to_batches(max_chunksize=2)[1].to_pandas()
                   n_legs        animals
                0       5  Brittle stars
                1     100      Centipede
        """
        pass

    def to_pydict(self): # real signature unknown; restored from __doc__
        """
        Table.to_pydict(self)
        
                Convert the Table to a dict or OrderedDict.
        
                Returns
                -------
                dict
        
                Examples
                --------
                >>> import pyarrow as pa
                >>> import pandas as pd
                >>> df = pd.DataFrame({'n_legs': [2, 4, 5, 100],
                ...                    'animals': ["Flamingo", "Horse", "Brittle stars", "Centipede"]})
                >>> table = pa.Table.from_pandas(df)
                >>> table.to_pydict()
                {'n_legs': [2, 4, 5, 100], 'animals': ['Flamingo', 'Horse', 'Brittle stars', 'Centipede']}
        """
        pass

    def to_pylist(self): # real signature unknown; restored from __doc__
        """
        Table.to_pylist(self)
        
                Convert the Table to a list of rows / dictionaries.
        
                Returns
                -------
                list
        
                Examples
                --------
                >>> import pyarrow as pa
                >>> import pandas as pd
                >>> df = pd.DataFrame({'n_legs': [2, 4, 5, 100],
                ...                    'animals': ["Flamingo", "Horse", "Brittle stars", "Centipede"]})
                >>> table = pa.Table.from_pandas(df)
                >>> table.to_pylist()
                [{'n_legs': 2, 'animals': 'Flamingo'}, {'n_legs': 4, 'animals': 'Horse'}, ...
        """
        pass

    def to_reader(self, max_chunksize=None): # real signature unknown; restored from __doc__
        """
        Table.to_reader(self, max_chunksize=None)
        
                Convert the Table to a RecordBatchReader.
        
                Note that this method is zero-copy, it merely exposes the same data
                under a different API.
        
                Parameters
                ----------
                max_chunksize : int, default None
                    Maximum size for RecordBatch chunks. Individual chunks may be
                    smaller depending on the chunk layout of individual columns.
        
                Returns
                -------
                RecordBatchReader
        
                Examples
                --------
                >>> import pyarrow as pa
                >>> import pandas as pd
                >>> df = pd.DataFrame({'n_legs': [2, 4, 5, 100],
                ...                    'animals': ["Flamingo", "Horse", "Brittle stars", "Centipede"]})
                >>> table = pa.Table.from_pandas(df)
        
                Convert a Table to a RecordBatchReader:
        
                >>> table.to_reader()
                <pyarrow.lib.RecordBatchReader object at ...>
        
                >>> reader = table.to_reader()
                >>> reader.schema
                n_legs: int64
                animals: string
                -- schema metadata --
                pandas: '{"index_columns": [{"kind": "range", "name": null, "start": 0, ...
                >>> reader.read_all()
                pyarrow.Table
                n_legs: int64
                animals: string
                ----
                n_legs: [[2,4,5,100]]
                animals: [["Flamingo","Horse","Brittle stars","Centipede"]]
        """
        pass

    def to_string(self, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        Table.to_string(self, *, show_metadata=False, preview_cols=0)
        
                Return human-readable string representation of Table.
        
                Parameters
                ----------
                show_metadata : bool, default False
                    Display Field-level and Schema-level KeyValueMetadata.
                preview_cols : int, default 0
                    Display values of the columns for the first N columns.
        
                Returns
                -------
                str
        """
        pass

    def unify_dictionaries(self, MemoryPool_memory_pool=None): # real signature unknown; restored from __doc__
        """
        Table.unify_dictionaries(self, MemoryPool memory_pool=None)
        
                Unify dictionaries across all chunks.
        
                This method returns an equivalent table, but where all chunks of
                each column share the same dictionary values.  Dictionary indices
                are transposed accordingly.
        
                Columns without dictionaries are returned unchanged.
        
                Parameters
                ----------
                memory_pool : MemoryPool, default None
                    For memory allocations, if required, otherwise use default pool
        
                Returns
                -------
                Table
        
                Examples
                --------
                >>> import pyarrow as pa
                >>> arr_1 = pa.array(["Flamingo", "Parot", "Dog"]).dictionary_encode()
                >>> arr_2 = pa.array(["Horse", "Brittle stars", "Centipede"]).dictionary_encode()
                >>> c_arr = pa.chunked_array([arr_1, arr_2])
                >>> table = pa.table([c_arr], names=["animals"])
                >>> table
                pyarrow.Table
                animals: dictionary<values=string, indices=int32, ordered=0>
                ----
                animals: [  -- dictionary:
                ["Flamingo","Parot","Dog"]  -- indices:
                [0,1,2],  -- dictionary:
                ["Horse","Brittle stars","Centipede"]  -- indices:
                [0,1,2]]
        
                Unify dictionaries across both chunks:
        
                >>> table.unify_dictionaries()
                pyarrow.Table
                animals: dictionary<values=string, indices=int32, ordered=0>
                ----
                animals: [  -- dictionary:
                ["Flamingo","Parot","Dog","Horse","Brittle stars","Centipede"]  -- indices:
                [0,1,2],  -- dictionary:
                ["Flamingo","Parot","Dog","Horse","Brittle stars","Centipede"]  -- indices:
                [3,4,5]]
        """
        pass

    def validate(self, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        Table.validate(self, *, full=False)
        
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
        Table._column(self, int i)
        
                Select a column by its numeric index.
        
                Parameters
                ----------
                i : int
                    The index of the column to retrieve.
        
                Returns
                -------
                ChunkedArray
        """
        pass

    def _ensure_integer_index(self, i): # real signature unknown; restored from __doc__
        """
        Table._ensure_integer_index(self, i)
        
                Ensure integer index (convert string column name to integer if needed).
        """
        pass

    def _to_pandas(self, options, categories=None, ignore_metadata=False, types_mapper=None): # real signature unknown; restored from __doc__
        """ Table._to_pandas(self, options, categories=None, ignore_metadata=False, types_mapper=None) """
        pass

    def __dataframe__(self, nan_as_null=False, allow_copy=True): # real signature unknown; restored from __doc__
        """
        Table.__dataframe__(self, nan_as_null: bool = False, allow_copy: bool = True)
        
                Return the dataframe interchange object implementing the interchange protocol.
                Parameters
                ----------
                nan_as_null : bool, default False
                    Whether to tell the DataFrame to overwrite null values in the data
                    with ``NaN`` (or ``NaT``).
                allow_copy : bool, default True
                    Whether to allow memory copying when exporting. If set to False
                    it would cause non-zero-copy exports to fail.
                Returns
                -------
                DataFrame interchange object
                    The object which consuming library can use to ingress the dataframe.
                Notes
                -----
                Details on the interchange protocol:
                https://data-apis.org/dataframe-protocol/latest/index.html
                `nan_as_null` currently has no effect; once support for nullable extension
                dtypes is added, this value should be propagated to columns.
        """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __getitem__(self, *args, **kwargs): # real signature unknown
        """
        Slice or return column at given index or column name.
        
                Parameters
                ----------
                key : integer, str, or slice
                    Slices with step not equal to 1 (or None) will produce a copy
                    rather than a zero-copy view.
        
                Returns
                -------
                ChunkedArray (index/column) or Table (slice)
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
        """ Table.__reduce__(self) """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __sizeof__(self): # real signature unknown; restored from __doc__
        """ Table.__sizeof__(self) """
        pass

    columns = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        List of all columns in numerical order.

        Returns
        -------
        list of ChunkedArray

        Examples
        --------
        >>> import pyarrow as pa
        >>> import pandas as pd
        >>> df = pd.DataFrame({'n_legs': [None, 4, 5, None],
        ...                    'animals': ["Flamingo", "Horse", None, "Centipede"]})
        >>> table = pa.Table.from_pandas(df)
        >>> table.columns
        [<pyarrow.lib.ChunkedArray object at ...>
        [
          [
            null,
            4,
            5,
            null
          ]
        ], <pyarrow.lib.ChunkedArray object at ...>
        [
          [
            "Flamingo",
            "Horse",
            null,
            "Centipede"
          ]
        ]]
        """

    column_names = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Names of the table's columns.

        Returns
        -------
        list of str

        Examples
        --------
        >>> import pyarrow as pa
        >>> import pandas as pd
        >>> df = pd.DataFrame({'n_legs': [2, 4, 5, 100],
        ...                    'animals': ["Flamingo", "Horse", "Brittle stars", "Centipede"]})
        >>> table = pa.Table.from_pandas(df)
        >>> table.column_names
        ['n_legs', 'animals']
        """

    nbytes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Total number of bytes consumed by the elements of the table.

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
        >>> import pandas as pd
        >>> df = pd.DataFrame({'n_legs': [None, 4, 5, None],
        ...                    'animals': ["Flamingo", "Horse", None, "Centipede"]})
        >>> table = pa.Table.from_pandas(df)
        >>> table.nbytes
        72
        """

    num_columns = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Number of columns in this table.

        Returns
        -------
        int

        Examples
        --------
        >>> import pyarrow as pa
        >>> import pandas as pd
        >>> df = pd.DataFrame({'n_legs': [None, 4, 5, None],
        ...                    'animals': ["Flamingo", "Horse", None, "Centipede"]})
        >>> table = pa.Table.from_pandas(df)
        >>> table.num_columns
        2
        """

    num_rows = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Number of rows in this table.

        Due to the definition of a table, all columns have the same number of
        rows.

        Returns
        -------
        int

        Examples
        --------
        >>> import pyarrow as pa
        >>> import pandas as pd
        >>> df = pd.DataFrame({'n_legs': [None, 4, 5, None],
        ...                    'animals': ["Flamingo", "Horse", None, "Centipede"]})
        >>> table = pa.Table.from_pandas(df)
        >>> table.num_rows
        4
        """

    schema = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Schema of the table and its columns.

        Returns
        -------
        Schema

        Examples
        --------
        >>> import pyarrow as pa
        >>> import pandas as pd
        >>> df = pd.DataFrame({'n_legs': [2, 4, 5, 100],
        ...                    'animals': ["Flamingo", "Horse", "Brittle stars", "Centipede"]})
        >>> table = pa.Table.from_pandas(df)
        >>> table.schema
        n_legs: int64
        animals: string
        -- schema metadata --
        pandas: '{"index_columns": [{"kind": "range", "name": null, "start": 0, "' ...
        """

    shape = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Dimensions of the table: (#rows, #columns).

        Returns
        -------
        (int, int)
            Number of rows and number of columns.

        Examples
        --------
        >>> import pyarrow as pa
        >>> import pandas as pd
        >>> df = pd.DataFrame({'n_legs': [None, 4, 5, None],
        ...                    'animals': ["Flamingo", "Horse", None, "Centipede"]})
        >>> table = pa.Table.from_pandas(df)
        >>> table.shape
        (4, 2)
        """


    __hash__ = None
    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001970BCC5840>'


