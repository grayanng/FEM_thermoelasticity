# encoding: utf-8
# module pyarrow._parquet
# from C:\Users\akharin\PycharmProjects\pythonProject\venv\lib\site-packages\pyarrow\_parquet.cp39-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import io as io # C:\Users\akharin\AppData\Local\Programs\Python\Python39\lib\io.py
import warnings as warnings # C:\Users\akharin\AppData\Local\Programs\Python\Python39\lib\warnings.py
import numpy as np # C:\Users\akharin\PycharmProjects\pythonProject\venv\lib\site-packages\numpy\__init__.py
from pyarrow.lib import (ArrowException, BufferOutputStream, 
    _datetime_from_int, frombytes, tobytes)

import pyarrow.lib as __pyarrow_lib


# functions

def indent(text, prefix, predicate=None): # reliably restored by inspect
    """
    Adds 'prefix' to the beginning of selected lines in 'text'.
    
        If 'predicate' is provided, 'prefix' will only be added to the lines
        where 'predicate(line)' is True. If 'predicate' is not provided,
        it will default to adding 'prefix' to all non-empty lines that do not
        consist solely of whitespace characters.
    """
    pass

def _reconstruct_filemetadata(Buffer_serialized): # real signature unknown; restored from __doc__
    """ _reconstruct_filemetadata(Buffer serialized) """
    pass

def _stringify_path(path): # reliably restored by inspect
    """ Convert *path* to a string or unicode path if possible. """
    pass

# classes

class ColumnChunkMetaData(__pyarrow_lib._Weakrefable):
    """ Column metadata for a single row group. """
    def equals(self, ColumnChunkMetaData_other): # real signature unknown; restored from __doc__
        """
        ColumnChunkMetaData.equals(self, ColumnChunkMetaData other)
        
                Return whether the two column chunk metadata objects are equal.
        
                Parameters
                ----------
                other : ColumnChunkMetaData
                    Metadata to compare against.
        
                Returns
                -------
                are_equal : bool
        """
        pass

    def to_dict(self): # real signature unknown; restored from __doc__
        """
        ColumnChunkMetaData.to_dict(self)
        
                Get dictionary represenation of the column chunk metadata.
        
                Returns
                -------
                dict
                    Dictionary with a key for each attribute of this class.
        """
        pass

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
        """ ColumnChunkMetaData.__reduce_cython__(self) """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ ColumnChunkMetaData.__setstate_cython__(self, __pyx_state) """
        pass

    compression = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Type of compression used for column (str).

        One of 'UNCOMPRESSED', 'SNAPPY', 'GZIP', 'LZO', 'BROTLI', 'LZ4', 'ZSTD',
        or 'UNKNOWN'.
        """

    data_page_offset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Offset of data page reglative to column chunk offset (int)."""

    dictionary_page_offset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Offset of dictionary page reglative to column chunk offset (int)."""

    encodings = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Encodings used for column (tuple of str).

        One of 'PLAIN', 'BIT_PACKED', 'RLE', 'BYTE_STREAM_SPLIT', 'DELTA_BINARY_PACKED',
        'DELTA_BYTE_ARRAY'.
        """

    file_offset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Offset into file where column chunk is located (int)."""

    file_path = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Optional file path if set (str or None)."""

    has_dictionary_page = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Whether there is dictionary data present in the column chunk (bool)."""

    has_index_page = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Not yet supported."""

    index_page_offset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Not yet supported."""

    is_stats_set = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Whether or not statistics are present in metadata (bool)."""

    num_values = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Total number of values (int)."""

    path_in_schema = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Nested path to field, separated by periods (str)."""

    physical_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Physical type of column (str)."""

    statistics = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Statistics for column chunk (:class:`Statistics`)."""

    total_compressed_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Compresssed size in bytes (int)."""

    total_uncompressed_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Uncompressed size in bytes (int)."""


    __hash__ = None
    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001C2112D5D80>'


class ColumnSchema(__pyarrow_lib._Weakrefable):
    """ Schema for a single column. """
    def equals(self, ColumnSchema_other): # real signature unknown; restored from __doc__
        """
        ColumnSchema.equals(self, ColumnSchema other)
        
                Return whether the two column schemas are equal.
        
                Parameters
                ----------
                other : ColumnSchema
                    Schema to compare against.
        
                Returns
                -------
                are_equal : bool
        """
        pass

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

    def __reduce__(self): # real signature unknown; restored from __doc__
        """ ColumnSchema.__reduce__(self) """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    converted_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Legacy converted type (str or None)."""

    length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Array length if fixed length byte array type, None otherwise (int or None)."""

    logical_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Logical type of column (:class:`ParquetLogicalType`)."""

    max_definition_level = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Maximum definition level (int)."""

    max_repetition_level = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Maximum repetition level (int)."""

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Name of field (str)."""

    path = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Nested path to field, separated by periods (str)."""

    physical_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Name of physical type (str)."""

    precision = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Precision if decimal type, None otherwise (int or None)."""

    scale = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Scale if decimal type, None otherwise (int or None)."""


    __hash__ = None


class FileDecryptionProperties(object):
    """ File-level decryption properties for the low-level API """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001C2112D5E40>'


class FileEncryptionProperties(object):
    """ File-level encryption properties for the low-level API """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001C2112D5C60>'


class FileMetaData(__pyarrow_lib._Weakrefable):
    """ Parquet metadata for a single file. """
    def append_row_groups(self, FileMetaData_other): # real signature unknown; restored from __doc__
        """
        FileMetaData.append_row_groups(self, FileMetaData other)
        
                Append row groups from other FileMetaData object.
        
                Parameters
                ----------
                other : FileMetaData
                    Other metadata to append row groups from.
        """
        pass

    def equals(self, FileMetaData_other): # real signature unknown; restored from __doc__
        """
        FileMetaData.equals(self, FileMetaData other)
        
                Return whether the two file metadata objects are equal.
        
                Parameters
                ----------
                other : FileMetaData
                    Metadata to compare against.
        
                Returns
                -------
                are_equal : bool
        """
        pass

    def row_group(self, int_i): # real signature unknown; restored from __doc__
        """
        FileMetaData.row_group(self, int i)
        
                Get metadata for row group at index i.
        
                Parameters
                ----------
                i : int
                    Row group index to get.
        
                Returns
                -------
                row_group_metadata : RowGroupMetaData
        """
        pass

    def set_file_path(self, path): # real signature unknown; restored from __doc__
        """
        FileMetaData.set_file_path(self, path)
        
                Set ColumnChunk file paths to the given value.
        
                This method modifies the ``file_path`` field of each ColumnChunk
                in the FileMetaData to be a particular value.
        
                Parameters
                ----------
                path : str
                    The file path to set on all ColumnChunks.
        """
        pass

    def to_dict(self): # real signature unknown; restored from __doc__
        """
        FileMetaData.to_dict(self)
        
                Get dictionary represenation of the file metadata.
        
                Returns
                -------
                dict
                    Dictionary with a key for each attribute of this class.
        """
        pass

    def write_metadata_file(self, where): # real signature unknown; restored from __doc__
        """
        FileMetaData.write_metadata_file(self, where)
        
                Write the metadata to a metadata-only Parquet file.
        
                Parameters
                ----------
                where : path or file-like object
                    Where to write the metadata.  Should be a writable path on
                    the local filesystem, or a writable file-like object.
        """
        pass

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

    def __reduce__(self): # real signature unknown; restored from __doc__
        """ FileMetaData.__reduce__(self) """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    created_by = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        String describing source of the parquet file (str).

        This typically includes library name and version number. For example, Arrow 7.0's
        writer returns 'parquet-cpp-arrow version 7.0.0'.
        """

    format_version = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Parquet format version used in file (str, such as '1.0', '2.4').

        If version is missing or unparsable, will default to assuming '2.4'.
        """

    metadata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Additional metadata as key value pairs (dict[bytes, bytes])."""

    num_columns = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Number of columns in file (int)."""

    num_rows = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Total number of rows in file (int)."""

    num_row_groups = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Number of row groups in file (int)."""

    schema = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Schema of the file (:class:`ParquetSchema`)."""

    serialized_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Size of the original thrift encoded metadata footer (int)."""


    __hash__ = None
    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001C2112D5CF0>'


class ParquetLogicalType(__pyarrow_lib._Weakrefable):
    """ Logical type of parquet type. """
    def to_json(self): # real signature unknown; restored from __doc__
        """
        ParquetLogicalType.to_json(self)
        
                Get a JSON string containing type and type parameters.
        
                Returns
                -------
                json : str
                    JSON representation of type, with at least a field called 'Type'
                    which contains the type name. If the type is parameterized, such
                    as a decimal with scale and precision, will contain those as fields
                    as well.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ ParquetLogicalType.__reduce_cython__(self) """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ ParquetLogicalType.__setstate_cython__(self, __pyx_state) """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Name of the logical type (str)."""


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001C2112D5EA0>'


class ParquetReader(__pyarrow_lib._Weakrefable):
    # no doc
    def close(self): # real signature unknown; restored from __doc__
        """ ParquetReader.close(self) """
        pass

    def column_name_idx(self, column_name): # real signature unknown; restored from __doc__
        """
        ParquetReader.column_name_idx(self, column_name)
        
                Find the index of a column by its name.
        
                Parameters
                ----------
                column_name : str
                    Name of the column; separation of nesting levels is done via ".".
        
                Returns
                -------
                column_idx : int
                    Integer index of the column in the schema.
        """
        pass

    def iter_batches(self, int64_t_batch_size, row_groups, column_indices=None, bool_use_threads=True): # real signature unknown; restored from __doc__
        """ ParquetReader.iter_batches(self, int64_t batch_size, row_groups, column_indices=None, bool use_threads=True) """
        pass

    def open(self, source, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ ParquetReader.open(self, source, *, bool use_memory_map=False, read_dictionary=None, FileMetaData metadata=None, int buffer_size=0, bool pre_buffer=False, coerce_int96_timestamp_unit=None, FileDecryptionProperties decryption_properties=None, thrift_string_size_limit=None, thrift_container_size_limit=None) """
        pass

    def read_all(self, column_indices=None, bool_use_threads=True): # real signature unknown; restored from __doc__
        """ ParquetReader.read_all(self, column_indices=None, bool use_threads=True) """
        pass

    def read_column(self, int_column_index): # real signature unknown; restored from __doc__
        """ ParquetReader.read_column(self, int column_index) """
        pass

    def read_row_group(self, int_i, column_indices=None, bool_use_threads=True): # real signature unknown; restored from __doc__
        """ ParquetReader.read_row_group(self, int i, column_indices=None, bool use_threads=True) """
        pass

    def read_row_groups(self, row_groups, column_indices=None, bool_use_threads=True): # real signature unknown; restored from __doc__
        """ ParquetReader.read_row_groups(self, row_groups, column_indices=None, bool use_threads=True) """
        pass

    def scan_contents(self, column_indices=None, batch_size=65536): # real signature unknown; restored from __doc__
        """ ParquetReader.scan_contents(self, column_indices=None, batch_size=65536) """
        pass

    def set_batch_size(self, int64_t_batch_size): # real signature unknown; restored from __doc__
        """ ParquetReader.set_batch_size(self, int64_t batch_size) """
        pass

    def set_use_threads(self, bool_use_threads): # real signature unknown; restored from __doc__
        """ ParquetReader.set_use_threads(self, bool use_threads) """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ ParquetReader.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ ParquetReader.__setstate_cython__(self, __pyx_state) """
        pass

    closed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    column_paths = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    metadata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    num_row_groups = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    schema_arrow = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _column_idx_map = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """_column_idx_map: object"""


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001C2112D5F30>'


class ParquetSchema(__pyarrow_lib._Weakrefable):
    """ A Parquet schema. """
    def column(self, i): # real signature unknown; restored from __doc__
        """
        ParquetSchema.column(self, i)
        
                Return the schema for a single column.
        
                Parameters
                ----------
                i : int
                    Index of column in schema.
        
                Returns
                -------
                column_schema : ColumnSchema
        """
        pass

    def equals(self, ParquetSchema_other): # real signature unknown; restored from __doc__
        """
        ParquetSchema.equals(self, ParquetSchema other)
        
                Return whether the two schemas are equal.
        
                Parameters
                ----------
                other : ParquetSchema
                    Schema to compare against.
        
                Returns
                -------
                are_equal : bool
        """
        pass

    def to_arrow_schema(self): # real signature unknown; restored from __doc__
        """
        ParquetSchema.to_arrow_schema(self)
        
                Convert Parquet schema to effective Arrow schema.
        
                Returns
                -------
                schema : Schema
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

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __reduce__(self): # real signature unknown; restored from __doc__
        """ ParquetSchema.__reduce__(self) """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    names = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Name of each field (list of str)."""


    __hash__ = None


class ParquetWriter(__pyarrow_lib._Weakrefable):
    # no doc
    def close(self): # real signature unknown; restored from __doc__
        """ ParquetWriter.close(self) """
        pass

    def write_table(self, Table_table, row_group_size=None): # real signature unknown; restored from __doc__
        """ ParquetWriter.write_table(self, Table table, row_group_size=None) """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ ParquetWriter.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ ParquetWriter.__setstate_cython__(self, __pyx_state) """
        pass

    allow_truncated_timestamps = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    coerce_timestamps = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    column_encoding = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    compression = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    compression_level = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    data_page_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    data_page_version = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dictionary_pagesize_limit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    encryption_properties = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    metadata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    row_group_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    store_schema = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    use_byte_stream_split = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    use_compliant_nested_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    use_deprecated_int96_timestamps = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    use_dictionary = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    version = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    writer_engine_version = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    write_batch_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    write_statistics = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class RowGroupMetaData(__pyarrow_lib._Weakrefable):
    """ Metadata for a single row group. """
    def column(self, int_i): # real signature unknown; restored from __doc__
        """
        RowGroupMetaData.column(self, int i)
        
                Get column metadata at given index.
        
                Parameters
                ----------
                i : int
                    Index of column to get metadata for.
        
                Returns
                -------
                ColumnChunkMetaData
                    Metadata for column within this chunk.
        """
        pass

    def equals(self, RowGroupMetaData_other): # real signature unknown; restored from __doc__
        """
        RowGroupMetaData.equals(self, RowGroupMetaData other)
        
                Return whether the two row group metadata objects are equal.
        
                Parameters
                ----------
                other : RowGroupMetaData
                    Metadata to compare against.
        
                Returns
                -------
                are_equal : bool
        """
        pass

    def to_dict(self): # real signature unknown; restored from __doc__
        """
        RowGroupMetaData.to_dict(self)
        
                Get dictionary represenation of the row group metadata.
        
                Returns
                -------
                dict
                    Dictionary with a key for each attribute of this class.
        """
        pass

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

    def __reduce__(self): # real signature unknown; restored from __doc__
        """ RowGroupMetaData.__reduce__(self) """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    num_columns = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Number of columns in this row group (int)."""

    num_rows = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Number of rows in this row group (int)."""

    total_byte_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Total byte size of all the uncompressed column data in this row group (int)."""


    __hash__ = None


class Statistics(__pyarrow_lib._Weakrefable):
    """ Statistics for a single column in a single row group. """
    def equals(self, Statistics_other): # real signature unknown; restored from __doc__
        """
        Statistics.equals(self, Statistics other)
        
                Return whether the two column statistics objects are equal.
        
                Parameters
                ----------
                other : Statistics
                    Statistics to compare against.
        
                Returns
                -------
                are_equal : bool
        """
        pass

    def to_dict(self): # real signature unknown; restored from __doc__
        """
        Statistics.to_dict(self)
        
                Get dictionary represenation of statistics.
        
                Returns
                -------
                dict
                    Dictionary with a key for each attribute of this class.
        """
        pass

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
        """ Statistics.__reduce_cython__(self) """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ Statistics.__setstate_cython__(self, __pyx_state) """
        pass

    converted_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Legacy converted type (str or None)."""

    distinct_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Distinct number of values in chunk (int).

        If this is not set, will return 0.
        """

    has_distinct_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Whether distinct count is preset (bool)."""

    has_min_max = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Whether min and max are present (bool)."""

    has_null_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Whether null count is present (bool)."""

    logical_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Logical type of column (:class:`ParquetLogicalType`)."""

    max = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Max value as logical type.

        Returned as the Python equivalent of logical type, such as datetime.date
        for dates and decimal.Decimal for decimals.
        """

    max_raw = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Max value as physical type (bool, int, float, or bytes)."""

    min = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Min value as logical type.

        Returned as the Python equivalent of logical type, such as datetime.date
        for dates and decimal.Decimal for decimals.
        """

    min_raw = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Min value as physical type (bool, int, float, or bytes)."""

    null_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Number of null values in chunk (int)."""

    num_values = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Number of non-null values (int)."""

    physical_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Physical type of column (str)."""


    __hash__ = None
    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001C2112D5DE0>'


# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x000001C202CEA910>'

__pyx_capi__ = {
    '_create_arrow_writer_properties': None, # (!) real value is '<capsule object "std::shared_ptr<parquet::ArrowWriterProperties>  (struct __pyx_opt_args_7pyarrow_8_parquet__create_arrow_writer_properties *__pyx_optional_args)" at 0x000001C2112D5C00>'
    '_create_writer_properties': None, # (!) real value is '<capsule object "std::shared_ptr<parquet::WriterProperties>  (struct __pyx_opt_args_7pyarrow_8_parquet__create_writer_properties *__pyx_optional_args)" at 0x000001C2112D5BD0>'
}

__spec__ = None # (!) real value is "ModuleSpec(name='pyarrow._parquet', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x000001C202CEA910>, origin='C:\\\\Users\\\\akharin\\\\PycharmProjects\\\\pythonProject\\\\venv\\\\lib\\\\site-packages\\\\pyarrow\\\\_parquet.cp39-win_amd64.pyd')"

__test__ = {}

