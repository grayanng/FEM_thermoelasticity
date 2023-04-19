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


from .Array import Array

class DictionaryArray(Array):
    """ Concrete class for dictionary-encoded Arrow arrays. """
    def dictionary_decode(self): # real signature unknown; restored from __doc__
        """
        DictionaryArray.dictionary_decode(self)
        
                Decodes the DictionaryArray to an Array.
        """
        pass

    def dictionary_encode(self): # real signature unknown; restored from __doc__
        """ DictionaryArray.dictionary_encode(self) """
        pass

    def from_arrays(self, indices, dictionary, mask=None, bool_ordered=False, bool_from_pandas=False, bool_safe=True, MemoryPool_memory_pool=None): # real signature unknown; restored from __doc__
        """
        DictionaryArray.from_arrays(indices, dictionary, mask=None, bool ordered=False, bool from_pandas=False, bool safe=True, MemoryPool memory_pool=None)
        
                Construct a DictionaryArray from indices and values.
        
                Parameters
                ----------
                indices : pyarrow.Array, numpy.ndarray or pandas.Series, int type
                    Non-negative integers referencing the dictionary values by zero
                    based index.
                dictionary : pyarrow.Array, ndarray or pandas.Series
                    The array of values referenced by the indices.
                mask : ndarray or pandas.Series, bool type
                    True values indicate that indices are actually null.
                ordered : bool, default False
                    Set to True if the category values are ordered.
                from_pandas : bool, default False
                    If True, the indices should be treated as though they originated in
                    a pandas.Categorical (null encoded as -1).
                safe : bool, default True
                    If True, check that the dictionary indices are in range.
                memory_pool : MemoryPool, default None
                    For memory allocations, if required, otherwise uses default pool.
        
                Returns
                -------
                dict_array : DictionaryArray
        """
        pass

    def from_buffers(self, DataType_type, int64_t_length, buffers, Array_dictionary, int64_t_null_count=-1, int64_t_offset=0): # real signature unknown; restored from __doc__
        """
        DictionaryArray.from_buffers(DataType type, int64_t length, buffers, Array dictionary, int64_t null_count=-1, int64_t offset=0)
        
                Construct a DictionaryArray from buffers.
        
                Parameters
                ----------
                type : pyarrow.DataType
                length : int
                    The number of values in the array.
                buffers : List[Buffer]
                    The buffers backing the indices array.
                dictionary : pyarrow.Array, ndarray or pandas.Series
                    The array of values referenced by the indices.
                null_count : int, default -1
                    The number of null entries in the indices array. Negative value means that
                    the null count is not known.
                offset : int, default 0
                    The array's logical offset (in values, not in bytes) from the
                    start of each buffer.
        
                Returns
                -------
                dict_array : DictionaryArray
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    dictionary = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    indices = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001970BCC5D80>'


