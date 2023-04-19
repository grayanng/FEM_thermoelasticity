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

class Array(_PandasConvertible):
    """
    Array()
    
        The base class for all Arrow arrays.
    """
    def buffers(self): # real signature unknown; restored from __doc__
        """
        Array.buffers(self)
        
                Return a list of Buffer objects pointing to this array's physical
                storage.
        
                To correctly interpret these buffers, you need to also apply the offset
                multiplied with the size of the stored data type.
        """
        pass

    def cast(self, target_type=None, safe=None, options=None): # real signature unknown; restored from __doc__
        """
        Array.cast(self, target_type=None, safe=None, options=None)
        
                Cast array values to another data type
        
                See :func:`pyarrow.compute.cast` for usage.
        
                Parameters
                ----------
                target_type : DataType, default None
                    Type to cast array to.
                safe : boolean, default True
                    Whether to check for conversion errors such as overflow.
                options : CastOptions, default None
                    Additional checks pass by CastOptions
        
                Returns
                -------
                cast : Array
        """
        pass

    def dictionary_encode(self, null_encoding=None): # real signature unknown; restored from __doc__
        """
        Array.dictionary_encode(self, null_encoding=u'mask')
        
                Compute dictionary-encoded representation of array.
        
                See :func:`pyarrow.compute.dictionary_encode` for full usage.
        
                Parameters
                ----------
                null_encoding : str, default "mask"
                    How to handle null entries.
        
                Returns
                -------
                encoded : DictionaryArray
                    A dictionary-encoded version of this array.
        """
        pass

    def diff(self, Array_other): # real signature unknown; restored from __doc__
        """
        Array.diff(self, Array other)
        
                Compare contents of this array against another one.
        
                Return a string containing the result of diffing this array
                (on the left side) against the other array (on the right side).
        
                Parameters
                ----------
                other : Array
                    The other array to compare this array with.
        
                Returns
                -------
                diff : str
                    A human-readable printout of the differences.
        
                Examples
                --------
                >>> import pyarrow as pa
                >>> left = pa.array(["one", "two", "three"])
                >>> right = pa.array(["two", None, "two-and-a-half", "three"])
                >>> print(left.diff(right)) # doctest: +SKIP
        
                @@ -0, +0 @@
                -"one"
                @@ -2, +1 @@
                +null
                +"two-and-a-half"
        """
        pass

    def drop_null(self): # real signature unknown; restored from __doc__
        """
        Array.drop_null(self)
        
                Remove missing values from an array.
        """
        pass

    def equals(self, Array_other): # real signature unknown; restored from __doc__
        """ Array.equals(self, Array other) """
        pass

    def fill_null(self, fill_value): # real signature unknown; restored from __doc__
        """
        Array.fill_null(self, fill_value)
        
                See :func:`pyarrow.compute.fill_null` for usage.
        
                Parameters
                ----------
                fill_value : any
                    The replacement value for null entries.
        
                Returns
                -------
                result : Array
                    A new array with nulls replaced by the given value.
        """
        pass

    def filter(self, Array_mask, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        Array.filter(self, Array mask, *, null_selection_behavior=u'drop')
        
                Select values from an array.
        
                See :func:`pyarrow.compute.filter` for full usage.
        
                Parameters
                ----------
                mask : Array or array-like
                    The boolean mask to filter the array with.
                null_selection_behavior : str, default "drop"
                    How nulls in the mask should be handled.
        
                Returns
                -------
                filtered : Array
                    An array of the same type, with only the elements selected by
                    the boolean mask.
        """
        pass

    def format(self, **kwargs): # real signature unknown; restored from __doc__
        """ Array.format(self, **kwargs) """
        pass

    def from_buffers(self, DataType_type, length, buffers, null_count=-1, offset=0, children=None): # real signature unknown; restored from __doc__
        """
        Array.from_buffers(DataType type, length, buffers, null_count=-1, offset=0, children=None)
        
                Construct an Array from a sequence of buffers.
        
                The concrete type returned depends on the datatype.
        
                Parameters
                ----------
                type : DataType
                    The value type of the array.
                length : int
                    The number of values in the array.
                buffers : List[Buffer]
                    The buffers backing this array.
                null_count : int, default -1
                    The number of null entries in the array. Negative value means that
                    the null count is not known.
                offset : int, default 0
                    The array's logical offset (in values, not in bytes) from the
                    start of each buffer.
                children : List[Array], default None
                    Nested type children with length matching type.num_fields.
        
                Returns
                -------
                array : Array
        """
        pass

    def from_pandas(self, obj, mask=None, type=None, bool_safe=True, MemoryPool_memory_pool=None): # real signature unknown; restored from __doc__
        """
        Array.from_pandas(obj, mask=None, type=None, bool safe=True, MemoryPool memory_pool=None)
        
                Convert pandas.Series to an Arrow Array.
        
                This method uses Pandas semantics about what values indicate
                nulls. See pyarrow.array for more general conversion from arrays or
                sequences to Arrow arrays.
        
                Parameters
                ----------
                obj : ndarray, pandas.Series, array-like
                mask : array (boolean), optional
                    Indicate which values are null (True) or not null (False).
                type : pyarrow.DataType
                    Explicit type to attempt to coerce to, otherwise will be inferred
                    from the data.
                safe : bool, default True
                    Check for overflows or other unsafe conversions.
                memory_pool : pyarrow.MemoryPool, optional
                    If not passed, will allocate memory from the currently-set default
                    memory pool.
        
                Notes
                -----
                Localized timestamps will currently be returned as UTC (pandas's native
                representation). Timezone-naive data will be implicitly interpreted as
                UTC.
        
                Returns
                -------
                array : pyarrow.Array or pyarrow.ChunkedArray
                    ChunkedArray is returned if object data overflows binary buffer.
        """
        pass

    def get_total_buffer_size(self): # real signature unknown; restored from __doc__
        """
        Array.get_total_buffer_size(self)
        
                The sum of bytes in each buffer referenced by the array.
        
                An array may only reference a portion of a buffer.
                This method will overestimate in this case and return the
                byte size of the entire buffer.
        
                If a buffer is referenced multiple times then it will
                only be counted once.
        """
        pass

    def index(self, value, start=None, end=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        Array.index(self, value, start=None, end=None, *, memory_pool=None)
        
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
        """
        pass

    def is_null(self, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        Array.is_null(self, *, nan_is_null=False)
        
                Return BooleanArray indicating the null values.
        
                Parameters
                ----------
                nan_is_null : bool (optional, default False)
                    Whether floating-point NaN values should also be considered null.
        
                Returns
                -------
                array : boolean Array
        """
        pass

    def is_valid(self): # real signature unknown; restored from __doc__
        """
        Array.is_valid(self)
        
                Return BooleanArray indicating the non-null values.
        """
        pass

    def slice(self, offset=0, length=None): # real signature unknown; restored from __doc__
        """
        Array.slice(self, offset=0, length=None)
        
                Compute zero-copy slice of this array.
        
                Parameters
                ----------
                offset : int, default 0
                    Offset from start of array to slice.
                length : int, default None
                    Length of slice (default is until end of Array starting from
                    offset).
        
                Returns
                -------
                sliced : RecordBatch
        """
        pass

    def sort(self, order=None, **kwargs): # real signature unknown; restored from __doc__
        """
        Array.sort(self, order=u'ascending', **kwargs)
        
                Sort the Array
        
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
                result : Array
        """
        pass

    def sum(self, **kwargs): # real signature unknown; restored from __doc__
        """
        Array.sum(self, **kwargs)
        
                Sum the values in a numerical array.
        
                See :func:`pyarrow.compute.sum` for full usage.
        
                Parameters
                ----------
                **kwargs : dict, optional
                    Options to pass to :func:`pyarrow.compute.sum`.
        
                Returns
                -------
                sum : Scalar
                    A scalar containing the sum value.
        """
        pass

    def take(self, indices): # real signature unknown; restored from __doc__
        """
        Array.take(self, indices)
        
                Select values from an array.
        
                See :func:`pyarrow.compute.take` for full usage.
        
                Parameters
                ----------
                indices : Array or array-like
                    The indices in the array whose values will be returned.
        
                Returns
                -------
                taken : Array
                    An array with the same datatype, containing the taken values.
        """
        pass

    def tolist(self): # real signature unknown; restored from __doc__
        """
        Array.tolist(self)
        
                Alias of to_pylist for compatibility with NumPy.
        """
        pass

    def to_numpy(self, zero_copy_only=True, writable=False): # real signature unknown; restored from __doc__
        """
        Array.to_numpy(self, zero_copy_only=True, writable=False)
        
                Return a NumPy view or copy of this array (experimental).
        
                By default, tries to return a view of this array. This is only
                supported for primitive arrays with the same memory layout as NumPy
                (i.e. integers, floating point, ..) and without any nulls.
        
                Parameters
                ----------
                zero_copy_only : bool, default True
                    If True, an exception will be raised if the conversion to a numpy
                    array would require copying the underlying data (e.g. in presence
                    of nulls, or for non-primitive types).
                writable : bool, default False
                    For numpy arrays created with zero copy (view on the Arrow data),
                    the resulting array is not writable (Arrow data is immutable).
                    By setting this to True, a copy of the array is made to ensure
                    it is writable.
        
                Returns
                -------
                array : numpy.ndarray
        """
        pass

    def to_pylist(self): # real signature unknown; restored from __doc__
        """
        Array.to_pylist(self)
        
                Convert to a list of native Python objects.
        
                Returns
                -------
                lst : list
        """
        pass

    def to_string(self, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        Array.to_string(self, *, int indent=2, int top_level_indent=0, int window=10, int container_window=2, bool skip_new_lines=False)
        
                Render a "pretty-printed" string representation of the Array.
        
                Parameters
                ----------
                indent : int, default 2
                    How much to indent the internal items in the string to
                    the right, by default ``2``.
                top_level_indent : int, default 0
                    How much to indent right the entire content of the array,
                    by default ``0``.
                window : int
                    How many primitive items to preview at the begin and end
                    of the array when the array is bigger than the window.
                    The other items will be ellipsed.
                container_window : int
                    How many container items (such as a list in a list array)
                    to preview at the begin and end of the array when the array
                    is bigger than the window.
                skip_new_lines : bool
                    If the array should be rendered as a single line of text
                    or if each element should be on its own line.
        """
        pass

    def unique(self): # real signature unknown; restored from __doc__
        """
        Array.unique(self)
        
                Compute distinct elements in array.
        
                Returns
                -------
                unique : Array
                    An array of the same data type, with deduplicated elements.
        """
        pass

    def validate(self, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        Array.validate(self, *, full=False)
        
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
        Array.value_counts(self)
        
                Compute counts of unique elements in array.
        
                Returns
                -------
                StructArray
                    An array of  <input type "Values", int64 "Counts"> structs
        """
        pass

    def view(self, target_type): # real signature unknown; restored from __doc__
        """
        Array.view(self, target_type)
        
                Return zero-copy "view" of array as another data type.
        
                The data types must have compatible columnar buffer layouts
        
                Parameters
                ----------
                target_type : DataType
                    Type to construct view as.
        
                Returns
                -------
                view : Array
        """
        pass

    def _debug_print(self): # real signature unknown; restored from __doc__
        """ Array._debug_print(self) """
        pass

    def _export_to_c(self, out_ptr, out_schema_ptr=0): # real signature unknown; restored from __doc__
        """
        Array._export_to_c(self, out_ptr, out_schema_ptr=0)
        
                Export to a C ArrowArray struct, given its pointer.
        
                If a C ArrowSchema struct pointer is also given, the array type
                is exported to it at the same time.
        
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

    def _import_from_c(self, in_ptr, type): # real signature unknown; restored from __doc__
        """
        Array._import_from_c(in_ptr, type)
        
                Import Array from a C ArrowArray struct, given its pointer
                and the imported array type.
        
                Parameters
                ----------
                in_ptr: int
                    The raw pointer to a C ArrowArray struct.
                type: DataType or int
                    Either a DataType object, or the raw pointer to a C ArrowSchema
                    struct.
        
                This is a low-level function intended for expert users.
        """
        pass

    def _to_pandas(self, options, types_mapper=None, **kwargs): # real signature unknown; restored from __doc__
        """ Array._to_pandas(self, options, types_mapper=None, **kwargs) """
        pass

    def __array__(self, dtype=None): # real signature unknown; restored from __doc__
        """ Array.__array__(self, dtype=None) """
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
                value : Scalar (index) or Array (slice)
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
        """ Array.__reduce__(self) """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __sizeof__(self): # real signature unknown; restored from __doc__
        """ Array.__sizeof__(self) """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    nbytes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Total number of bytes consumed by the elements of the array.

        In other words, the sum of bytes from all buffer
        ranges referenced.

        Unlike `get_total_buffer_size` this method will account for array
        offsets.

        If buffers are shared between arrays then the shared
        portion will be counted multiple times.

        The dictionary of dictionary arrays will always be counted in their
        entirety even if the array only references a portion of the dictionary.
        """

    null_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    offset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        A relative position into another array's data.

        The purpose is to enable zero-copy slicing. This value defaults to zero
        but must be applied on all operations with the physical storage
        buffers.
        """

    type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __hash__ = None
    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001970BC82F00>'


