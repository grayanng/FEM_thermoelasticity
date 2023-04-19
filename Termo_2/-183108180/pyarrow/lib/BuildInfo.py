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


from .tuple import tuple

class BuildInfo(tuple):
    """ BuildInfo(version, version_info, so_version, full_so_version, compiler_id, compiler_version, compiler_flags, git_id, git_description, package_kind, build_type) """
    def _asdict(self): # reliably restored by inspect
        """ Return a new dict which maps field names to their values. """
        pass

    @classmethod
    def _make(cls, *args, **kwargs): # real signature unknown
        """ Make a new BuildInfo object from a sequence or iterable """
        pass

    def _replace(self, **kwds): # reliably restored by inspect
        """ Return a new BuildInfo object replacing specified fields with new values """
        pass

    def __getnewargs__(self): # reliably restored by inspect
        """ Return self as a plain tuple.  Used by copy and pickle. """
        pass

    def __init__(self, version, version_info, so_version, full_so_version, compiler_id, compiler_version, compiler_flags, git_id, git_description, package_kind, build_type): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(_cls, version, version_info, so_version, full_so_version, compiler_id, compiler_version, compiler_flags, git_id, git_description, package_kind, build_type): # reliably restored by inspect
        """ Create new instance of BuildInfo(version, version_info, so_version, full_so_version, compiler_id, compiler_version, compiler_flags, git_id, git_description, package_kind, build_type) """
        pass

    def __repr__(self): # reliably restored by inspect
        """ Return a nicely formatted representation string """
        pass

    build_type = _tuplegetter(10, 'Alias for field number 10')
    compiler_flags = _tuplegetter(6, 'Alias for field number 6')
    compiler_id = _tuplegetter(4, 'Alias for field number 4')
    compiler_version = _tuplegetter(5, 'Alias for field number 5')
    full_so_version = _tuplegetter(3, 'Alias for field number 3')
    git_description = _tuplegetter(8, 'Alias for field number 8')
    git_id = _tuplegetter(7, 'Alias for field number 7')
    package_kind = _tuplegetter(9, 'Alias for field number 9')
    so_version = _tuplegetter(2, 'Alias for field number 2')
    version = _tuplegetter(0, 'Alias for field number 0')
    version_info = _tuplegetter(1, 'Alias for field number 1')
    _fields = (
        'version',
        'version_info',
        'so_version',
        'full_so_version',
        'compiler_id',
        'compiler_version',
        'compiler_flags',
        'git_id',
        'git_description',
        'package_kind',
        'build_type',
    )
    _field_defaults = {}
    __slots__ = ()


