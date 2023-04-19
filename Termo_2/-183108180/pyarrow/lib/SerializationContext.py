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

class SerializationContext(_Weakrefable):
    """ SerializationContext() """
    def clone(self): # real signature unknown; restored from __doc__
        """
        SerializationContext.clone(self)
        
                Return copy of this SerializationContext.
        
                Returns
                -------
                clone : SerializationContext
        """
        pass

    def deserialize(self, what): # real signature unknown; restored from __doc__
        """
        SerializationContext.deserialize(self, what)
        
                Call pyarrow.deserialize and pass this SerializationContext.
        """
        pass

    def deserialize_components(self, what): # real signature unknown; restored from __doc__
        """
        SerializationContext.deserialize_components(self, what)
        
                Call pyarrow.deserialize_components and pass this SerializationContext.
        """
        pass

    def register_type(self, type_, type_id, pickle=False, custom_serializer=None, custom_deserializer=None): # real signature unknown; restored from __doc__
        """
        SerializationContext.register_type(self, type_, type_id, pickle=False, custom_serializer=None, custom_deserializer=None)
        
                EXPERIMENTAL: Add type to the list of types we can serialize.
        
                Parameters
                ----------
                type\_ : type
                    The type that we can serialize.
                type_id : string
                    A string used to identify the type.
                pickle : bool
                    True if the serialization should be done with pickle.
                    False if it should be done efficiently with Arrow.
                custom_serializer : callable
                    This argument is optional, but can be provided to
                    serialize objects of the class in a particular way.
                custom_deserializer : callable
                    This argument is optional, but can be provided to
                    deserialize objects of the class in a particular way.
        """
        pass

    def serialize(self, obj): # real signature unknown; restored from __doc__
        """
        SerializationContext.serialize(self, obj)
        
                Call pyarrow.serialize and pass this SerializationContext.
        """
        pass

    def serialize_to(self, value, sink): # real signature unknown; restored from __doc__
        """
        SerializationContext.serialize_to(self, value, sink)
        
                Call pyarrow.serialize_to and pass this SerializationContext.
        """
        pass

    def set_pickle(self, serializer, deserializer): # real signature unknown; restored from __doc__
        """
        SerializationContext.set_pickle(self, serializer, deserializer)
        
                Set the serializer and deserializer to use for objects that are to be
                pickled.
        
                Parameters
                ----------
                serializer : callable
                    The serializer to use (e.g., pickle.dumps or cloudpickle.dumps).
                deserializer : callable
                    The deserializer to use (e.g., pickle.dumps or cloudpickle.dumps).
        """
        pass

    def _deserialize_callback(self, serialized_obj): # real signature unknown; restored from __doc__
        """ SerializationContext._deserialize_callback(self, serialized_obj) """
        pass

    def _serialize_callback(self, obj): # real signature unknown; restored from __doc__
        """ SerializationContext._serialize_callback(self, obj) """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ SerializationContext.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ SerializationContext.__setstate_cython__(self, __pyx_state) """
        pass


