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


class Scanner(__pyarrow_lib._Weakrefable):
    """
    Scanner()
    A materialized scan operation with context and options bound.
    
        A scanner is the class that glues the scan tasks, data fragments and data
        sources together.
    
        Parameters
        ----------
        dataset : Dataset
            Dataset to scan.
        columns : list of str or dict, default None
            The columns to project. This can be a list of column names to
            include (order and duplicates will be preserved), or a dictionary
            with {{new_column_name: expression}} values for more advanced
            projections.
    
            The list of columns or expressions may use the special fields
            `__batch_index` (the index of the batch within the fragment),
            `__fragment_index` (the index of the fragment within the dataset),
            `__last_in_fragment` (whether the batch is last in fragment), and
            `__filename` (the name of the source file or a description of the
            source fragment).
    
            The columns will be passed down to Datasets and corresponding data
            fragments to avoid loading, copying, and deserializing columns
            that will not be required further down the compute chain.
            By default all of the available columns are projected.
            Raises an exception if any of the referenced column names does
            not exist in the dataset's Schema.
        filter : Expression, default None
            Scan will return only the rows matching the filter.
            If possible the predicate will be pushed down to exploit the
            partition information or internal metadata found in the data
            source, e.g. Parquet statistics. Otherwise filters the loaded
            RecordBatches before yielding them.
        batch_size : int, default 128Ki
            The maximum row count for scanned record batches. If scanned
            record batches are overflowing memory then this method can be
            called to reduce their size.
        batch_readahead : int, default 16
            The number of batches to read ahead in a file. This might not work
            for all file formats. Increasing this number will increase
            RAM usage but could also improve IO utilization.
        fragment_readahead : int, default 4
            The number of files to read ahead. Increasing this number will increase
            RAM usage but could also improve IO utilization.
        use_threads : bool, default True
            If enabled, then maximum parallelism will be used determined by
            the number of available CPU cores.
        use_async : bool, default True
            This flag is deprecated and is being kept for this release for
            backwards compatibility.  It will be removed in the next release.
        memory_pool : MemoryPool, default None
            For memory allocations, if required. If not specified, uses the
            default pool.
    """
    def count_rows(self): # real signature unknown; restored from __doc__
        """
        Scanner.count_rows(self)
        
                Count rows matching the scanner filter.
        
                Returns
                -------
                count : int
        """
        pass

    def from_batches(self, source, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        Scanner.from_batches(source, *, Schema schema=None, columns=None, Expression filter=None, int batch_size=_DEFAULT_BATCH_SIZE, FragmentScanOptions fragment_scan_options=None, bool use_threads=True, use_async=None, MemoryPool memory_pool=None)
        
                Create a Scanner from an iterator of batches.
        
                This creates a scanner which can be used only once. It is
                intended to support writing a dataset (which takes a scanner)
                from a source which can be read only once (e.g. a
                RecordBatchReader or generator).
        
                Parameters
                ----------
                source : Iterator
                    The iterator of Batches.
                schema : Schema
                    The schema of the batches.
                columns : list of str or dict, default None
                        The columns to project.
                filter : Expression, default None
                    Scan will return only the rows matching the filter.
                batch_size : int, default 128Ki
                    The maximum row count for scanned record batches.
                fragment_scan_options : FragmentScanOptions
                    The fragment scan options.
                use_threads : bool, default True
                    If enabled, then maximum parallelism will be used determined by
                    the number of available CPU cores.
                use_async : bool, default True
                    This flag is deprecated and is being kept for this release for
                    backwards compatibility.  It will be removed in the next
                    release.
                memory_pool : MemoryPool, default None
                    For memory allocations, if required. If not specified, uses the
                    default pool.
        """
        pass

    def from_dataset(self, Dataset_dataset, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        Scanner.from_dataset(Dataset dataset, *, columns=None, Expression filter=None, int batch_size=_DEFAULT_BATCH_SIZE, int batch_readahead=_DEFAULT_BATCH_READAHEAD, int fragment_readahead=_DEFAULT_FRAGMENT_READAHEAD, FragmentScanOptions fragment_scan_options=None, bool use_threads=True, use_async=None, MemoryPool memory_pool=None)
        
                Create Scanner from Dataset,
        
                Parameters
                ----------
                dataset : Dataset
                    Dataset to scan.
                columns : list of str, default None
                    The columns to project. This can be a list of column names to
                    include (order and duplicates will be preserved), or a dictionary
                    with {new_column_name: expression} values for more advanced
                    projections.
        
                    The list of columns or expressions may use the special fields
                    `__batch_index` (the index of the batch within the fragment),
                    `__fragment_index` (the index of the fragment within the dataset),
                    `__last_in_fragment` (whether the batch is last in fragment), and
                    `__filename` (the name of the source file or a description of the
                    source fragment).
        
                    The columns will be passed down to Datasets and corresponding data
                    fragments to avoid loading, copying, and deserializing columns
                    that will not be required further down the compute chain.
                    By default all of the available columns are projected. Raises
                    an exception if any of the referenced column names does not exist
                    in the dataset's Schema.
                filter : Expression, default None
                    Scan will return only the rows matching the filter.
                    If possible the predicate will be pushed down to exploit the
                    partition information or internal metadata found in the data
                    source, e.g. Parquet statistics. Otherwise filters the loaded
                    RecordBatches before yielding them.
                batch_size : int, default 128Ki
                    The maximum row count for scanned record batches. If scanned
                    record batches are overflowing memory then this method can be
                    called to reduce their size.
                batch_readahead : int, default 16
                    The number of batches to read ahead in a file. This might not work
                    for all file formats. Increasing this number will increase
                    RAM usage but could also improve IO utilization.
                fragment_readahead : int, default 4
                    The number of files to read ahead. Increasing this number will increase
                    RAM usage but could also improve IO utilization.
                fragment_scan_options : FragmentScanOptions, default None
                    Options specific to a particular scan and fragment type, which
                    can change between different scans of the same dataset.
                use_threads : bool, default True
                    If enabled, then maximum parallelism will be used determined by
                    the number of available CPU cores.
                use_async : bool, default True
                    This flag is deprecated and is being kept for this release for
                    backwards compatibility.  It will be removed in the next
                    release.
                memory_pool : MemoryPool, default None
                    For memory allocations, if required. If not specified, uses the
                    default pool.
        """
        pass

    def from_fragment(self, Fragment_fragment, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        Scanner.from_fragment(Fragment fragment, *, Schema schema=None, columns=None, Expression filter=None, int batch_size=_DEFAULT_BATCH_SIZE, int batch_readahead=_DEFAULT_BATCH_READAHEAD, FragmentScanOptions fragment_scan_options=None, bool use_threads=True, use_async=None, MemoryPool memory_pool=None)
        
                Create Scanner from Fragment,
        
                Parameters
                ----------
                fragment : Fragment
                    fragment to scan.
                schema : Schema, optional
                    The schema of the fragment.
                columns : list of str, default None
                    The columns to project. This can be a list of column names to
                    include (order and duplicates will be preserved), or a dictionary
                    with {new_column_name: expression} values for more advanced
                    projections.
        
                    The list of columns or expressions may use the special fields
                    `__batch_index` (the index of the batch within the fragment),
                    `__fragment_index` (the index of the fragment within the dataset),
                    `__last_in_fragment` (whether the batch is last in fragment), and
                    `__filename` (the name of the source file or a description of the
                    source fragment).
        
                    The columns will be passed down to Datasets and corresponding data
                    fragments to avoid loading, copying, and deserializing columns
                    that will not be required further down the compute chain.
                    By default all of the available columns are projected. Raises
                    an exception if any of the referenced column names does not exist
                    in the dataset's Schema.
                filter : Expression, default None
                    Scan will return only the rows matching the filter.
                    If possible the predicate will be pushed down to exploit the
                    partition information or internal metadata found in the data
                    source, e.g. Parquet statistics. Otherwise filters the loaded
                    RecordBatches before yielding them.
                batch_size : int, default 128Ki
                    The maximum row count for scanned record batches. If scanned
                    record batches are overflowing memory then this method can be
                    called to reduce their size.
                batch_readahead : int, default 16
                    The number of batches to read ahead in a file. This might not work
                    for all file formats. Increasing this number will increase
                    RAM usage but could also improve IO utilization.
                fragment_scan_options : FragmentScanOptions, default None
                    Options specific to a particular scan and fragment type, which
                    can change between different scans of the same dataset.
                use_threads : bool, default True
                    If enabled, then maximum parallelism will be used determined by
                    the number of available CPU cores.
                use_async : bool, default True
                    This flag is deprecated and is being kept for this release for
                    backwards compatibility.  It will be removed in the next
                    release.
                memory_pool : MemoryPool, default None
                    For memory allocations, if required. If not specified, uses the
                    default pool.
                use_threads : bool, default True
                    If enabled, then maximum parallelism will be used determined by
                    the number of available CPU cores.
                use_async : bool, default True
                    This flag is deprecated and is being kept for this release for
                    backwards compatibility.  It will be removed in the next
                    release.
                memory_pool : MemoryPool, default None
                    For memory allocations, if required. If not specified, uses the
                    default pool.
        """
        pass

    def head(self, int_num_rows): # real signature unknown; restored from __doc__
        """
        Scanner.head(self, int num_rows)
        
                Load the first N rows of the dataset.
        
                Parameters
                ----------
                num_rows : int
                    The number of rows to load.
        
                Returns
                -------
                Table
        """
        pass

    def scan_batches(self): # real signature unknown; restored from __doc__
        """
        Scanner.scan_batches(self)
        
                Consume a Scanner in record batches with corresponding fragments.
        
                Returns
                -------
                record_batches : iterator of TaggedRecordBatch
        """
        pass

    def take(self, indices): # real signature unknown; restored from __doc__
        """
        Scanner.take(self, indices)
        
                Select rows of data by index.
        
                Will only consume as many batches of the underlying dataset as
                needed. Otherwise, this is equivalent to
                ``to_table().take(indices)``.
        
                Parameters
                ----------
                indices : Array or array-like
                    indices of rows to select in the dataset.
        
                Returns
                -------
                Table
        """
        pass

    def to_batches(self): # real signature unknown; restored from __doc__
        """
        Scanner.to_batches(self)
        
                Consume a Scanner in record batches.
        
                Returns
                -------
                record_batches : iterator of RecordBatch
        """
        pass

    def to_reader(self): # real signature unknown; restored from __doc__
        """
        Scanner.to_reader(self)
        Consume this scanner as a RecordBatchReader.
        
                Returns
                -------
                RecordBatchReader
        """
        pass

    def to_table(self): # real signature unknown; restored from __doc__
        """
        Scanner.to_table(self)
        
                Convert a Scanner into a Table.
        
                Use this convenience utility with care. This will serially materialize
                the Scan result in memory before creating the Table.
        
                Returns
                -------
                Table
        """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ Scanner.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ Scanner.__setstate_cython__(self, __pyx_state) """
        pass

    dataset_schema = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The schema with which batches will be read from fragments."""

    projected_schema = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        The materialized schema of the data, accounting for projections.

        This is the schema of any data returned from the scanner.
        """


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x00000187AB21E3F0>'


