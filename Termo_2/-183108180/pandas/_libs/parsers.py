# encoding: utf-8
# module pandas._libs.parsers
# from C:\Users\akharin\PycharmProjects\pythonProject\venv\lib\site-packages\pandas\_libs\parsers.cp39-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import inspect as inspect # C:\Users\akharin\AppData\Local\Programs\Python\Python39\lib\inspect.py
import sys as sys # <module 'sys' (built-in)>
import time as time # <module 'time' (built-in)>
import warnings as warnings # C:\Users\akharin\AppData\Local\Programs\Python\Python39\lib\warnings.py
import numpy as np # C:\Users\akharin\PycharmProjects\pythonProject\venv\lib\site-packages\numpy\__init__.py
import pandas._libs.lib as lib # C:\Users\akharin\PycharmProjects\pythonProject\venv\lib\site-packages\pandas\_libs\lib.cp39-win_amd64.pyd
import numpy as __numpy
import pandas.core.dtypes.base as __pandas_core_dtypes_base
import pandas.core.dtypes.dtypes as __pandas_core_dtypes_dtypes


# Variables with simple values

ENOENT = 2

QUOTE_MINIMAL = 0
QUOTE_NONE = 3
QUOTE_NONNUMERIC = 2

# functions

def decode(input, output): # reliably restored by inspect
    """ Decode a file; input and output are binary files. """
    pass

def find_stack_level(): # reliably restored by inspect
    """
    Find the first place in the stack that is not inside pandas
        (tests notwithstanding).
    """
    pass

def is_bool_dtype(arr_or_dtype): # reliably restored by inspect
    """
    Check whether the provided array or dtype is of a boolean dtype.
    
        Parameters
        ----------
        arr_or_dtype : array-like or dtype
            The array or dtype to check.
    
        Returns
        -------
        boolean
            Whether or not the array or dtype is of a boolean dtype.
    
        Notes
        -----
        An ExtensionArray is considered boolean when the ``_is_boolean``
        attribute is set to True.
    
        Examples
        --------
        >>> is_bool_dtype(str)
        False
        >>> is_bool_dtype(int)
        False
        >>> is_bool_dtype(bool)
        True
        >>> is_bool_dtype(np.bool_)
        True
        >>> is_bool_dtype(np.array(['a', 'b']))
        False
        >>> is_bool_dtype(pd.Series([1, 2]))
        False
        >>> is_bool_dtype(np.array([True, False]))
        True
        >>> is_bool_dtype(pd.Categorical([True, False]))
        True
        >>> is_bool_dtype(pd.arrays.SparseArray([True, False]))
        True
    """
    pass

def is_datetime64_dtype(arr_or_dtype): # reliably restored by inspect
    """
    Check whether an array-like or dtype is of the datetime64 dtype.
    
        Parameters
        ----------
        arr_or_dtype : array-like or dtype
            The array-like or dtype to check.
    
        Returns
        -------
        boolean
            Whether or not the array-like or dtype is of the datetime64 dtype.
    
        Examples
        --------
        >>> is_datetime64_dtype(object)
        False
        >>> is_datetime64_dtype(np.datetime64)
        True
        >>> is_datetime64_dtype(np.array([], dtype=int))
        False
        >>> is_datetime64_dtype(np.array([], dtype=np.datetime64))
        True
        >>> is_datetime64_dtype([1, 2, 3])
        False
    """
    pass

def is_dict_like(obj): # reliably restored by inspect
    """
    Check if the object is dict-like.
    
        Parameters
        ----------
        obj : The object to check
    
        Returns
        -------
        is_dict_like : bool
            Whether `obj` has dict-like properties.
    
        Examples
        --------
        >>> is_dict_like({1: 2})
        True
        >>> is_dict_like([1, 2, 3])
        False
        >>> is_dict_like(dict)
        False
        >>> is_dict_like(dict())
        True
    """
    pass

def is_extension_array_dtype(arr_or_dtype): # reliably restored by inspect
    """
    Check if an object is a pandas extension array type.
    
        See the :ref:`Use Guide <extending.extension-types>` for more.
    
        Parameters
        ----------
        arr_or_dtype : object
            For array-like input, the ``.dtype`` attribute will
            be extracted.
    
        Returns
        -------
        bool
            Whether the `arr_or_dtype` is an extension array type.
    
        Notes
        -----
        This checks whether an object implements the pandas extension
        array interface. In pandas, this includes:
    
        * Categorical
        * Sparse
        * Interval
        * Period
        * DatetimeArray
        * TimedeltaArray
    
        Third-party libraries may implement arrays or types satisfying
        this interface as well.
    
        Examples
        --------
        >>> from pandas.api.types import is_extension_array_dtype
        >>> arr = pd.Categorical(['a', 'b'])
        >>> is_extension_array_dtype(arr)
        True
        >>> is_extension_array_dtype(arr.dtype)
        True
    
        >>> arr = np.array(['a', 'b'])
        >>> is_extension_array_dtype(arr.dtype)
        False
    """
    pass

def is_float_dtype(arr_or_dtype): # reliably restored by inspect
    """
    Check whether the provided array or dtype is of a float dtype.
    
        Parameters
        ----------
        arr_or_dtype : array-like or dtype
            The array or dtype to check.
    
        Returns
        -------
        boolean
            Whether or not the array or dtype is of a float dtype.
    
        Examples
        --------
        >>> is_float_dtype(str)
        False
        >>> is_float_dtype(int)
        False
        >>> is_float_dtype(float)
        True
        >>> is_float_dtype(np.array(['a', 'b']))
        False
        >>> is_float_dtype(pd.Series([1, 2]))
        False
        >>> is_float_dtype(pd.Index([1, 2.]))
        True
    """
    pass

def is_integer_dtype(arr_or_dtype): # reliably restored by inspect
    """
    Check whether the provided array or dtype is of an integer dtype.
    
        Unlike in `is_any_int_dtype`, timedelta64 instances will return False.
    
        The nullable Integer dtypes (e.g. pandas.Int64Dtype) are also considered
        as integer by this function.
    
        Parameters
        ----------
        arr_or_dtype : array-like or dtype
            The array or dtype to check.
    
        Returns
        -------
        boolean
            Whether or not the array or dtype is of an integer dtype and
            not an instance of timedelta64.
    
        Examples
        --------
        >>> is_integer_dtype(str)
        False
        >>> is_integer_dtype(int)
        True
        >>> is_integer_dtype(float)
        False
        >>> is_integer_dtype(np.uint64)
        True
        >>> is_integer_dtype('int8')
        True
        >>> is_integer_dtype('Int8')
        True
        >>> is_integer_dtype(pd.Int8Dtype)
        True
        >>> is_integer_dtype(np.datetime64)
        False
        >>> is_integer_dtype(np.timedelta64)
        False
        >>> is_integer_dtype(np.array(['a', 'b']))
        False
        >>> is_integer_dtype(pd.Series([1, 2]))
        True
        >>> is_integer_dtype(np.array([], dtype=np.timedelta64))
        False
        >>> is_integer_dtype(pd.Index([1, 2.]))  # float
        False
    """
    pass

def is_object_dtype(arr_or_dtype): # reliably restored by inspect
    """
    Check whether an array-like or dtype is of the object dtype.
    
        Parameters
        ----------
        arr_or_dtype : array-like or dtype
            The array-like or dtype to check.
    
        Returns
        -------
        boolean
            Whether or not the array-like or dtype is of the object dtype.
    
        Examples
        --------
        >>> is_object_dtype(object)
        True
        >>> is_object_dtype(int)
        False
        >>> is_object_dtype(np.array([], dtype=object))
        True
        >>> is_object_dtype(np.array([], dtype=int))
        False
        >>> is_object_dtype([1, 2, 3])
        False
    """
    pass

def sanitize_objects(*args, **kwargs): # real signature unknown
    """
    Convert specified values, including the given set na_values to np.nan.
    
        Parameters
        ----------
        values : ndarray[object]
        na_values : set
    
        Returns
        -------
        na_count : int
    """
    pass

def _compute_na_values(*args, **kwargs): # real signature unknown
    pass

def _ensure_encoded(*args, **kwargs): # real signature unknown
    pass

def _maybe_upcast(*args, **kwargs): # real signature unknown
    """  """
    pass

def __pyx_unpickle_Enum(*args, **kwargs): # real signature unknown
    pass

# classes

class CategoricalDtype(__pandas_core_dtypes_dtypes.PandasExtensionDtype, __pandas_core_dtypes_base.ExtensionDtype):
    """
    Type for categorical data with the categories and orderedness.
    
        Parameters
        ----------
        categories : sequence, optional
            Must be unique, and must not contain any nulls.
            The categories are stored in an Index,
            and if an index is provided the dtype of that index will be used.
        ordered : bool or None, default False
            Whether or not this categorical is treated as a ordered categorical.
            None can be used to maintain the ordered value of existing categoricals when
            used in operations that combine categoricals, e.g. astype, and will resolve to
            False if there is no existing ordered to maintain.
    
        Attributes
        ----------
        categories
        ordered
    
        Methods
        -------
        None
    
        See Also
        --------
        Categorical : Represent a categorical variable in classic R / S-plus fashion.
    
        Notes
        -----
        This class is useful for specifying the type of a ``Categorical``
        independent of the values. See :ref:`categorical.categoricaldtype`
        for more.
    
        Examples
        --------
        >>> t = pd.CategoricalDtype(categories=['b', 'a'], ordered=True)
        >>> pd.Series(['a', 'b', 'a', 'c'], dtype=t)
        0      a
        1      b
        2      a
        3    NaN
        dtype: category
        Categories (2, object): ['b' < 'a']
    
        An empty CategoricalDtype with a specific dtype can be created
        by providing an empty index. As follows,
    
        >>> pd.CategoricalDtype(pd.DatetimeIndex([])).categories.dtype
        dtype('<M8[ns]')
    """
    @classmethod
    def construct_array_type(cls, *args, **kwargs): # real signature unknown
        """
        Return the array type associated with this dtype.
        
                Returns
                -------
                type
        """
        pass

    @classmethod
    def construct_from_string(cls, *args, **kwargs): # real signature unknown
        """
        Construct a CategoricalDtype from a string.
        
                Parameters
                ----------
                string : str
                    Must be the string "category" in order to be successfully constructed.
        
                Returns
                -------
                CategoricalDtype
                    Instance of the dtype.
        
                Raises
                ------
                TypeError
                    If a CategoricalDtype cannot be constructed from the input.
        """
        pass

    def update_dtype(self, dtype): # reliably restored by inspect
        """
        Returns a CategoricalDtype with categories and ordered taken from dtype
                if specified, otherwise falling back to self if unspecified
        
                Parameters
                ----------
                dtype : CategoricalDtype
        
                Returns
                -------
                new_dtype : CategoricalDtype
        """
        pass

    def validate_categories(categories, fastpath=False): # reliably restored by inspect
        """
        Validates that we have good categories
        
                Parameters
                ----------
                categories : array-like
                fastpath : bool
                    Whether to skip nan and uniqueness checks
        
                Returns
                -------
                categories : Index
        """
        pass

    def validate_ordered(ordered): # reliably restored by inspect
        """
        Validates that we have a valid ordered parameter. If
                it is not a boolean, a TypeError will be raised.
        
                Parameters
                ----------
                ordered : object
                    The parameter to be verified.
        
                Raises
                ------
                TypeError
                    If 'ordered' is not a boolean.
        """
        pass

    def _finalize(self, categories, ordered, fastpath=False): # reliably restored by inspect
        # no doc
        pass

    @classmethod
    def _from_categorical_dtype(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def _from_fastpath(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def _from_values_or_dtype(cls): # real signature unknown; restored from __doc__
        """
        Construct dtype from the input parameters used in :class:`Categorical`.
        
                This constructor method specifically does not do the factorization
                step, if that is needed to find the categories. This constructor may
                therefore return ``CategoricalDtype(categories=None, ordered=None)``,
                which may not be useful. Additional steps may therefore have to be
                taken to create the final dtype.
        
                The return dtype is specified from the inputs in this prioritized
                order:
                1. if dtype is a CategoricalDtype, return dtype
                2. if dtype is the string 'category', create a CategoricalDtype from
                   the supplied categories and ordered parameters, and return that.
                3. if values is a categorical, use value.dtype, but override it with
                   categories and ordered if either/both of those are not None.
                4. if dtype is None and values is not a categorical, construct the
                   dtype from categories and ordered, even if either of those is None.
        
                Parameters
                ----------
                values : list-like, optional
                    The list-like must be 1-dimensional.
                categories : list-like, optional
                    Categories for the CategoricalDtype.
                ordered : bool, optional
                    Designating if the categories are ordered.
                dtype : CategoricalDtype or the string "category", optional
                    If ``CategoricalDtype``, cannot be used together with
                    `categories` or `ordered`.
        
                Returns
                -------
                CategoricalDtype
        
                Examples
                --------
                >>> pd.CategoricalDtype._from_values_or_dtype()
                CategoricalDtype(categories=None, ordered=None)
                >>> pd.CategoricalDtype._from_values_or_dtype(
                ...     categories=['a', 'b'], ordered=True
                ... )
                CategoricalDtype(categories=['a', 'b'], ordered=True)
                >>> dtype1 = pd.CategoricalDtype(['a', 'b'], ordered=True)
                >>> dtype2 = pd.CategoricalDtype(['x', 'y'], ordered=False)
                >>> c = pd.Categorical([0, 1], dtype=dtype1, fastpath=True)
                >>> pd.CategoricalDtype._from_values_or_dtype(
                ...     c, ['x', 'y'], ordered=True, dtype=dtype2
                ... )
                Traceback (most recent call last):
                    ...
                ValueError: Cannot specify `categories` or `ordered` together with
                `dtype`.
        
                The supplied dtype takes precedence over values' dtype:
        
                >>> pd.CategoricalDtype._from_values_or_dtype(c, dtype=dtype2)
                CategoricalDtype(categories=['x', 'y'], ordered=False)
        """
        pass

    def _get_common_dtype(self, dtypes): # reliably restored by inspect
        # no doc
        pass

    def __eq__(self, other): # reliably restored by inspect
        """
        Rules for CDT equality:
                1) Any CDT is equal to the string 'category'
                2) Any CDT is equal to itself
                3) Any CDT is equal to a CDT with categories=None regardless of ordered
                4) A CDT with ordered=True is only equal to another CDT with
                   ordered=True and identical categories in the same order
                5) A CDT with ordered={False, None} is only equal to another CDT with
                   ordered={False, None} and identical categories, but same order is
                   not required. There is no distinction between False/None.
                6) Any other comparison returns False
        """
        pass

    def __hash__(self): # reliably restored by inspect
        # no doc
        pass

    def __init__(self, categories=None, ordered=False): # reliably restored by inspect
        # no doc
        pass

    def __repr__(self): # reliably restored by inspect
        # no doc
        pass

    def __setstate__(self, state): # reliably restored by inspect
        # no doc
        pass

    categories = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        An ``Index`` containing the unique categories allowed.
        """

    ordered = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Whether the categories have an ordered relationship.
        """

    _is_boolean = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    base = dtype('O')
    kind = 'O'
    name = 'category'
    str = '|O08'
    type = None # (!) real value is "<class 'pandas.core.dtypes.dtypes.CategoricalDtypeType'>"
    _cache_dtypes = {}
    _hash_categories = None # (!) real value is '<pandas._libs.properties.CachedProperty object at 0x00000195535654C0>'
    _metadata = (
        'categories',
        'ordered',
    )
    __annotations__ = {
        '_cache_dtypes': 'dict[str_type, PandasExtensionDtype]',
        'kind': 'str_type',
        'type': 'type[CategoricalDtypeType]',
    }


class defaultdict(dict):
    """
    defaultdict(default_factory=None, /, [...]) --> dict with default factory
    
    The default factory is called without arguments to produce
    a new value when a key is not present, in __getitem__ only.
    A defaultdict compares equal to a dict with the same items.
    All remaining arguments are treated the same as if they were
    passed to the dict constructor, including keyword arguments.
    """
    def copy(self): # real signature unknown; restored from __doc__
        """ D.copy() -> a shallow copy of D. """
        pass

    @classmethod
    def __class_getitem__(cls, *args, **kwargs): # real signature unknown
        """ See PEP 585 """
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        """ D.copy() -> a shallow copy of D. """
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __init__(self, default_factory=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    def __missing__(self, key): # real signature unknown; restored from __doc__
        """
        __missing__(key) # Called by __getitem__ for missing key; pseudo-code:
          if self.default_factory is None: raise KeyError((key,))
          self[key] = value = self.default_factory()
          return value
        """
        pass

    def __or__(self, *args, **kwargs): # real signature unknown
        """ Return self|value. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ Return state information for pickling. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __ror__(self, *args, **kwargs): # real signature unknown
        """ Return value|self. """
        pass

    default_factory = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Factory for default value called by __missing__()."""



class EmptyDataError(ValueError):
    """ Exception raised in ``pd.read_csv`` when empty data or header is encountered. """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class k(__numpy.generic):
    """
    Any Python object.
    
        :Character code: ``'O'``
    """
    def __add__(self, *args, **kwargs): # real signature unknown
        """ Return self+value. """
        pass

    def __call__(self, *args, **kwargs): # real signature unknown
        """ Call self as a function. """
        pass

    def __contains__(self, *args, **kwargs): # real signature unknown
        """ Return key in self. """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __delitem__(self, *args, **kwargs): # real signature unknown
        """ Delete self[key]. """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
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

    def __iadd__(self, *args, **kwargs): # real signature unknown
        """ Implement self+=value. """
        pass

    def __imul__(self, *args, **kwargs): # real signature unknown
        """ Implement self*=value. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
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

    def __mul__(self, *args, **kwargs): # real signature unknown
        """ Return self*value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        """ Return value*self. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    def __setitem__(self, *args, **kwargs): # real signature unknown
        """ Set self[key] to value. """
        pass


class ParserError(ValueError):
    """
    Exception that is raised by an error encountered in parsing file contents.
    
        This is a generic error raised for errors encountered when functions like
        `read_csv` or `read_html` are parsing contents of a file.
    
        See Also
        --------
        read_csv : Read CSV (comma-separated) file into a DataFrame.
        read_html : Read HTML table into a DataFrame.
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class ParserWarning(Warning):
    """
    Warning raised when reading a file that doesn't use the default 'c' parser.
    
        Raised by `pd.read_csv` and `pd.read_table` when it is necessary to change
        parsers, generally from the default 'c' parser to 'python'.
    
        It happens due to a lack of support or functionality for parsing a
        particular attribute of a CSV file with the requested engine.
    
        Currently, 'c' unsupported options include the following parameters:
    
        1. `sep` other than a single character (e.g. regex separators)
        2. `skipfooter` higher than 0
        3. `sep=None` with `delim_whitespace=False`
    
        The warning can be avoided by adding `engine='python'` as a parameter in
        `pd.read_csv` and `pd.read_table` methods.
    
        See Also
        --------
        pd.read_csv : Read CSV (comma-separated) file into DataFrame.
        pd.read_table : Read general delimited file into DataFrame.
    
        Examples
        --------
        Using a `sep` in `pd.read_csv` other than a single character:
    
        >>> import io
        >>> csv = '''a;b;c
        ...           1;1,8
        ...           1;2,1'''
        >>> df = pd.read_csv(io.StringIO(csv), sep='[;,]')  # doctest: +SKIP
        ... # ParserWarning: Falling back to the 'python' engine...
    
        Adding `engine='python'` to `pd.read_csv` removes the Warning:
    
        >>> df = pd.read_csv(io.StringIO(csv), sep='[;,]', engine='python')
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class TextReader(object):
    """
    # source: StringIO or file object
    
        ..versionchange:: 1.2.0
            removed 'compression', 'memory_map', and 'encoding' argument.
            These arguments are outsourced to CParserWrapper.
            'source' has to be a file handle.
    """
    def close(self, *args, **kwargs): # real signature unknown
        pass

    def read(self, *args, **kwargs): # real signature unknown
        """ rows=None --> read all rows """
        pass

    def read_low_memory(self, *args, **kwargs): # real signature unknown
        """ rows=None --> read all rows """
        pass

    def remove_noconvert(self, *args, **kwargs): # real signature unknown
        pass

    def set_noconvert(self, *args, **kwargs): # real signature unknown
        pass

    def _convert_column_data(self, *args, **kwargs): # real signature unknown
        pass

    def _get_converter(self, *args, **kwargs): # real signature unknown
        pass

    def _set_quoting(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    converters = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    delimiter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dtype = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    header = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    index_col = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    leading_cols = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    na_values = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    skiprows = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    table_width = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    unnamed_cols = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    usecols = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x0000019554298B40>'


# variables with complex values

na_values = {
    np.double: 
        nan
    ,
    np.intp: 
        -9223372036854775808
    ,
    np.int32: 
        -2147483648
    ,
    np.short: 
        -32768
    ,
    np.byte: 
        -128
    ,
    np.uintp: 
        18446744073709551615
    ,
    np.uint: 
        4294967295
    ,
    np.ushort: 
        65535
    ,
    np.ubyte: 
        255
    ,
    np.bool_: 
        255
    ,
    np.object_: 
        nan
    ,
    dtype('float64'): 
        nan
    ,
    dtype('int64'): 
        -9223372036854775808
    ,
    dtype('int32'): 
        -2147483648
    ,
    dtype('int16'): 
        -32768
    ,
    dtype('int8'): 
        -128
    ,
    dtype('uint64'): 
        18446744073709551615
    ,
    dtype('uint32'): 
        4294967295
    ,
    dtype('uint16'): 
        65535
    ,
    dtype('uint8'): 
        255
    ,
    dtype('bool'): 
        255
    ,
    dtype('O'): 
        nan
    ,
}

STR_NA_VALUES = None # (!) real value is "{'', '-nan', 'NaN', '<NA>', '-NaN', '1.#QNAN', 'NULL', 'nan', '#N/A', '1.#IND', '#N/A N/A', '#NA', 'null', 'NA', 'n/a', '-1.#IND', 'N/A', '-1.#QNAN'}"

_NA_VALUES = [
    b'',
    b'-nan',
    b'NaN',
    b'<NA>',
    b'-NaN',
    b'1.#QNAN',
    b'NULL',
    b'nan',
    b'#N/A',
    b'1.#IND',
    b'#N/A N/A',
    b'#NA',
    b'null',
    b'NA',
    b'n/a',
    b'-1.#IND',
    b'N/A',
    b'-1.#QNAN',
]

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x00000195542982E0>'

__spec__ = None # (!) real value is "ModuleSpec(name='pandas._libs.parsers', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x00000195542982E0>, origin='C:\\\\Users\\\\akharin\\\\PycharmProjects\\\\pythonProject\\\\venv\\\\lib\\\\site-packages\\\\pandas\\\\_libs\\\\parsers.cp39-win_amd64.pyd')"

__test__ = {}

