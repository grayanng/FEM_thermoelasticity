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


from .KeyValuePartitioning import KeyValuePartitioning

class DirectoryPartitioning(KeyValuePartitioning):
    """
    DirectoryPartitioning(Schema schema, dictionaries=None, segment_encoding=u'uri')
    
        A Partitioning based on a specified Schema.
    
        The DirectoryPartitioning expects one segment in the file path for each
        field in the schema (all fields are required to be present).
        For example given schema<year:int16, month:int8> the path "/2009/11" would
        be parsed to ("year"_ == 2009 and "month"_ == 11).
    
        Parameters
        ----------
        schema : Schema
            The schema that describes the partitions present in the file path.
        dictionaries : dict[str, Array]
            If the type of any field of `schema` is a dictionary type, the
            corresponding entry of `dictionaries` must be an array containing
            every value which may be taken by the corresponding column or an
            error will be raised in parsing.
        segment_encoding : str, default "uri"
            After splitting paths into segments, decode the segments. Valid
            values are "uri" (URI-decode segments) and "none" (leave as-is).
    
        Returns
        -------
        DirectoryPartitioning
    
        Examples
        --------
        >>> from pyarrow.dataset import DirectoryPartitioning
        >>> partitioning = DirectoryPartitioning(
        ...     pa.schema([("year", pa.int16()), ("month", pa.int8())]))
        >>> print(partitioning.parse("/2009/11/"))
        ((year == 2009) and (month == 11))
    """
    def discover(self, field_names=None, infer_dictionary=False, max_partition_dictionary_size=0, schema=None, segment_encoding=None): # real signature unknown; restored from __doc__
        """
        DirectoryPartitioning.discover(field_names=None, infer_dictionary=False, max_partition_dictionary_size=0, schema=None, segment_encoding=u'uri')
        
                Discover a DirectoryPartitioning.
        
                Parameters
                ----------
                field_names : list of str
                    The names to associate with the values from the subdirectory names.
                    If schema is given, will be populated from the schema.
                infer_dictionary : bool, default False
                    When inferring a schema for partition fields, yield dictionary
                    encoded types instead of plain types. This can be more efficient
                    when materializing virtual columns, and Expressions parsed by the
                    finished Partitioning will include dictionaries of all unique
                    inspected values for each field.
                max_partition_dictionary_size : int, default 0
                    Synonymous with infer_dictionary for backwards compatibility with
                    1.0: setting this to -1 or None is equivalent to passing
                    infer_dictionary=True.
                schema : Schema, default None
                    Use this schema instead of inferring a schema from partition
                    values. Partition values will be validated against this schema
                    before accumulation into the Partitioning's dictionary.
                segment_encoding : str, default "uri"
                    After splitting paths into segments, decode the segments. Valid
                    values are "uri" (URI-decode segments) and "none" (leave as-is).
        
                Returns
                -------
                PartitioningFactory
                    To be used in the FileSystemFactoryOptions.
        """
        pass

    def __init__(self, Schema_schema, dictionaries=None, segment_encoding=None): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ DirectoryPartitioning.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ DirectoryPartitioning.__setstate_cython__(self, __pyx_state) """
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x00000187AB21EAE0>'


