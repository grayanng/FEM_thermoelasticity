# encoding: utf-8
# module pyarrow._compute
# from C:\Users\akharin\PycharmProjects\pythonProject\venv\lib\site-packages\pyarrow\_compute.cp39-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import sys as sys # <module 'sys' (built-in)>
import pyarrow.lib as lib # C:\Users\akharin\PycharmProjects\pythonProject\venv\lib\site-packages\pyarrow\lib.cp39-win_amd64.pyd
import inspect as inspect # C:\Users\akharin\AppData\Local\Programs\Python\Python39\lib\inspect.py
import numpy as np # C:\Users\akharin\PycharmProjects\pythonProject\venv\lib\site-packages\numpy\__init__.py
from pyarrow.lib import ArrowInvalid, frombytes, tobytes

import pyarrow.lib as __pyarrow_lib


from .tuple import tuple

class FunctionDoc(tuple):
    """ FunctionDoc(summary, description, arg_names, options_class, options_required) """
    def _asdict(self): # reliably restored by inspect
        """ Return a new dict which maps field names to their values. """
        pass

    @classmethod
    def _make(cls, *args, **kwargs): # real signature unknown
        """ Make a new FunctionDoc object from a sequence or iterable """
        pass

    def _replace(self, **kwds): # reliably restored by inspect
        """ Return a new FunctionDoc object replacing specified fields with new values """
        pass

    def __getnewargs__(self): # reliably restored by inspect
        """ Return self as a plain tuple.  Used by copy and pickle. """
        pass

    def __init__(self, summary, description, arg_names, options_class, options_required): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(_cls, summary, description, arg_names, options_class, options_required): # reliably restored by inspect
        """ Create new instance of FunctionDoc(summary, description, arg_names, options_class, options_required) """
        pass

    def __repr__(self): # reliably restored by inspect
        """ Return a nicely formatted representation string """
        pass

    arg_names = _tuplegetter(2, 'Alias for field number 2')
    description = _tuplegetter(1, 'Alias for field number 1')
    options_class = _tuplegetter(3, 'Alias for field number 3')
    options_required = _tuplegetter(4, 'Alias for field number 4')
    summary = _tuplegetter(0, 'Alias for field number 0')
    _fields = (
        'summary',
        'description',
        'arg_names',
        'options_class',
        'options_required',
    )
    _field_defaults = {}
    __slots__ = ()


