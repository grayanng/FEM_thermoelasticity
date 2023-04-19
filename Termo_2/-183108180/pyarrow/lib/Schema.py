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

class Schema(_Weakrefable):
    """
    Schema()
    
        A named collection of types a.k.a schema. A schema defines the
        column names and types in a record batch or table data structure.
        They also contain metadata about the columns. For example, schemas 
        converted from Pandas contain metadata about their original Pandas 
        types so they can be converted back to the same types.
    
        Warnings
        --------
        Do not call this class's constructor directly. Instead use
        :func:`pyarrow.schema` factory function which makes a new Arrow
        Schema object.
    
        Examples
        --------
        Create a new Arrow Schema object:
    
        >>> import pyarrow as pa
        >>> pa.schema([
        ...     ('some_int', pa.int32()),
        ...     ('some_string', pa.string())
        ... ])
        some_int: int32
        some_string: string
    
        Create Arrow Schema with metadata:
    
        >>> pa.schema([
        ...     pa.field('n_legs', pa.int64()),
        ...     pa.field('animals', pa.string())],
        ...     metadata={"n_legs": "Number of legs per animal"})
        n_legs: int64
        animals: string
        -- schema metadata --
        n_legs: 'Number of legs per animal'
    """
    def add_metadata(self, metadata): # real signature unknown; restored from __doc__
        """
        Schema.add_metadata(self, metadata)
        
                DEPRECATED
        
                Parameters
                ----------
                metadata : dict
                    Keys and values must be string-like / coercible to bytes
        """
        pass

    def append(self, Field_field): # real signature unknown; restored from __doc__
        """
        Schema.append(self, Field field)
        
                Append a field at the end of the schema.
        
                In contrast to Python's ``list.append()`` it does return a new
                object, leaving the original Schema unmodified.
        
                Parameters
                ----------
                field : Field
        
                Returns
                -------
                schema: Schema
                    New object with appended field.
        
                Examples
                --------
                >>> import pyarrow as pa
                >>> schema = pa.schema([
                ...     pa.field('n_legs', pa.int64()),
                ...     pa.field('animals', pa.string())])
        
                Append a field 'extra' at the end of the schema:
        
                >>> schema_new = schema.append(pa.field('extra', pa.bool_()))
                >>> schema_new
                n_legs: int64
                animals: string
                extra: bool
        
                Original schema is unmodified:
        
                >>> schema
                n_legs: int64
                animals: string
        """
        pass

    def empty_table(self): # real signature unknown; restored from __doc__
        """
        Schema.empty_table(self)
        
                Provide an empty table according to the schema.
        
                Returns
                -------
                table: pyarrow.Table
        
                Examples
                --------
                >>> import pyarrow as pa
                >>> schema = pa.schema([
                ...     pa.field('n_legs', pa.int64()),
                ...     pa.field('animals', pa.string())])
        
                Create an empty table with schema's fields:
        
                >>> schema.empty_table()
                pyarrow.Table
                n_legs: int64
                animals: string
                ----
                n_legs: [[]]
                animals: [[]]
        """
        pass

    def equals(self, Schema_other, bool_check_metadata=False): # real signature unknown; restored from __doc__
        """
        Schema.equals(self, Schema other, bool check_metadata=False)
        
                Test if this schema is equal to the other
        
                Parameters
                ----------
                other :  pyarrow.Schema
                check_metadata : bool, default False
                    Key/value metadata must be equal too
        
                Returns
                -------
                is_equal : bool
        
                Examples
                --------
                >>> import pyarrow as pa
                >>> schema1 = pa.schema([
                ...     pa.field('n_legs', pa.int64()),
                ...     pa.field('animals', pa.string())],
                ...     metadata={"n_legs": "Number of legs per animal"})
                >>> schema2 = pa.schema([
                ...     ('some_int', pa.int32()),
                ...     ('some_string', pa.string())
                ... ])
        
                Test two equal schemas:
        
                >>> schema1.equals(schema1)
                True
        
                Test two unequal schemas:
        
                >>> schema1.equals(schema2)
                False
        """
        pass

    def field(self, i): # real signature unknown; restored from __doc__
        """
        Schema.field(self, i)
        
                Select a field by its column name or numeric index.
        
                Parameters
                ----------
                i : int or string
        
                Returns
                -------
                pyarrow.Field
        
                Examples
                --------
                >>> import pyarrow as pa
                >>> schema = pa.schema([
                ...     pa.field('n_legs', pa.int64()),
                ...     pa.field('animals', pa.string())])
        
                Select the second field:
        
                >>> schema.field(1)
                pyarrow.Field<animals: string>
        
                Select the field of the column named 'n_legs':
        
                >>> schema.field('n_legs')
                pyarrow.Field<n_legs: int64>
        """
        pass

    def field_by_name(self, name): # real signature unknown; restored from __doc__
        """
        Schema.field_by_name(self, name)
        
                DEPRECATED
        
                Parameters
                ----------
                name : str
        
                Returns
                -------
                field: pyarrow.Field
        """
        pass

    @classmethod
    def from_pandas(cls, type_cls, df, preserve_index=None): # real signature unknown; restored from __doc__
        """
        Schema.from_pandas(type cls, df, preserve_index=None)
        
                Returns implied schema from dataframe
        
                Parameters
                ----------
                df : pandas.DataFrame
                preserve_index : bool, default True
                    Whether to store the index as an additional column (or columns, for
                    MultiIndex) in the resulting `Table`.
                    The default of None will store the index as a column, except for
                    RangeIndex which is stored as metadata only. Use
                    ``preserve_index=True`` to force it to be stored as a column.
        
                Returns
                -------
                pyarrow.Schema
        
                Examples
                --------
                >>> import pandas as pd
                >>> import pyarrow as pa
                >>> df = pd.DataFrame({
                ...     'int': [1, 2],
                ...     'str': ['a', 'b']
                ... })
        
                Create an Arrow Schema from the schema of a pandas dataframe:
        
                >>> pa.Schema.from_pandas(df)
                int: int64
                str: string
                -- schema metadata --
                pandas: '{"index_columns": [{"kind": "range", "name": null, ...
        """
        pass

    def get_all_field_indices(self, name): # real signature unknown; restored from __doc__
        """
        Schema.get_all_field_indices(self, name)
        
                Return sorted list of indices for the fields with the given name.
        
                Parameters
                ----------
                name : str
                    The name of the field to look up.
        
                Returns
                -------
                indices : List[int]
        
                Examples
                --------
                >>> import pyarrow as pa
                >>> schema = pa.schema([
                ...     pa.field('n_legs', pa.int64()),
                ...     pa.field('animals', pa.string()),
                ...     pa.field('animals', pa.bool_())])
        
                Get the indexes of the fields named 'animals':
        
                >>> schema.get_all_field_indices("animals")
                [1, 2]
        """
        pass

    def get_field_index(self, name): # real signature unknown; restored from __doc__
        """
        Schema.get_field_index(self, name)
        
                Return index of the unique field with the given name.
        
                Parameters
                ----------
                name : str
                    The name of the field to look up.
        
                Returns
                -------
                index : int
                    The index of the field with the given name; -1 if the
                    name isn't found or there are several fields with the given
                    name.
        
                Examples
                --------
                >>> import pyarrow as pa
                >>> schema = pa.schema([
                ...     pa.field('n_legs', pa.int64()),
                ...     pa.field('animals', pa.string())])
        
                Get the index of the field named 'animals':
        
                >>> schema.get_field_index("animals")
                1
        
                Index in case of several fields with the given name:
        
                >>> schema = pa.schema([
                ...     pa.field('n_legs', pa.int64()),
                ...     pa.field('animals', pa.string()),
                ...     pa.field('animals', pa.bool_())],
                ...     metadata={"n_legs": "Number of legs per animal"})
                >>> schema.get_field_index("animals")
                -1
        """
        pass

    def insert(self, int_i, Field_field): # real signature unknown; restored from __doc__
        """
        Schema.insert(self, int i, Field field)
        
                Add a field at position i to the schema.
        
                Parameters
                ----------
                i : int
                field : Field
        
                Returns
                -------
                schema: Schema
        
                Examples
                --------
                >>> import pyarrow as pa
                >>> schema = pa.schema([
                ...     pa.field('n_legs', pa.int64()),
                ...     pa.field('animals', pa.string())])
        
                Insert a new field on the second position:
        
                >>> schema.insert(1, pa.field('extra', pa.bool_()))
                n_legs: int64
                extra: bool
                animals: string
        """
        pass

    def remove(self, int_i): # real signature unknown; restored from __doc__
        """
        Schema.remove(self, int i)
        
                Remove the field at index i from the schema.
        
                Parameters
                ----------
                i : int
        
                Returns
                -------
                schema: Schema
        
                Examples
                --------
                >>> import pyarrow as pa
                >>> schema = pa.schema([
                ...     pa.field('n_legs', pa.int64()),
                ...     pa.field('animals', pa.string())])
        
                Remove the second field of the schema:
        
                >>> schema.remove(1)
                n_legs: int64
        """
        pass

    def remove_metadata(self): # real signature unknown; restored from __doc__
        """
        Schema.remove_metadata(self)
        
                Create new schema without metadata, if any
        
                Returns
                -------
                schema : pyarrow.Schema
        
                Examples
                --------
                >>> import pyarrow as pa
                >>> schema = pa.schema([
                ...     pa.field('n_legs', pa.int64()),
                ...     pa.field('animals', pa.string())],
                ...     metadata={"n_legs": "Number of legs per animal"})
                >>> schema
                n_legs: int64
                animals: string
                -- schema metadata --
                n_legs: 'Number of legs per animal'
        
                Create a new schema with removing the metadata from the original:
        
                >>> schema.remove_metadata()
                n_legs: int64
                animals: string
        """
        pass

    def serialize(self, memory_pool=None): # real signature unknown; restored from __doc__
        """
        Schema.serialize(self, memory_pool=None)
        
                Write Schema to Buffer as encapsulated IPC message
        
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
                >>> schema = pa.schema([
                ...     pa.field('n_legs', pa.int64()),
                ...     pa.field('animals', pa.string())])
        
                Write schema to Buffer:
        
                >>> schema.serialize()
                <pyarrow.Buffer address=0x... size=... is_cpu=True is_mutable=True>
        """
        pass

    def set(self, int_i, Field_field): # real signature unknown; restored from __doc__
        """
        Schema.set(self, int i, Field field)
        
                Replace a field at position i in the schema.
        
                Parameters
                ----------
                i : int
                field : Field
        
                Returns
                -------
                schema: Schema
        
                Examples
                --------
                >>> import pyarrow as pa
                >>> schema = pa.schema([
                ...     pa.field('n_legs', pa.int64()),
                ...     pa.field('animals', pa.string())])
        
                Replace the second field of the schema with a new field 'extra':
        
                >>> schema.set(1, pa.field('replaced', pa.bool_()))
                n_legs: int64
                replaced: bool
        """
        pass

    def to_string(self, truncate_metadata=True, show_field_metadata=True, show_schema_metadata=True): # real signature unknown; restored from __doc__
        """
        Schema.to_string(self, truncate_metadata=True, show_field_metadata=True, show_schema_metadata=True)
        
                Return human-readable representation of Schema
        
                Parameters
                ----------
                truncate_metadata : boolean, default True
                    Limit metadata key/value display to a single line of ~80 characters
                    or less
                show_field_metadata : boolean, default True
                    Display Field-level KeyValueMetadata
                show_schema_metadata : boolean, default True
                    Display Schema-level KeyValueMetadata
        
                Returns
                -------
                str : the formatted output
        """
        pass

    def with_metadata(self, metadata): # real signature unknown; restored from __doc__
        """
        Schema.with_metadata(self, metadata)
        
                Add metadata as dict of string keys and values to Schema
        
                Parameters
                ----------
                metadata : dict
                    Keys and values must be string-like / coercible to bytes
        
                Returns
                -------
                schema : pyarrow.Schema
        
                Examples
                --------
                >>> import pyarrow as pa
                >>> schema = pa.schema([
                ...     pa.field('n_legs', pa.int64()),
                ...     pa.field('animals', pa.string())])
        
                Add metadata to existing schema field:
        
                >>> schema.with_metadata({"n_legs": "Number of legs per animal"})
                n_legs: int64
                animals: string
                -- schema metadata --
                n_legs: 'Number of legs per animal'
        """
        pass

    def _export_to_c(self, out_ptr): # real signature unknown; restored from __doc__
        """
        Schema._export_to_c(self, out_ptr)
        
                Export to a C ArrowSchema struct, given its pointer.
        
                Be careful: if you don't pass the ArrowSchema struct to a consumer,
                its memory will leak.  This is a low-level function intended for
                expert users.
        """
        pass

    def _field(self, int_i): # real signature unknown; restored from __doc__
        """
        Schema._field(self, int i)
        
                Select a field by its numeric index.
        
                Parameters
                ----------
                i : int
        
                Returns
                -------
                pyarrow.Field
        """
        pass

    def _import_from_c(self, in_ptr): # real signature unknown; restored from __doc__
        """
        Schema._import_from_c(in_ptr)
        
                Import Schema from a C ArrowSchema struct, given its pointer.
        
                This is a low-level function intended for expert users.
        """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __getitem__(self, *args, **kwargs): # real signature unknown
        """ Return self[key]. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __hash__(self, *args, **kwargs): # real signature unknown
        """ Return hash(self). """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    def __iter__(self, *args, **kwargs): # real signature unknown
        """ Implement iter(self). """
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
        """ Schema.__reduce__(self) """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __sizeof__(self): # real signature unknown; restored from __doc__
        """ Schema.__sizeof__(self) """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    metadata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        The schema's metadata.

        Returns
        -------
        metadata: dict

        Examples
        --------
        >>> import pyarrow as pa
        >>> schema = pa.schema([
        ...     pa.field('n_legs', pa.int64()),
        ...     pa.field('animals', pa.string())],
        ...     metadata={"n_legs": "Number of legs per animal"})

        Get the metadata of the schema's fields:

        >>> schema.metadata
        {b'n_legs': b'Number of legs per animal'}
        """

    names = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        The schema's field names.

        Returns
        -------
        list of str

        Examples
        --------
        >>> import pyarrow as pa
        >>> schema = pa.schema([
        ...     pa.field('n_legs', pa.int64()),
        ...     pa.field('animals', pa.string())])

        Get the names of the schema's fields:

        >>> schema.names
        ['n_legs', 'animals']
        """

    pandas_metadata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Return deserialized-from-JSON pandas metadata field (if it exists)

        Examples
        --------
        >>> import pyarrow as pa
        >>> import pandas as pd
        >>> df = pd.DataFrame({'n_legs': [2, 4, 5, 100],
        ...                    'animals': ["Flamingo", "Horse", "Brittle stars", "Centipede"]})
        >>> schema = pa.Table.from_pandas(df).schema

        Select pandas metadata field from Arrow Schema:

        >>> schema.pandas_metadata
        {'index_columns': [{'kind': 'range', 'name': None, 'start': 0, 'stop': 4, 'step': 1}], ...
        """

    types = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        The schema's field types.

        Returns
        -------
        list of DataType

        Examples
        --------
        >>> import pyarrow as pa
        >>> schema = pa.schema([
        ...     pa.field('n_legs', pa.int64()),
        ...     pa.field('animals', pa.string())])

        Get the types of the schema's fields:

        >>> schema.types
        [DataType(int64), DataType(string)]
        """


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001970BC82630>'


