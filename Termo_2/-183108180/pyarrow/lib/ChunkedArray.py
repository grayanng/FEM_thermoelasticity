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

class ChunkedArray(_PandasConvertible):
    """
    ChunkedArray()
    
        An array-like composed from a (possibly empty) collection of pyarrow.Arrays
    
        Warnings
        --------
        Do not call this class's constructor directly.
    
        Examples
        --------
        To construct a ChunkedArray object use :func:`pyarrow.chunked_array`:
    
        >>> import pyarrow as pa
        >>> pa.chunked_array([], type=pa.int8())
        <pyarrow.lib.ChunkedArray object at ...>
        [
        ...
        ]
    
        >>> pa.chunked_array([[2, 2, 4], [4, 5, 100]])
        <pyarrow.lib.ChunkedArray object at ...>
        [
          [
            2,
            2,
            4
          ],
          [
            4,
            5,
            100
          ]
        ]
        >>> isinstance(pa.chunked_array([[2, 2, 4], [4, 5, 100]]), pa.ChunkedArray)
        True
    """
    def cast(self, target_type=None, safe=None, options=None): # real signature unknown; restored from __doc__
        """
        ChunkedArray.cast(self, target_type=None, safe=None, options=None)
        
                Cast array values to another data type
        
                See :func:`pyarrow.compute.cast` for usage.
        
                Parameters
                ----------
                target_type : DataType, None
                    Type to cast array to.
                safe : boolean, default True
                    Whether to check for conversion errors such as overflow.
                options : CastOptions, default None
                    Additional checks pass by CastOptions
        
                Returns
                -------
                cast : Array or ChunkedArray
        
                Examples
                --------
                >>> import pyarrow as pa
                >>> n_legs = pa.chunked_array([[2, 2, 4], [4, 5, 100]])
                >>> n_legs.type
                DataType(int64)
        
                Change the data type of an array:
        
                >>> n_legs_seconds = n_legs.cast(pa.duration('s'))
                >>> n_legs_seconds.type
                DurationType(duration[s])
        """
        pass

    def chunk(self, i): # real signature unknown; restored from __doc__
        """
        ChunkedArray.chunk(self, i)
        
                Select a chunk by its index.
        
                Parameters
                ----------
                i : int
        
                Returns
                -------
                pyarrow.Array
        
                Examples
                --------
                >>> import pyarrow as pa
                >>> n_legs = pa.chunked_array([[2, 2, None], [4, 5, 100]])
                >>> n_legs.chunk(1)
                <pyarrow.lib.Int64Array object at ...>
                [
                  4,
                  5,
                  100
                ]
        """
        pass

    def combine_chunks(self, MemoryPool_memory_pool=None): # real signature unknown; restored from __doc__
        """
        ChunkedArray.combine_chunks(self, MemoryPool memory_pool=None)
        
                Flatten this ChunkedArray into a single non-chunked array.
        
                Parameters
                ----------
                memory_pool : MemoryPool, default None
                    For memory allocations, if required, otherwise use default pool
        
                Returns
                -------
                result : Array
        
                Examples
                --------
                >>> import pyarrow as pa
                >>> n_legs = pa.chunked_array([[2, 2, 4], [4, 5, 100]])
                >>> n_legs
                <pyarrow.lib.ChunkedArray object at ...>
                [
                  [
                    2,
                    2,
                    4
                  ],
                  [
                    4,
                    5,
                    100
                  ]
                ]
                >>> n_legs.combine_chunks()
                <pyarrow.lib.Int64Array object at ...>
                [
                  2,
                  2,
                  4,
                  4,
                  5,
                  100
                ]
        """
        pass

    def dictionary_encode(self, null_encoding=None): # real signature unknown; restored from __doc__
        """
        ChunkedArray.dictionary_encode(self, null_encoding=u'mask')
        
                Compute dictionary-encoded representation of array.
        
                See :func:`pyarrow.compute.dictionary_encode` for full usage.
        
                Parameters
                ----------
                null_encoding : str, default "mask"
                    How to handle null entries.
        
                Returns
                -------
                encoded : ChunkedArray
                    A dictionary-encoded version of this array.
        
                Examples
                --------
                >>> import pyarrow as pa
                >>> animals = pa.chunked_array((
                ...             ["Flamingo", "Parot", "Dog"],
                ...             ["Horse", "Brittle stars", "Centipede"]
                ...             ))
                >>> animals.dictionary_encode()
                <pyarrow.lib.ChunkedArray object at ...>
                [
                ...
                  -- dictionary:
                    [
                      "Flamingo",
                      "Parot",
                      "Dog",
                      "Horse",
                      "Brittle stars",
                      "Centipede"
                    ]
                  -- indices:
                    [
                      0,
                      1,
                      2
                    ],
                ...
                  -- dictionary:
                    [
                      "Flamingo",
                      "Parot",
                      "Dog",
                      "Horse",
                      "Brittle stars",
                      "Centipede"
                    ]
                  -- indices:
                    [
                      3,
                      4,
                      5
                    ]
                ]
        """
        pass

    def drop_null(self): # real signature unknown; restored from __doc__
        """
        ChunkedArray.drop_null(self)
        
                Remove missing values from a chunked array.
                See :func:`pyarrow.compute.drop_null` for full description.
        
                Examples
                --------
                >>> import pyarrow as pa
                >>> n_legs = pa.chunked_array([[2, 2, None], [4, 5, 100]])
                >>> n_legs
                <pyarrow.lib.ChunkedArray object at ...>
                [
                  [
                    2,
                    2,
                    null
                  ],
                  [
                    4,
                    5,
                    100
                  ]
                ]
                >>> n_legs.drop_null()
                <pyarrow.lib.ChunkedArray object at ...>
                [
                  [
                    2,
                    2
                  ],
                  [
                    4,
                    5,
                    100
                  ]
                ]
        """
        pass

    def equals(self, ChunkedArray_other): # real signature unknown; restored from __doc__
        """
        ChunkedArray.equals(self, ChunkedArray other)
        
                Return whether the contents of two chunked arrays are equal.
        
                Parameters
                ----------
                other : pyarrow.ChunkedArray
                    Chunked array to compare against.
        
                Returns
                -------
                are_equal : bool
        
                Examples
                --------
                >>> import pyarrow as pa
                >>> n_legs = pa.chunked_array([[2, 2, 4], [4, 5, 100]])
                >>> animals = pa.chunked_array((
                ...             ["Flamingo", "Parot", "Dog"],
                ...             ["Horse", "Brittle stars", "Centipede"]
                ...             ))
                >>> n_legs.equals(n_legs)
                True
                >>> n_legs.equals(animals)
                False
        """
        pass

    def fill_null(self, fill_value): # real signature unknown; restored from __doc__
        """
        ChunkedArray.fill_null(self, fill_value)
        
                Replace each null element in values with fill_value.
        
                See :func:`pyarrow.compute.fill_null` for full usage.
        
                Parameters
                ----------
                fill_value : any
                    The replacement value for null entries.
        
                Returns
                -------
                result : Array or ChunkedArray
                    A new array with nulls replaced by the given value.
        
                Examples
                --------
                >>> import pyarrow as pa
                >>> fill_value = pa.scalar(5, type=pa.int8())
                >>> n_legs = pa.chunked_array([[2, 2, 4], [4, None, 100]])
                >>> n_legs.fill_null(fill_value)
                <pyarrow.lib.ChunkedArray object at ...>
                [
                  [
                    2,
                    2,
                    4,
                    4,
                    5,
                    100
                  ]
                ]
        """
        pass

    def filter(self, mask, null_selection_behavior=None): # real signature unknown; restored from __doc__
        """
        ChunkedArray.filter(self, mask, null_selection_behavior=u'drop')
        
                Select values from the chunked array.
        
                See :func:`pyarrow.compute.filter` for full usage.
        
                Parameters
                ----------
                mask : Array or array-like
                    The boolean mask to filter the chunked array with.
                null_selection_behavior : str, default "drop"
                    How nulls in the mask should be handled.
        
                Returns
                -------
                filtered : Array or ChunkedArray
                    An array of the same type, with only the elements selected by
                    the boolean mask.
        
                Examples
                --------
                >>> import pyarrow as pa
                >>> n_legs = pa.chunked_array([[2, 2, 4], [4, 5, 100]])
                >>> n_legs
                <pyarrow.lib.ChunkedArray object at ...>
                [
                  [
                    2,
                    2,
                    4
                  ],
                  [
                    4,
                    5,
                    100
                  ]
                ]
                >>> mask = pa.array([True, False, None, True, False, True])
                >>> n_legs.filter(mask)
                <pyarrow.lib.ChunkedArray object at ...>
                [
                  [
                    2
                  ],
                  [
                    4,
                    100
                  ]
                ]
                >>> n_legs.filter(mask, null_selection_behavior="emit_null")
                <pyarrow.lib.ChunkedArray object at ...>
                [
                  [
                    2,
                    null
                  ],
                  [
                    4,
                    100
                  ]
                ]
        """
        pass

    def flatten(self, MemoryPool_memory_pool=None): # real signature unknown; restored from __doc__
        """
        ChunkedArray.flatten(self, MemoryPool memory_pool=None)
        
                Flatten this ChunkedArray.  If it has a struct type, the column is
                flattened into one array per struct field.
        
                Parameters
                ----------
                memory_pool : MemoryPool, default None
                    For memory allocations, if required, otherwise use default pool
        
                Returns
                -------
                result : list of ChunkedArray
        
                Examples
                --------
                >>> import pyarrow as pa
                >>> n_legs = pa.chunked_array([[2, 2, 4], [4, 5, 100]])
                >>> c_arr = pa.chunked_array(n_legs.value_counts())
                >>> c_arr
                <pyarrow.lib.ChunkedArray object at ...>
                [
                  -- is_valid: all not null
                  -- child 0 type: int64
                    [
                      2,
                      4,
                      5,
                      100
                    ]
                  -- child 1 type: int64
                    [
                      2,
                      2,
                      1,
                      1
                    ]
                ]
                >>> c_arr.flatten()
                [<pyarrow.lib.ChunkedArray object at ...>
                [
                  [
                    2,
                    4,
                    5,
                    100
                  ]
                ], <pyarrow.lib.ChunkedArray object at ...>
                [
                  [
                    2,
                    2,
                    1,
                    1
                  ]
                ]]
                >>> c_arr.type
                StructType(struct<values: int64, counts: int64>)
                >>> n_legs.type
                DataType(int64)
        """
        pass

    def format(self, **kwargs): # real signature unknown; restored from __doc__
        """ ChunkedArray.format(self, **kwargs) """
        pass

    def get_total_buffer_size(self): # real signature unknown; restored from __doc__
        """
        ChunkedArray.get_total_buffer_size(self)
        
                The sum of bytes in each buffer referenced by the chunked array.
        
                An array may only reference a portion of a buffer.
                This method will overestimate in this case and return the
                byte size of the entire buffer.
        
                If a buffer is referenced multiple times then it will
                only be counted once.
        
                Examples
                --------
                >>> import pyarrow as pa
                >>> n_legs = pa.chunked_array([[2, 2, 4], [4, None, 100]])
                >>> n_legs.get_total_buffer_size()
                49
        """
        pass

    def index(self, value, start=None, end=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        ChunkedArray.index(self, value, start=None, end=None, *, memory_pool=None)
        
                Find the first index of a value.
        
                See :func:`pyarrow.compute.index` for full usage.
        
                Parameters
                ----------
                value : Scalar or object
                    The value to look for in the array.
                start : int, optional
                    The start index where to look for `value`.
                end : int, optional
                    The end index where to look for `value`.
                memory_pool : MemoryPool, optional
                    A memory pool for potential memory allocations.
        
                Returns
                -------
                index : Int64Scalar
                    The index of the value in the array (-1 if not found).
        
                Examples
                --------
                >>> import pyarrow as pa
                >>> n_legs = pa.chunked_array([[2, 2, 4], [4, 5, 100]])
                >>> n_legs
                <pyarrow.lib.ChunkedArray object at ...>
                [
                  [
                    2,
                    2,
                    4
                  ],
                  [
                    4,
                    5,
                    100
                  ]
                ]
                >>> n_legs.index(4)
                <pyarrow.Int64Scalar: 2>
                >>> n_legs.index(4, start=3)
                <pyarrow.Int64Scalar: 3>
        """
        pass

    def is_null(self, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        ChunkedArray.is_null(self, *, nan_is_null=False)
        
                Return boolean array indicating the null values.
        
                Parameters
                ----------
                nan_is_null : bool (optional, default False)
                    Whether floating-point NaN values should also be considered null.
        
                Returns
                -------
                array : boolean Array or ChunkedArray
        
                Examples
                --------
                >>> import pyarrow as pa
                >>> n_legs = pa.chunked_array([[2, 2, 4], [4, None, 100]])
                >>> n_legs.is_null()
                <pyarrow.lib.ChunkedArray object at ...>
                [
                  [
                    false,
                    false,
                    false,
                    false,
                    true,
                    false
                  ]
                ]
        """
        pass

    def is_valid(self): # real signature unknown; restored from __doc__
        """
        ChunkedArray.is_valid(self)
        
                Return boolean array indicating the non-null values.
        
                Examples
                --------
                >>> import pyarrow as pa
                >>> n_legs = pa.chunked_array([[2, 2, 4], [4, None, 100]])
                >>> n_legs.is_valid()
                <pyarrow.lib.ChunkedArray object at ...>
                [
                  [
                    true,
                    true,
                    true
                  ],
                  [
                    true,
                    false,
                    true
                  ]
                ]
        """
        pass

    def iterchunks(self): # real signature unknown; restored from __doc__
        """
        ChunkedArray.iterchunks(self)
        
                Convert to an iterator of ChunkArrays.
        
                Examples
                --------
                >>> import pyarrow as pa
                >>> n_legs = pa.chunked_array([[2, 2, 4], [4, None, 100]])
                >>> for i in n_legs.iterchunks():
                ...     print(i.null_count)
                ...
                0
                1
        """
        pass

    def length(self): # real signature unknown; restored from __doc__
        """
        ChunkedArray.length(self)
        
                Return length of a ChunkedArray.
        
                Examples
                --------
                >>> import pyarrow as pa
                >>> n_legs = pa.chunked_array([[2, 2, 4], [4, 5, 100]])
                >>> n_legs.length()
                6
        """
        pass

    def slice(self, offset=0, length=None): # real signature unknown; restored from __doc__
        """
        ChunkedArray.slice(self, offset=0, length=None)
        
                Compute zero-copy slice of this ChunkedArray
        
                Parameters
                ----------
                offset : int, default 0
                    Offset from start of array to slice
                length : int, default None
                    Length of slice (default is until end of batch starting from
                    offset)
        
                Returns
                -------
                sliced : ChunkedArray
        
                Examples
                --------
                >>> import pyarrow as pa
                >>> n_legs = pa.chunked_array([[2, 2, 4], [4, 5, 100]])
                >>> n_legs
                <pyarrow.lib.ChunkedArray object at ...>
                [
                  [
                    2,
                    2,
                    4
                  ],
                  [
                    4,
                    5,
                    100
                  ]
                ]
                >>> n_legs.slice(2,2)
                <pyarrow.lib.ChunkedArray object at ...>
                [
                  [
                    4
                  ],
                  [
                    4
                  ]
                ]
        """
        pass

    def sort(self, order=None, **kwargs): # real signature unknown; restored from __doc__
        """
        ChunkedArray.sort(self, order=u'ascending', **kwargs)
        
                Sort the ChunkedArray
        
                Parameters
                ----------
                order : str, default "ascending"
                    Which order to sort values in.
                    Accepted values are "ascending", "descending".
                **kwargs : dict, optional
                    Additional sorting options.
                    As allowed by :class:`SortOptions`
        
                Returns
                -------
                result : ChunkedArray
        """
        pass

    def take(self, indices): # real signature unknown; restored from __doc__
        """
        ChunkedArray.take(self, indices)
        
                Select values from the chunked array.
        
                See :func:`pyarrow.compute.take` for full usage.
        
                Parameters
                ----------
                indices : Array or array-like
                    The indices in the array whose values will be returned.
        
                Returns
                -------
                taken : Array or ChunkedArray
                    An array with the same datatype, containing the taken values.
        
                Examples
                --------
                >>> import pyarrow as pa
                >>> n_legs = pa.chunked_array([[2, 2, 4], [4, 5, 100]])
                >>> n_legs
                <pyarrow.lib.ChunkedArray object at ...>
                [
                  [
                    2,
                    2,
                    4
                  ],
                  [
                    4,
                    5,
                    100
                  ]
                ]
                >>> n_legs.take([1,4,5])
                <pyarrow.lib.ChunkedArray object at ...>
                [
                  [
                    2,
                    5,
                    100
                  ]
                ]
        """
        pass

    def to_numpy(self): # real signature unknown; restored from __doc__
        """
        ChunkedArray.to_numpy(self)
        
                Return a NumPy copy of this array (experimental).
        
                Returns
                -------
                array : numpy.ndarray
        
                Examples
                --------
                >>> import pyarrow as pa
                >>> n_legs = pa.chunked_array([[2, 2, 4], [4, 5, 100]])
                >>> n_legs.to_numpy()
                array([  2,   2,   4,   4,   5, 100])
        """
        pass

    def to_pylist(self): # real signature unknown; restored from __doc__
        """
        ChunkedArray.to_pylist(self)
        
                Convert to a list of native Python objects.
        
                Examples
                --------
                >>> import pyarrow as pa
                >>> n_legs = pa.chunked_array([[2, 2, 4], [4, None, 100]])
                >>> n_legs.to_pylist()
                [2, 2, 4, 4, None, 100]
        """
        pass

    def to_string(self, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        ChunkedArray.to_string(self, *, int indent=0, int window=5, int container_window=2, bool skip_new_lines=False)
        
                Render a "pretty-printed" string representation of the ChunkedArray
        
                Parameters
                ----------
                indent : int
                    How much to indent right the content of the array,
                    by default ``0``.
                window : int
                    How many items to preview within each chunk at the begin and end
                    of the chunk when the chunk is bigger than the window.
                    The other elements will be ellipsed.
                container_window : int
                    How many chunks to preview at the begin and end
                    of the array when the array is bigger than the window.
                    The other elements will be ellipsed.
                    This setting also applies to list columns.
                skip_new_lines : bool
                    If the array should be rendered as a single line of text
                    or if each element should be on its own line.
        
                Examples
                --------
                >>> import pyarrow as pa
                >>> n_legs = pa.chunked_array([[2, 2, 4], [4, 5, 100]])
                >>> n_legs.to_string(skip_new_lines=True)
                '[[2,2,4],[4,5,100]]'
        """
        pass

    def unify_dictionaries(self, MemoryPool_memory_pool=None): # real signature unknown; restored from __doc__
        """
        ChunkedArray.unify_dictionaries(self, MemoryPool memory_pool=None)
        
                Unify dictionaries across all chunks.
        
                This method returns an equivalent chunked array, but where all
                chunks share the same dictionary values.  Dictionary indices are
                transposed accordingly.
        
                If there are no dictionaries in the chunked array, it is returned
                unchanged.
        
                Parameters
                ----------
                memory_pool : MemoryPool, default None
                    For memory allocations, if required, otherwise use default pool
        
                Returns
                -------
                result : ChunkedArray
        
                Examples
                --------
                >>> import pyarrow as pa
                >>> arr_1 = pa.array(["Flamingo", "Parot", "Dog"]).dictionary_encode()
                >>> arr_2 = pa.array(["Horse", "Brittle stars", "Centipede"]).dictionary_encode()
                >>> c_arr = pa.chunked_array([arr_1, arr_2])
                >>> c_arr
                <pyarrow.lib.ChunkedArray object at ...>
                [
                ...
                  -- dictionary:
                    [
                      "Flamingo",
                      "Parot",
                      "Dog"
                    ]
                  -- indices:
                    [
                      0,
                      1,
                      2
                    ],
                ...
                  -- dictionary:
                    [
                      "Horse",
                      "Brittle stars",
                      "Centipede"
                    ]
                  -- indices:
                    [
                      0,
                      1,
                      2
                    ]
                ]
                >>> c_arr.unify_dictionaries()
                <pyarrow.lib.ChunkedArray object at ...>
                [
                ...
                  -- dictionary:
                    [
                      "Flamingo",
                      "Parot",
                      "Dog",
                      "Horse",
                      "Brittle stars",
                      "Centipede"
                    ]
                  -- indices:
                    [
                      0,
                      1,
                      2
                    ],
                ...
                  -- dictionary:
                    [
                      "Flamingo",
                      "Parot",
                      "Dog",
                      "Horse",
                      "Brittle stars",
                      "Centipede"
                    ]
                  -- indices:
                    [
                      3,
                      4,
                      5
                    ]
                ]
        """
        pass

    def unique(self): # real signature unknown; restored from __doc__
        """
        ChunkedArray.unique(self)
        
                Compute distinct elements in array
        
                Returns
                -------
                pyarrow.Array
        
                Examples
                --------
                >>> import pyarrow as pa
                >>> n_legs = pa.chunked_array([[2, 2, 4], [4, 5, 100]])
                >>> n_legs
                <pyarrow.lib.ChunkedArray object at ...>
                [
                  [
                    2,
                    2,
                    4
                  ],
                  [
                    4,
                    5,
                    100
                  ]
                ]
                >>> n_legs.unique()
                <pyarrow.lib.Int64Array object at ...>
                [
                  2,
                  4,
                  5,
                  100
                ]
        """
        pass

    def validate(self, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        ChunkedArray.validate(self, *, full=False)
        
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

    def value_counts(self): # real signature unknown; restored from __doc__
        """
        ChunkedArray.value_counts(self)
        
                Compute counts of unique elements in array.
        
                Returns
                -------
                An array of  <input type "Values", int64_t "Counts"> structs
        
                Examples
                --------
                >>> import pyarrow as pa
                >>> n_legs = pa.chunked_array([[2, 2, 4], [4, 5, 100]])
                >>> n_legs
                <pyarrow.lib.ChunkedArray object at ...>
                [
                  [
                    2,
                    2,
                    4
                  ],
                  [
                    4,
                    5,
                    100
                  ]
                ]
                >>> n_legs.value_counts()
                <pyarrow.lib.StructArray object at ...>
                -- is_valid: all not null
                -- child 0 type: int64
                  [
                    2,
                    4,
                    5,
                    100
                  ]
                -- child 1 type: int64
                  [
                    2,
                    2,
                    1,
                    1
                  ]
        """
        pass

    def _to_pandas(self, options, types_mapper=None, **kwargs): # real signature unknown; restored from __doc__
        """ ChunkedArray._to_pandas(self, options, types_mapper=None, **kwargs) """
        pass

    def __array__(self, dtype=None): # real signature unknown; restored from __doc__
        """ ChunkedArray.__array__(self, dtype=None) """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __getitem__(self, *args, **kwargs): # real signature unknown
        """
        Slice or return value at given index
        
                Parameters
                ----------
                key : integer or slice
                    Slices with step not equal to 1 (or None) will produce a copy
                    rather than a zero-copy view
        
                Returns
                -------
                value : Scalar (index) or ChunkedArray (slice)
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
        """ ChunkedArray.__reduce__(self) """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __sizeof__(self): # real signature unknown; restored from __doc__
        """ ChunkedArray.__sizeof__(self) """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    chunks = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Convert to a list of single-chunked arrays.

        Examples
        --------
        >>> import pyarrow as pa
        >>> n_legs = pa.chunked_array([[2, 2, None], [4, 5, 100]])
        >>> n_legs
        <pyarrow.lib.ChunkedArray object at ...>
        [
          [
            2,
            2,
            null
          ],
          [
            4,
            5,
            100
          ]
        ]
        >>> n_legs.chunks
        [<pyarrow.lib.Int64Array object at ...>
        [
          2,
          2,
          null
        ], <pyarrow.lib.Int64Array object at ...>
        [
          4,
          5,
          100
        ]]
        """

    data = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    nbytes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Total number of bytes consumed by the elements of the chunked array.

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
        >>> n_legs = pa.chunked_array([[2, 2, 4], [4, None, 100]])
        >>> n_legs.nbytes
        49
        """

    null_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Number of null entries

        Returns
        -------
        int

        Examples
        --------
        >>> import pyarrow as pa
        >>> n_legs = pa.chunked_array([[2, 2, 4], [4, None, 100]])
        >>> n_legs.null_count
        1
        """

    num_chunks = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Number of underlying chunks.

        Returns
        -------
        int

        Examples
        --------
        >>> import pyarrow as pa
        >>> n_legs = pa.chunked_array([[2, 2, None], [4, 5, 100]])
        >>> n_legs.num_chunks
        2
        """

    type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Return data type of a ChunkedArray.

        Examples
        --------
        >>> import pyarrow as pa
        >>> n_legs = pa.chunked_array([[2, 2, 4], [4, 5, 100]])
        >>> n_legs.type
        DataType(int64)
        """

    _name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __hash__ = None
    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001970BCC58A0>'


