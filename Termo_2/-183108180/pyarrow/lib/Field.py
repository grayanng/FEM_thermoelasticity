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


from ._Weakrefable import _Weakrefable

class Field(_Weakrefable):
    """
    Field()
    
        A named field, with a data type, nullability, and optional metadata.
    
        Notes
        -----
        Do not use this class's constructor directly; use pyarrow.field
    """
    def equals(self, Field_other, bool_check_metadata=False): # real signature unknown; restored from __doc__
        """
        Field.equals(self, Field other, bool check_metadata=False)
        
                Test if this field is equal to the other
        
                Parameters
                ----------
                other : pyarrow.Field
                check_metadata : bool, default False
                    Whether Field metadata equality should be checked as well.
        
                Returns
                -------
                is_equal : bool
        """
        pass

    def flatten(self): # real signature unknown; restored from __doc__
        """
        Field.flatten(self)
        
                Flatten this field.  If a struct field, individual child fields
                will be returned with their names prefixed by the parent's name.
        
                Returns
                -------
                fields : List[pyarrow.Field]
        """
        pass

    def remove_metadata(self): # real signature unknown; restored from __doc__
        """
        Field.remove_metadata(self)
        
                Create new field without metadata, if any
        
                Returns
                -------
                field : pyarrow.Field
        """
        pass

    def with_metadata(self, metadata): # real signature unknown; restored from __doc__
        """
        Field.with_metadata(self, metadata)
        
                Add metadata as dict of string keys and values to Field
        
                Parameters
                ----------
                metadata : dict
                    Keys and values must be string-like / coercible to bytes
        
                Returns
                -------
                field : pyarrow.Field
        """
        pass

    def with_name(self, name): # real signature unknown; restored from __doc__
        """
        Field.with_name(self, name)
        
                A copy of this field with the replaced name
        
                Parameters
                ----------
                name : str
        
                Returns
                -------
                field : pyarrow.Field
        """
        pass

    def with_nullable(self, nullable): # real signature unknown; restored from __doc__
        """
        Field.with_nullable(self, nullable)
        
                A copy of this field with the replaced nullability
        
                Parameters
                ----------
                nullable : bool
        
                Returns
                -------
                field: pyarrow.Field
        """
        pass

    def with_type(self, DataType_new_type): # real signature unknown; restored from __doc__
        """
        Field.with_type(self, DataType new_type)
        
                A copy of this field with the replaced type
        
                Parameters
                ----------
                new_type : pyarrow.DataType
        
                Returns
                -------
                field : pyarrow.Field
        """
        pass

    def _export_to_c(self, out_ptr): # real signature unknown; restored from __doc__
        """
        Field._export_to_c(self, out_ptr)
        
                Export to a C ArrowSchema struct, given its pointer.
        
                Be careful: if you don't pass the ArrowSchema struct to a consumer,
                its memory will leak.  This is a low-level function intended for
                expert users.
        """
        pass

    def _import_from_c(self, in_ptr): # real signature unknown; restored from __doc__
        """
        Field._import_from_c(in_ptr)
        
                Import Field from a C ArrowSchema struct, given its pointer.
        
                This is a low-level function intended for expert users.
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

    def __hash__(self, *args, **kwargs): # real signature unknown
        """ Return hash(self). """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
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
        """ Field.__reduce__(self) """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    metadata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    nullable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001970BC825D0>'


