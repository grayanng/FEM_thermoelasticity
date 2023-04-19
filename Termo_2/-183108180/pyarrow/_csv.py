# encoding: utf-8
# module pyarrow._csv
# from C:\Users\akharin\PycharmProjects\pythonProject\venv\lib\site-packages\pyarrow\_csv.cp39-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import codecs as codecs # C:\Users\akharin\AppData\Local\Programs\Python\Python39\lib\codecs.py
from pyarrow.lib import SignalStopHandler, frombytes, tobytes

import collections.abc as __collections_abc
import pyarrow.lib as __pyarrow_lib


# functions

def namedtuple(typename, field_names, *, rename=False, defaults=None, module=None): # reliably restored by inspect
    """
    Returns a new subclass of tuple with named fields.
    
        >>> Point = namedtuple('Point', ['x', 'y'])
        >>> Point.__doc__                   # docstring for the new class
        'Point(x, y)'
        >>> p = Point(11, y=22)             # instantiate with positional args or keywords
        >>> p[0] + p[1]                     # indexable like a plain tuple
        33
        >>> x, y = p                        # unpack like a regular tuple
        >>> x, y
        (11, 22)
        >>> p.x + p.y                       # fields also accessible by name
        33
        >>> d = p._asdict()                 # convert to a dictionary
        >>> d['x']
        11
        >>> Point(**d)                      # convert from a dictionary
        Point(x=11, y=22)
        >>> p._replace(x=100)               # _replace() is like str.replace() but targets named fields
        Point(x=100, y=22)
    """
    pass

def open_csv(input_file, read_options=None, parse_options=None, convert_options=None, MemoryPool_memory_pool=None): # real signature unknown; restored from __doc__
    """
    open_csv(input_file, read_options=None, parse_options=None, convert_options=None, MemoryPool memory_pool=None)
    
        Open a streaming reader of CSV data.
    
        Reading using this function is always single-threaded.
    
        Parameters
        ----------
        input_file : string, path or file-like object
            The location of CSV data.  If a string or path, and if it ends
            with a recognized compressed file extension (e.g. ".gz" or ".bz2"),
            the data is automatically decompressed when reading.
        read_options : pyarrow.csv.ReadOptions, optional
            Options for the CSV reader (see pyarrow.csv.ReadOptions constructor
            for defaults)
        parse_options : pyarrow.csv.ParseOptions, optional
            Options for the CSV parser
            (see pyarrow.csv.ParseOptions constructor for defaults)
        convert_options : pyarrow.csv.ConvertOptions, optional
            Options for converting CSV data
            (see pyarrow.csv.ConvertOptions constructor for defaults)
        memory_pool : MemoryPool, optional
            Pool to allocate Table memory from
    
        Returns
        -------
        :class:`pyarrow.csv.CSVStreamingReader`
    """
    pass

def read_csv(input_file, read_options=None, parse_options=None, convert_options=None, MemoryPool_memory_pool=None): # real signature unknown; restored from __doc__
    """
    read_csv(input_file, read_options=None, parse_options=None, convert_options=None, MemoryPool memory_pool=None)
    
        Read a Table from a stream of CSV data.
    
        Parameters
        ----------
        input_file : string, path or file-like object
            The location of CSV data.  If a string or path, and if it ends
            with a recognized compressed file extension (e.g. ".gz" or ".bz2"),
            the data is automatically decompressed when reading.
        read_options : pyarrow.csv.ReadOptions, optional
            Options for the CSV reader (see pyarrow.csv.ReadOptions constructor
            for defaults)
        parse_options : pyarrow.csv.ParseOptions, optional
            Options for the CSV parser
            (see pyarrow.csv.ParseOptions constructor for defaults)
        convert_options : pyarrow.csv.ConvertOptions, optional
            Options for converting CSV data
            (see pyarrow.csv.ConvertOptions constructor for defaults)
        memory_pool : MemoryPool, optional
            Pool to allocate Table memory from
    
        Returns
        -------
        :class:`pyarrow.Table`
            Contents of the CSV file as a in-memory table.
    
        Examples
        --------
    
        Defining an example file from bytes object:
    
        >>> import io
        >>> s = "animals,n_legs,entry\nFlamingo,2,2022-03-01\nHorse,4,2022-03-02\nBrittle stars,5,2022-03-03\nCentipede,100,2022-03-04"
        >>> print(s)
        animals,n_legs,entry
        Flamingo,2,2022-03-01
        Horse,4,2022-03-02
        Brittle stars,5,2022-03-03
        Centipede,100,2022-03-04
        >>> source = io.BytesIO(s.encode())
    
        Reading from the file
    
        >>> from pyarrow import csv
        >>> csv.read_csv(source)
        pyarrow.Table
        animals: string
        n_legs: int64
        entry: date32[day]
        ----
        animals: [["Flamingo","Horse","Brittle stars","Centipede"]]
        n_legs: [[2,4,5,100]]
        entry: [[2022-03-01,2022-03-02,2022-03-03,2022-03-04]]
    """
    pass

def write_csv(data, output_file, write_options=None, MemoryPool_memory_pool=None): # real signature unknown; restored from __doc__
    """
    write_csv(data, output_file, write_options=None, MemoryPool memory_pool=None)
    
        Write record batch or table to a CSV file.
    
        Parameters
        ----------
        data : pyarrow.RecordBatch or pyarrow.Table
            The data to write.
        output_file : string, path, pyarrow.NativeFile, or file-like object
            The location where to write the CSV data.
        write_options : pyarrow.csv.WriteOptions
            Options to configure writing the CSV data.
        memory_pool : MemoryPool, optional
            Pool for temporary allocations.
    
        Examples
        --------
    
        >>> import pyarrow as pa
        >>> from pyarrow import csv
    
        >>> legs = pa.array([2, 4, 5, 100])
        >>> animals = pa.array(["Flamingo", "Horse", "Brittle stars", "Centipede"])
        >>> entry_date = pa.array(["01/03/2022", "02/03/2022",
        ...                        "03/03/2022", "04/03/2022"])
        >>> table = pa.table([animals, legs, entry_date],
        ...                  names=["animals", "n_legs", "entry"])
    
        >>> csv.write_csv(table, "animals.csv")
    
        >>> write_options = csv.WriteOptions(include_header=False)
        >>> csv.write_csv(table, "animals.csv", write_options=write_options)
    
        >>> write_options = csv.WriteOptions(delimiter=";")
        >>> csv.write_csv(table, "animals.csv", write_options=write_options)
    """
    pass

def _raise_invalid_function_option(value, description, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """ _raise_invalid_function_option(value, description, *, exception_class=ValueError) """
    pass

def _stringify_path(path): # reliably restored by inspect
    """ Convert *path* to a string or unicode path if possible. """
    pass

def __pyx_unpickle__ISO8601(__pyx_type, long___pyx_checksum, __pyx_state): # real signature unknown; restored from __doc__
    """ __pyx_unpickle__ISO8601(__pyx_type, long __pyx_checksum, __pyx_state) """
    pass

# classes

class ConvertOptions(__pyarrow_lib._Weakrefable):
    """
    ConvertOptions(check_utf8=None, *, column_types=None, null_values=None, true_values=None, false_values=None, decimal_point=None, strings_can_be_null=None, quoted_strings_can_be_null=None, include_columns=None, include_missing_columns=None, auto_dict_encode=None, auto_dict_max_cardinality=None, timestamp_parsers=None)
    
        Options for converting CSV data.
    
        Parameters
        ----------
        check_utf8 : bool, optional (default True)
            Whether to check UTF8 validity of string columns.
        column_types : pyarrow.Schema or dict, optional
            Explicitly map column names to column types. Passing this argument
            disables type inference on the defined columns.
        null_values : list, optional
            A sequence of strings that denote nulls in the data
            (defaults are appropriate in most cases). Note that by default,
            string columns are not checked for null values. To enable
            null checking for those, specify ``strings_can_be_null=True``.
        true_values : list, optional
            A sequence of strings that denote true booleans in the data
            (defaults are appropriate in most cases).
        false_values : list, optional
            A sequence of strings that denote false booleans in the data
            (defaults are appropriate in most cases).
        decimal_point : 1-character string, optional (default '.')
            The character used as decimal point in floating-point and decimal
            data.
        strings_can_be_null : bool, optional (default False)
            Whether string / binary columns can have null values.
            If true, then strings in null_values are considered null for
            string columns.
            If false, then all strings are valid string values.
        quoted_strings_can_be_null : bool, optional (default True)
            Whether quoted values can be null.
            If true, then strings in "null_values" are also considered null
            when they appear quoted in the CSV file. Otherwise, quoted values
            are never considered null.
        include_columns : list, optional
            The names of columns to include in the Table.
            If empty, the Table will include all columns from the CSV file.
            If not empty, only these columns will be included, in this order.
        include_missing_columns : bool, optional (default False)
            If false, columns in `include_columns` but not in the CSV file will
            error out.
            If true, columns in `include_columns` but not in the CSV file will
            produce a column of nulls (whose type is selected using
            `column_types`, or null by default).
            This option is ignored if `include_columns` is empty.
        auto_dict_encode : bool, optional (default False)
            Whether to try to automatically dict-encode string / binary data.
            If true, then when type inference detects a string or binary column,
            it it dict-encoded up to `auto_dict_max_cardinality` distinct values
            (per chunk), after which it switches to regular encoding.
            This setting is ignored for non-inferred columns (those in
            `column_types`).
        auto_dict_max_cardinality : int, optional
            The maximum dictionary cardinality for `auto_dict_encode`.
            This value is per chunk.
        timestamp_parsers : list, optional
            A sequence of strptime()-compatible format strings, tried in order
            when attempting to infer or convert timestamp values (the special
            value ISO8601() can also be given).  By default, a fast built-in
            ISO-8601 parser is used.
    
        Examples
        --------
    
        Defining an example data:
    
        >>> import io
        >>> s = "animals,n_legs,entry,fast\nFlamingo,2,01/03/2022,Yes\nHorse,4,02/03/2022,Yes\nBrittle stars,5,03/03/2022,No\nCentipede,100,04/03/2022,No\n,6,05/03/2022,"
        >>> print(s)
        animals,n_legs,entry,fast
        Flamingo,2,01/03/2022,Yes
        Horse,4,02/03/2022,Yes
        Brittle stars,5,03/03/2022,No
        Centipede,100,04/03/2022,No
        ,6,05/03/2022,
    
        Change the type of a column:
    
        >>> import pyarrow as pa
        >>> from pyarrow import csv
        >>> convert_options = csv.ConvertOptions(column_types={"n_legs": pa.float64()})
        >>> csv.read_csv(io.BytesIO(s.encode()), convert_options=convert_options)
        pyarrow.Table
        animals: string
        n_legs: double
        entry: string
        fast: string
        ----
        animals: [["Flamingo","Horse","Brittle stars","Centipede",""]]
        n_legs: [[2,4,5,100,6]]
        entry: [["01/03/2022","02/03/2022","03/03/2022","04/03/2022","05/03/2022"]]
        fast: [["Yes","Yes","No","No",""]]
    
        Define a date parsing format to get a timestamp type column
        (in case dates are not in ISO format and not converted by default):
    
        >>> convert_options = csv.ConvertOptions(
        ...                   timestamp_parsers=["%m/%d/%Y", "%m-%d-%Y"])
        >>> csv.read_csv(io.BytesIO(s.encode()), convert_options=convert_options)
        pyarrow.Table
        animals: string
        n_legs: int64
        entry: timestamp[s]
        fast: string
        ----
        animals: [["Flamingo","Horse","Brittle stars","Centipede",""]]
        n_legs: [[2,4,5,100,6]]
        entry: [[2022-01-03 00:00:00,2022-02-03 00:00:00,2022-03-03 00:00:00,2022-04-03 00:00:00,2022-05-03 00:00:00]]
        fast: [["Yes","Yes","No","No",""]]
    
        Specify a subset of columns to be read:
    
        >>> convert_options = csv.ConvertOptions(
        ...                   include_columns=["animals", "n_legs"])
        >>> csv.read_csv(io.BytesIO(s.encode()), convert_options=convert_options)
        pyarrow.Table
        animals: string
        n_legs: int64
        ----
        animals: [["Flamingo","Horse","Brittle stars","Centipede",""]]
        n_legs: [[2,4,5,100,6]]
    
        List additional column to be included as a null typed column:
    
        >>> convert_options = csv.ConvertOptions(
        ...                   include_columns=["animals", "n_legs", "location"],
        ...                   include_missing_columns=True)
        >>> csv.read_csv(io.BytesIO(s.encode()), convert_options=convert_options)
        pyarrow.Table
        animals: string
        n_legs: int64
        location: null
        ----
        animals: [["Flamingo","Horse","Brittle stars","Centipede",""]]
        n_legs: [[2,4,5,100,6]]
        location: [5 nulls]
    
        Define columns as dictionary type (by default only the
        string/binary columns are dictionary encoded):
    
        >>> convert_options = csv.ConvertOptions(
        ...                   timestamp_parsers=["%m/%d/%Y", "%m-%d-%Y"],
        ...                   auto_dict_encode=True)
        >>> csv.read_csv(io.BytesIO(s.encode()), convert_options=convert_options)
        pyarrow.Table
        animals: dictionary<values=string, indices=int32, ordered=0>
        n_legs: int64
        entry: timestamp[s]
        fast: dictionary<values=string, indices=int32, ordered=0>
        ----
        animals: [  -- dictionary:
        ["Flamingo","Horse","Brittle stars","Centipede",""]  -- indices:
        [0,1,2,3,4]]
        n_legs: [[2,4,5,100,6]]
        entry: [[2022-01-03 00:00:00,2022-02-03 00:00:00,2022-03-03 00:00:00,2022-04-03 00:00:00,2022-05-03 00:00:00]]
        fast: [  -- dictionary:
        ["Yes","No",""]  -- indices:
        [0,0,1,1,2]]
    
        Set upper limit for the number of categories. If the categories
        is more than the limit, the conversion to dictionary will not
        happen:
    
        >>> convert_options = csv.ConvertOptions(
        ...                   include_columns=["animals"],
        ...                   auto_dict_encode=True,
        ...                   auto_dict_max_cardinality=2)
        >>> csv.read_csv(io.BytesIO(s.encode()), convert_options=convert_options)
        pyarrow.Table
        animals: string
        ----
        animals: [["Flamingo","Horse","Brittle stars","Centipede",""]]
    
        Set empty strings to missing values:
    
        >>> convert_options = csv.ConvertOptions(include_columns=["animals", "n_legs"],
        ...                   strings_can_be_null=True)
        >>> csv.read_csv(io.BytesIO(s.encode()), convert_options=convert_options)
        pyarrow.Table
        animals: string
        n_legs: int64
        ----
        animals: [["Flamingo","Horse","Brittle stars","Centipede",null]]
        n_legs: [[2,4,5,100,6]]
    
        Define values to be True and False when converting a column
        into a bool type:
    
        >>> convert_options = csv.ConvertOptions(
        ...                   include_columns=["fast"],
        ...                   false_values=["No"],
        ...                   true_values=["Yes"])
        >>> csv.read_csv(io.BytesIO(s.encode()), convert_options=convert_options)
        pyarrow.Table
        fast: bool
        ----
        fast: [[true,true,false,false,null]]
    """
    def equals(self, ConvertOptions_other): # real signature unknown; restored from __doc__
        """ ConvertOptions.equals(self, ConvertOptions other) """
        pass

    def validate(self): # real signature unknown; restored from __doc__
        """ ConvertOptions.validate(self) """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __getstate__(self): # real signature unknown; restored from __doc__
        """ ConvertOptions.__getstate__(self) """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __init__(self, check_utf8=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
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

    def __reduce_cython__(self): # real signature unknown; restored from __doc__
        """ ConvertOptions.__reduce_cython__(self) """
        pass

    def __setstate_cython__(self, __pyx_state): # real signature unknown; restored from __doc__
        """ ConvertOptions.__setstate_cython__(self, __pyx_state) """
        pass

    def __setstate__(self, state): # real signature unknown; restored from __doc__
        """ ConvertOptions.__setstate__(self, state) """
        pass

    auto_dict_encode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Whether to try to automatically dict-encode string / binary data.
        """

    auto_dict_max_cardinality = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        The maximum dictionary cardinality for `auto_dict_encode`.

        This value is per chunk.
        """

    check_utf8 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Whether to check UTF8 validity of string columns.
        """

    column_types = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Explicitly map column names to column types.
        """

    decimal_point = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        The character used as decimal point in floating-point and decimal
        data.
        """

    false_values = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        A sequence of strings that denote false booleans in the data.
        """

    include_columns = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        The names of columns to include in the Table.

        If empty, the Table will include all columns from the CSV file.
        If not empty, only these columns will be included, in this order.
        """

    include_missing_columns = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        If false, columns in `include_columns` but not in the CSV file will
        error out.
        If true, columns in `include_columns` but not in the CSV file will
        produce a null column (whose type is selected using `column_types`,
        or null by default).
        This option is ignored if `include_columns` is empty.
        """

    null_values = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        A sequence of strings that denote nulls in the data.
        """

    quoted_strings_can_be_null = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Whether quoted values can be null.
        """

    strings_can_be_null = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Whether string / binary columns can have null values.
        """

    timestamp_parsers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        A sequence of strptime()-compatible format strings, tried in order
        when attempting to infer or convert timestamp values (the special
        value ISO8601() can also be given).  By default, a fast built-in
        ISO-8601 parser is used.
        """

    true_values = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        A sequence of strings that denote true booleans in the data.
        """


    __hash__ = None
    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001893F280690>'
    __slots__ = ()


class CSVStreamingReader(__pyarrow_lib.RecordBatchReader):
    """
    CSVStreamingReader()
    An object that reads record batches incrementally from a CSV file.
    
        Should not be instantiated directly by user code.
    """
    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ CSVStreamingReader.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ CSVStreamingReader.__setstate_cython__(self, __pyx_state) """
        pass

    schema = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001894D875C90>'


class CSVWriter(__pyarrow_lib._CRecordBatchWriter):
    """
    CSVWriter(sink, Schema schema, WriteOptions write_options=None, *, MemoryPool memory_pool=None)
    
        Writer to create a CSV file.
    
        Parameters
        ----------
        sink : str, path, pyarrow.OutputStream or file-like object
            The location where to write the CSV data.
        schema : pyarrow.Schema
            The schema of the data to be written.
        write_options : pyarrow.csv.WriteOptions
            Options to configure writing the CSV data.
        memory_pool : MemoryPool, optional
            Pool for temporary allocations.
    """
    def __init__(self, sink, Schema_schema, WriteOptions_write_options=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ CSVWriter.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ CSVWriter.__setstate_cython__(self, __pyx_state) """
        pass


class _InvalidRow(tuple):
    """ _InvalidRow(expected_columns, actual_columns, number, text) """
    def _asdict(self): # reliably restored by inspect
        """ Return a new dict which maps field names to their values. """
        pass

    @classmethod
    def _make(cls, *args, **kwargs): # real signature unknown
        """ Make a new _InvalidRow object from a sequence or iterable """
        pass

    def _replace(self, **kwds): # reliably restored by inspect
        """ Return a new _InvalidRow object replacing specified fields with new values """
        pass

    def __getnewargs__(self): # reliably restored by inspect
        """ Return self as a plain tuple.  Used by copy and pickle. """
        pass

    def __init__(self, expected_columns, actual_columns, number, text): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(_cls, expected_columns, actual_columns, number, text): # reliably restored by inspect
        """ Create new instance of _InvalidRow(expected_columns, actual_columns, number, text) """
        pass

    def __repr__(self): # reliably restored by inspect
        """ Return a nicely formatted representation string """
        pass

    actual_columns = _tuplegetter(1, 'Alias for field number 1')
    expected_columns = _tuplegetter(0, 'Alias for field number 0')
    number = _tuplegetter(2, 'Alias for field number 2')
    text = _tuplegetter(3, 'Alias for field number 3')
    _fields = (
        'expected_columns',
        'actual_columns',
        'number',
        'text',
    )
    _field_defaults = {}
    __slots__ = ()


class InvalidRow(_InvalidRow):
    """
    Description of an invalid row in a CSV file.
    
        Parameters
        ----------
        expected_columns : int
            The expected number of columns in the row.
        actual_columns : int
            The actual number of columns in the row.
        number : int or None
            The physical row number if known, otherwise None.
        text : str
            The contents of the row.
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __slots__ = ()


class Mapping(__collections_abc.Collection):
    # no doc
    def get(self, key, default=None): # reliably restored by inspect
        """ D.get(k[,d]) -> D[k] if k in D, else d.  d defaults to None. """
        pass

    def items(self): # reliably restored by inspect
        """ D.items() -> a set-like object providing a view on D's items """
        pass

    def keys(self): # reliably restored by inspect
        """ D.keys() -> a set-like object providing a view on D's keys """
        pass

    def values(self): # reliably restored by inspect
        """ D.values() -> an object providing a view on D's values """
        pass

    def __contains__(self, key): # reliably restored by inspect
        # no doc
        pass

    def __eq__(self, other): # reliably restored by inspect
        # no doc
        pass

    def __getitem__(self, key): # reliably restored by inspect
        # no doc
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _abc_impl = None # (!) real value is '<_abc._abc_data object at 0x000001893CE48F00>'
    __abstractmethods__ = frozenset({'__iter__', '__getitem__', '__len__'})
    __hash__ = None
    __reversed__ = None
    __slots__ = ()


class ParseOptions(__pyarrow_lib._Weakrefable):
    """
    ParseOptions(delimiter=None, *, quote_char=None, double_quote=None, escape_char=None, newlines_in_values=None, ignore_empty_lines=None, invalid_row_handler=None)
    
        Options for parsing CSV files.
    
        Parameters
        ----------
        delimiter : 1-character string, optional (default ',')
            The character delimiting individual cells in the CSV data.
        quote_char : 1-character string or False, optional (default '"')
            The character used optionally for quoting CSV values
            (False if quoting is not allowed).
        double_quote : bool, optional (default True)
            Whether two quotes in a quoted CSV value denote a single quote
            in the data.
        escape_char : 1-character string or False, optional (default False)
            The character used optionally for escaping special characters
            (False if escaping is not allowed).
        newlines_in_values : bool, optional (default False)
            Whether newline characters are allowed in CSV values.
            Setting this to True reduces the performance of multi-threaded
            CSV reading.
        ignore_empty_lines : bool, optional (default True)
            Whether empty lines are ignored in CSV input.
            If False, an empty line is interpreted as containing a single empty
            value (assuming a one-column CSV file).
        invalid_row_handler : callable, optional (default None)
            If not None, this object is called for each CSV row that fails
            parsing (because of a mismatching number of columns).
            It should accept a single InvalidRow argument and return either
            "skip" or "error" depending on the desired outcome.
    
        Examples
        --------
    
        Defining an example file from bytes object:
    
        >>> import io
        >>> s = "animals;n_legs;entry\nFlamingo;2;2022-03-01\n# Comment here:\nHorse;4;2022-03-02\nBrittle stars;5;2022-03-03\nCentipede;100;2022-03-04"
        >>> print(s)
        animals;n_legs;entry
        Flamingo;2;2022-03-01
        # Comment here:
        Horse;4;2022-03-02
        Brittle stars;5;2022-03-03
        Centipede;100;2022-03-04
        >>> source = io.BytesIO(s.encode())
    
        Read the data from a file skipping rows with comments
        and defining the delimiter:
    
        >>> from pyarrow import csv
        >>> def skip_comment(row):
        ...     if row.text.startswith("# "):
        ...         return 'skip'
        ...     else:
        ...         return 'error'
        ...
        >>> parse_options = csv.ParseOptions(delimiter=";", invalid_row_handler=skip_comment)
        >>> csv.read_csv(source, parse_options=parse_options)
        pyarrow.Table
        animals: string
        n_legs: int64
        entry: date32[day]
        ----
        animals: [["Flamingo","Horse","Brittle stars","Centipede"]]
        n_legs: [[2,4,5,100]]
        entry: [[2022-03-01,2022-03-02,2022-03-03,2022-03-04]]
    """
    def equals(self, ParseOptions_other): # real signature unknown; restored from __doc__
        """ ParseOptions.equals(self, ParseOptions other) """
        pass

    def validate(self): # real signature unknown; restored from __doc__
        """ ParseOptions.validate(self) """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __getstate__(self): # real signature unknown; restored from __doc__
        """ ParseOptions.__getstate__(self) """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __init__(self, delimiter=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
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

    def __reduce_cython__(self): # real signature unknown; restored from __doc__
        """ ParseOptions.__reduce_cython__(self) """
        pass

    def __setstate_cython__(self, __pyx_state): # real signature unknown; restored from __doc__
        """ ParseOptions.__setstate_cython__(self, __pyx_state) """
        pass

    def __setstate__(self, state): # real signature unknown; restored from __doc__
        """ ParseOptions.__setstate__(self, state) """
        pass

    delimiter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        The character delimiting individual cells in the CSV data.
        """

    double_quote = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Whether two quotes in a quoted CSV value denote a single quote
        in the data.
        """

    escape_char = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        The character used optionally for escaping special characters
        (False if escaping is not allowed).
        """

    ignore_empty_lines = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Whether empty lines are ignored in CSV input.
        If False, an empty line is interpreted as containing a single empty
        value (assuming a one-column CSV file).
        """

    invalid_row_handler = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Optional handler for invalid rows.

        If not None, this object is called for each CSV row that fails
        parsing (because of a mismatching number of columns).
        It should accept a single InvalidRow argument and return either
        "skip" or "error" depending on the desired outcome.
        """

    newlines_in_values = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Whether newline characters are allowed in CSV values.
        Setting this to True reduces the performance of multi-threaded
        CSV reading.
        """

    quote_char = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        The character used optionally for quoting CSV values
        (False if quoting is not allowed).
        """


    __hash__ = None
    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001894D875B40>'
    __slots__ = ()


class ReadOptions(__pyarrow_lib._Weakrefable):
    """
    ReadOptions(use_threads=None, *, block_size=None, skip_rows=None, skip_rows_after_names=None, column_names=None, autogenerate_column_names=None, encoding=u'utf8')
    
        Options for reading CSV files.
    
        Parameters
        ----------
        use_threads : bool, optional (default True)
            Whether to use multiple threads to accelerate reading
        block_size : int, optional
            How much bytes to process at a time from the input stream.
            This will determine multi-threading granularity as well as
            the size of individual record batches or table chunks.
            Minimum valid value for block size is 1
        skip_rows : int, optional (default 0)
            The number of rows to skip before the column names (if any)
            and the CSV data.
        skip_rows_after_names : int, optional (default 0)
            The number of rows to skip after the column names.
            This number can be larger than the number of rows in one
            block, and empty rows are counted.
            The order of application is as follows:
            - `skip_rows` is applied (if non-zero);
            - column names aread (unless `column_names` is set);
            - `skip_rows_after_names` is applied (if non-zero).
        column_names : list, optional
            The column names of the target table.  If empty, fall back on
            `autogenerate_column_names`.
        autogenerate_column_names : bool, optional (default False)
            Whether to autogenerate column names if `column_names` is empty.
            If true, column names will be of the form "f0", "f1"...
            If false, column names will be read from the first CSV row
            after `skip_rows`.
        encoding : str, optional (default 'utf8')
            The character encoding of the CSV data.  Columns that cannot
            decode using this encoding can still be read as Binary.
    
        Examples
        --------
    
        Defining an example data:
    
        >>> import io
        >>> s = "1,2,3\nFlamingo,2,2022-03-01\nHorse,4,2022-03-02\nBrittle stars,5,2022-03-03\nCentipede,100,2022-03-04"
        >>> print(s)
        1,2,3
        Flamingo,2,2022-03-01
        Horse,4,2022-03-02
        Brittle stars,5,2022-03-03
        Centipede,100,2022-03-04
    
        Ignore the first numbered row and substitute it with defined
        or autogenerated column names:
    
        >>> from pyarrow import csv
        >>> read_options = csv.ReadOptions(
        ...                column_names=["animals", "n_legs", "entry"],
        ...                skip_rows=1)
        >>> csv.read_csv(io.BytesIO(s.encode()), read_options=read_options)
        pyarrow.Table
        animals: string
        n_legs: int64
        entry: date32[day]
        ----
        animals: [["Flamingo","Horse","Brittle stars","Centipede"]]
        n_legs: [[2,4,5,100]]
        entry: [[2022-03-01,2022-03-02,2022-03-03,2022-03-04]]
    
        >>> read_options = csv.ReadOptions(autogenerate_column_names=True,
        ...                                skip_rows=1)
        >>> csv.read_csv(io.BytesIO(s.encode()), read_options=read_options)
        pyarrow.Table
        f0: string
        f1: int64
        f2: date32[day]
        ----
        f0: [["Flamingo","Horse","Brittle stars","Centipede"]]
        f1: [[2,4,5,100]]
        f2: [[2022-03-01,2022-03-02,2022-03-03,2022-03-04]]
    
        Remove the first 2 rows of the data:
    
        >>> read_options = csv.ReadOptions(skip_rows_after_names=2)
        >>> csv.read_csv(io.BytesIO(s.encode()), read_options=read_options)
        pyarrow.Table
        1: string
        2: int64
        3: date32[day]
        ----
        1: [["Brittle stars","Centipede"]]
        2: [[5,100]]
        3: [[2022-03-03,2022-03-04]]
    """
    def equals(self, ReadOptions_other): # real signature unknown; restored from __doc__
        """ ReadOptions.equals(self, ReadOptions other) """
        pass

    def validate(self): # real signature unknown; restored from __doc__
        """ ReadOptions.validate(self) """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __getstate__(self): # real signature unknown; restored from __doc__
        """ ReadOptions.__getstate__(self) """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __init__(self, use_threads=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
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

    def __reduce_cython__(self): # real signature unknown; restored from __doc__
        """ ReadOptions.__reduce_cython__(self) """
        pass

    def __setstate_cython__(self, __pyx_state): # real signature unknown; restored from __doc__
        """ ReadOptions.__setstate_cython__(self, __pyx_state) """
        pass

    def __setstate__(self, state): # real signature unknown; restored from __doc__
        """ ReadOptions.__setstate__(self, state) """
        pass

    autogenerate_column_names = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Whether to autogenerate column names if `column_names` is empty.
        If true, column names will be of the form "f0", "f1"...
        If false, column names will be read from the first CSV row
        after `skip_rows`.
        """

    block_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        How much bytes to process at a time from the input stream.
        This will determine multi-threading granularity as well as
        the size of individual record batches or table chunks.
        """

    column_names = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        The column names of the target table.  If empty, fall back on
        `autogenerate_column_names`.
        """

    encoding = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """encoding: object"""

    skip_rows = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        The number of rows to skip before the column names (if any)
        and the CSV data.
        See `skip_rows_after_names` for interaction description
        """

    skip_rows_after_names = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        The number of rows to skip after the column names.
        This number can be larger than the number of rows in one
        block, and empty rows are counted.
        The order of application is as follows:
        - `skip_rows` is applied (if non-zero);
        - column names aread (unless `column_names` is set);
        - `skip_rows_after_names` is applied (if non-zero).
        """

    use_threads = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Whether to use multiple threads to accelerate reading.
        """


    __hash__ = None
    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001894D875BA0>'
    __slots__ = ()


class WriteOptions(__pyarrow_lib._Weakrefable):
    """
    WriteOptions(include_header=None, *, batch_size=None, delimiter=None, quoting_style=None)
    
        Options for writing CSV files.
    
        Parameters
        ----------
        include_header : bool, optional (default True)
            Whether to write an initial header line with column names
        batch_size : int, optional (default 1024)
            How many rows to process together when converting and writing
            CSV data
        delimiter : 1-character string, optional (default ",")
            The character delimiting individual cells in the CSV data.
        quoting_style : str, optional (default "needed")
            Whether to quote values, and if so, which quoting style to use.
            The following values are accepted:
    
            - "needed" (default): only enclose values in quotes when needed.
            - "all_valid": enclose all valid values in quotes; nulls are not quoted.
            - "none": do not enclose any values in quotes; values containing
              special characters (such as quotes, cell delimiters or line endings)
              will raise an error.
    """
    def validate(self): # real signature unknown; restored from __doc__
        """ WriteOptions.validate(self) """
        pass

    def __init__(self, include_header=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ WriteOptions.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ WriteOptions.__setstate_cython__(self, __pyx_state) """
        pass

    batch_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        How many rows to process together when converting and writing
        CSV data.
        """

    delimiter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        The character delimiting individual cells in the CSV data.
        """

    include_header = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Whether to write an initial header line with column names.
        """

    quoting_style = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Whether to quote values, and if so, which quoting style to use.
        The following values are accepted:

        - "needed" (default): only enclose values in quotes when needed.
        - "all_valid": enclose all valid values in quotes; nulls are not quoted.
        - "none": do not enclose any values in quotes; values containing
          special characters (such as quotes, cell delimiters or line endings)
          will raise an error.
        """


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001894D875C00>'
    __slots__ = ()


class _ISO8601(__pyarrow_lib._Weakrefable):
    """ A special object indicating ISO-8601 parsing. """
    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
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

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ _ISO8601.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ _ISO8601.__setstate_cython__(self, __pyx_state) """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    __hash__ = None
    __slots__ = ()


# variables with complex values

ISO8601 = None # (!) real value is '<pyarrow._csv._ISO8601 object at 0x000001893F2D8790>'

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x000001893F27F700>'

__spec__ = None # (!) real value is "ModuleSpec(name='pyarrow._csv', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x000001893F27F700>, origin='C:\\\\Users\\\\akharin\\\\PycharmProjects\\\\pythonProject\\\\venv\\\\lib\\\\site-packages\\\\pyarrow\\\\_csv.cp39-win_amd64.pyd')"

__test__ = {
    'read_csv (line 1147)': '\n    Read a Table from a stream of CSV data.\n\n    Parameters\n    ----------\n    input_file : string, path or file-like object\n        The location of CSV data.  If a string or path, and if it ends\n        with a recognized compressed file extension (e.g. ".gz" or ".bz2"),\n        the data is automatically decompressed when reading.\n    read_options : pyarrow.csv.ReadOptions, optional\n        Options for the CSV reader (see pyarrow.csv.ReadOptions constructor\n        for defaults)\n    parse_options : pyarrow.csv.ParseOptions, optional\n        Options for the CSV parser\n        (see pyarrow.csv.ParseOptions constructor for defaults)\n    convert_options : pyarrow.csv.ConvertOptions, optional\n        Options for converting CSV data\n        (see pyarrow.csv.ConvertOptions constructor for defaults)\n    memory_pool : MemoryPool, optional\n        Pool to allocate Table memory from\n\n    Returns\n    -------\n    :class:`pyarrow.Table`\n        Contents of the CSV file as a in-memory table.\n\n    Examples\n    --------\n\n    Defining an example file from bytes object:\n\n    >>> import io\n    >>> s = "animals,n_legs,entry\\nFlamingo,2,2022-03-01\\nHorse,4,2022-03-02\\nBrittle stars,5,2022-03-03\\nCentipede,100,2022-03-04"\n    >>> print(s)\n    animals,n_legs,entry\n    Flamingo,2,2022-03-01\n    Horse,4,2022-03-02\n    Brittle stars,5,2022-03-03\n    Centipede,100,2022-03-04\n    >>> source = io.BytesIO(s.encode())\n\n    Reading from the file\n\n    >>> from pyarrow import csv\n    >>> csv.read_csv(source)\n    pyarrow.Table\n    animals: string\n    n_legs: int64\n    entry: date32[day]\n    ----\n    animals: [["Flamingo","Horse","Brittle stars","Centipede"]]\n    n_legs: [[2,4,5,100]]\n    entry: [[2022-03-01,2022-03-02,2022-03-03,2022-03-04]]\n    ',
    'write_csv (line 1410)': '\n    Write record batch or table to a CSV file.\n\n    Parameters\n    ----------\n    data : pyarrow.RecordBatch or pyarrow.Table\n        The data to write.\n    output_file : string, path, pyarrow.NativeFile, or file-like object\n        The location where to write the CSV data.\n    write_options : pyarrow.csv.WriteOptions\n        Options to configure writing the CSV data.\n    memory_pool : MemoryPool, optional\n        Pool for temporary allocations.\n\n    Examples\n    --------\n\n    >>> import pyarrow as pa\n    >>> from pyarrow import csv\n\n    >>> legs = pa.array([2, 4, 5, 100])\n    >>> animals = pa.array(["Flamingo", "Horse", "Brittle stars", "Centipede"])\n    >>> entry_date = pa.array(["01/03/2022", "02/03/2022",\n    ...                        "03/03/2022", "04/03/2022"])\n    >>> table = pa.table([animals, legs, entry_date],\n    ...                  names=["animals", "n_legs", "entry"])\n\n    >>> csv.write_csv(table, "animals.csv")\n\n    >>> write_options = csv.WriteOptions(include_header=False)\n    >>> csv.write_csv(table, "animals.csv", write_options=write_options)\n\n    >>> write_options = csv.WriteOptions(delimiter=";")\n    >>> csv.write_csv(table, "animals.csv", write_options=write_options)\n    ',
}

