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

class Scalar(_Weakrefable):
    """
    Scalar()
    
        The base class for scalars.
    """
    def as_py(self): # real signature unknown; restored from __doc__
        """ Scalar.as_py(self) """
        pass

    def cast(self, target_type): # real signature unknown; restored from __doc__
        """
        Scalar.cast(self, target_type)
        
                Attempt a safe cast to target data type.
        
                Parameters
                ----------
                target_type : DataType or string coercible to DataType
                    The type to cast the scalar to.
        
                Returns
                -------
                scalar : A Scalar of the given target data type.
        """
        pass

    def equals(self, Scalar_other): # real signature unknown; restored from __doc__
        """ Scalar.equals(self, Scalar other) """
        pass

    def validate(self, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        Scalar.validate(self, *, full=False)
        
                Perform validation checks.  An exception is raised if validation fails.
        
                By default only cheap validation checks are run.  Pass `full=True`
                for thorough validation checks (potentially O(n)).
        
                Parameters
                ----------
                full : bool, default False
                    If True, run expensive checks, otherwise cheap checks only.
        
                Raises
                ------
                ArrowInvalid
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
        """ Scalar.__reduce__(self) """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    is_valid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Holds a valid (non-null) value.
        """

    type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Data type of the Scalar object.
        """


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001970BC82F90>'


