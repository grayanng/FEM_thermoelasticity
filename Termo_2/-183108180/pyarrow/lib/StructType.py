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


from .DataType import DataType

class StructType(DataType):
    """
    Concrete class for struct data types.
    
        ``StructType`` supports direct indexing using ``[...]`` (implemented via
        ``__getitem__``) to access its fields.
        It will return the struct field with the given index or name.
    
        Examples
        --------
        >>> import pyarrow as pa
    
        Accessing fields using direct indexing:
    
        >>> struct_type = pa.struct({'x': pa.int32(), 'y': pa.string()})
        >>> struct_type[0]
        pyarrow.Field<x: int32>
        >>> struct_type['y']
        pyarrow.Field<y: string>
    
        Accessing fields using ``field()``:
    
        >>> struct_type.field(1)
        pyarrow.Field<y: string>
        >>> struct_type.field('x')
        pyarrow.Field<x: int32>
    
        # Creating a schema from the struct type's fields:
        >>> pa.schema(list(struct_type))
        x: int32
        y: string
    """
    def field(self, i): # real signature unknown; restored from __doc__
        """
        StructType.field(self, i) -> Field
        
                Select a field by its column name or numeric index.
        
                Parameters
                ----------
                i : int or str
        
                Returns
                -------
                pyarrow.Field
        
                Examples
                --------
        
                >>> import pyarrow as pa
                >>> struct_type = pa.struct({'x': pa.int32(), 'y': pa.string()})
        
                Select the second field:
        
                >>> struct_type.field(1)
                pyarrow.Field<y: string>
        
                Select the field named 'x':
        
                >>> struct_type.field('x')
                pyarrow.Field<x: int32>
        """
        return Field

    def get_all_field_indices(self, name): # real signature unknown; restored from __doc__
        """
        StructType.get_all_field_indices(self, name)
        
                Return sorted list of indices for the fields with the given name.
        
                Parameters
                ----------
                name : str
                    The name of the field to look up.
        
                Returns
                -------
                indices : List[int]
        """
        pass

    def get_field_index(self, name): # real signature unknown; restored from __doc__
        """
        StructType.get_field_index(self, name)
        
                Return index of the unique field with the given name.
        
                Parameters
                ----------
                name : str
                    The name of the field to look up.
        
                Returns
                -------
                index : int
                    The index of the field with the given name; -1 if the
                    name isn't found or there are several fields with the given
                    name.
        """
        pass

    def __getitem__(self, *args, **kwargs): # real signature unknown
        """
        Return the struct field with the given index or name.
        
                Alias of ``field``.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __iter__(self, *args, **kwargs): # real signature unknown
        """ Iterate over struct fields, in order. """
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Like num_fields(). """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self): # real signature unknown; restored from __doc__
        """ StructType.__reduce__(self) """
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001970BC823F0>'


