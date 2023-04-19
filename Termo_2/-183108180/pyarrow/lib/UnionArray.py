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

class UnionArray(Array):
    """ Concrete class for Arrow arrays of a Union data type. """
    def child(self, int_pos): # real signature unknown; restored from __doc__
        """ UnionArray.child(self, int pos) """
        pass

    def field(self, int_pos): # real signature unknown; restored from __doc__
        """
        UnionArray.field(self, int pos)
        
                Return the given child field as an individual array.
        
                For sparse unions, the returned array has its offset, length,
                and null count adjusted.
        
                For dense unions, the returned array is unchanged.
        
                Parameters
                ----------
                pos : int
                    The physical index of the union child field (not its type code).
        
                Returns
                -------
                field : Array
                    The given child field.
        """
        pass

    def from_dense(self, Array_types, Array_value_offsets, list_children, list_field_names=None, list_type_codes=None): # real signature unknown; restored from __doc__
        """
        UnionArray.from_dense(Array types, Array value_offsets, list children, list field_names=None, list type_codes=None)
        
                Construct dense UnionArray from arrays of int8 types, int32 offsets and
                children arrays
        
                Parameters
                ----------
                types : Array (int8 type)
                value_offsets : Array (int32 type)
                children : list
                field_names : list
                type_codes : list
        
                Returns
                -------
                union_array : UnionArray
        """
        pass

    def from_sparse(self, Array_types, list_children, list_field_names=None, list_type_codes=None): # real signature unknown; restored from __doc__
        """
        UnionArray.from_sparse(Array types, list children, list field_names=None, list type_codes=None)
        
                Construct sparse UnionArray from arrays of int8 types and children
                arrays
        
                Parameters
                ----------
                types : Array (int8 type)
                children : list
                field_names : list
                type_codes : list
        
                Returns
                -------
                union_array : UnionArray
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    offsets = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Get the value offsets array (dense arrays only).

        Does not account for any slice offset.
        """

    type_codes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get the type codes array."""


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001970BCC5C60>'


