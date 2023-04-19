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

class HivePartitioning(KeyValuePartitioning):
    """
    HivePartitioning(Schema schema, dictionaries=None, null_fallback=u'__HIVE_DEFAULT_PARTITION__', segment_encoding=u'uri')
    
        A Partitioning for "/$key=$value/" nested directories as found in
        Apache Hive.
    
        Multi-level, directory based partitioning scheme originating from
        Apache Hive with all data files stored in the leaf directories. Data is
        partitioned by static values of a particular column in the schema.
        Partition keys are represented in the form $key=$value in directory names.
        Field order is ignored, as are missing or unrecognized field names.
    
        For example, given schema<year:int16, month:int8, day:int8>, a possible
        path would be "/year=2009/month=11/day=15".
    
        Parameters
        ----------
        schema : Schema
            The schema that describes the partitions present in the file path.
        dictionaries : dict[str, Array]
            If the type of any field of `schema` is a dictionary type, the
            corresponding entry of `dictionaries` must be an array containing
            every value which may be taken by the corresponding column or an
            error will be raised in parsing.
        null_fallback : str, default "__HIVE_DEFAULT_PARTITION__"
            If any field is None then this fallback will be used as a label
        segment_encoding : str, default "uri"
            After splitting paths into segments, decode the segments. Valid
            values are "uri" (URI-decode segments) and "none" (leave as-is).
    
        Returns
        -------
        HivePartitioning
    
        Examples
        --------
        >>> from pyarrow.dataset import HivePartitioning
        >>> partitioning = HivePartitioning(
        ...     pa.schema([("year", pa.int16()), ("month", pa.int8())]))
        >>> print(partitioning.parse("/year=2009/month=11/"))
        ((year == 2009) and (month == 11))
    """
    def discover(self, infer_dictionary=False, max_partition_dictionary_size=0, null_fallback=None, schema=None, segment_encoding=None): # real signature unknown; restored from __doc__
        """
        HivePartitioning.discover(infer_dictionary=False, max_partition_dictionary_size=0, null_fallback=u'__HIVE_DEFAULT_PARTITION__', schema=None, segment_encoding=u'uri')
        
                Discover a HivePartitioning.
        
                Parameters
                ----------
                infer_dictionary : bool, default False
                    When inferring a schema for partition fields, yield dictionary
                    encoded types instead of plain. This can be more efficient when
                    materializing virtual columns, and Expressions parsed by the
                    finished Partitioning will include dictionaries of all unique
                    inspected values for each field.
                max_partition_dictionary_size : int, default 0
                    Synonymous with infer_dictionary for backwards compatibility with
                    1.0: setting this to -1 or None is equivalent to passing
                    infer_dictionary=True.
                null_fallback : str, default "__HIVE_DEFAULT_PARTITION__"
                    When inferring a schema for partition fields this value will be
                    replaced by null.  The default is set to __HIVE_DEFAULT_PARTITION__
                    for compatibility with Spark
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

    def __init__(self, Schema_schema, dictionaries=None, null_fallback=None, segment_encoding=None): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ HivePartitioning.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ HivePartitioning.__setstate_cython__(self, __pyx_state) """
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x00000187AB21EB40>'


