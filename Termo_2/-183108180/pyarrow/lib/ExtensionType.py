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


from .BaseExtensionType import BaseExtensionType

class ExtensionType(BaseExtensionType):
    """
    ExtensionType(DataType storage_type, extension_name)
    
        Concrete base class for Python-defined extension types.
    
        Parameters
        ----------
        storage_type : DataType
        extension_name : str
    """
    def __arrow_ext_class__(self): # real signature unknown; restored from __doc__
        """
        ExtensionType.__arrow_ext_class__(self)
        Return an extension array class to be used for building or
                deserializing arrays with this extension type.
        
                This method should return a subclass of the ExtensionArray class. By
                default, if not specialized in the extension implementation, an
                extension type array will be a built-in ExtensionArray instance.
        """
        pass

    @classmethod
    def __arrow_ext_deserialize__(cls, type_self, storage_type, serialized): # real signature unknown; restored from __doc__
        """
        ExtensionType.__arrow_ext_deserialize__(type self, storage_type, serialized)
        
                Return an extension type instance from the storage type and serialized
                metadata.
        
                This method should return an instance of the ExtensionType subclass
                that matches the passed storage type and serialized metadata (the
                return value of ``__arrow_ext_serialize__``).
        """
        pass

    def __arrow_ext_scalar_class__(self): # real signature unknown; restored from __doc__
        """
        ExtensionType.__arrow_ext_scalar_class__(self)
        Return an extension scalar class for building scalars with this
                extension type.
        
                This method should return subclass of the ExtensionScalar class. By
                default, if not specialized in the extension implementation, an
                extension type scalar will be a built-in ExtensionScalar instance.
        """
        pass

    def __arrow_ext_serialize__(self): # real signature unknown; restored from __doc__
        """
        ExtensionType.__arrow_ext_serialize__(self)
        
                Serialized representation of metadata to reconstruct the type object.
        
                This method should return a bytes object, and those serialized bytes
                are stored in the custom metadata of the Field holding an extension
                type in an IPC message.
                The bytes are passed to ``__arrow_ext_deserialize`` and should hold
                sufficient information to reconstruct the data type instance.
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
        """
        Initialize an extension type instance.
        
                This should be called at the end of the subclass'
                ``__init__`` method.
        """
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

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    __hash__ = None
    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001970BC824E0>'


