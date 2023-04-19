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


class IOBase(___io._IOBase):
    """
    The abstract base class for all I/O classes.
    
    This class provides dummy implementations for many methods that
    derived classes can override selectively; the default implementations
    represent a file that cannot be read, written or seeked.
    
    Even though IOBase does not declare read, readinto, or write because
    their signatures will vary, implementations and clients should
    consider those methods part of the interface. Also, implementations
    may raise UnsupportedOperation when operations they do not support are
    called.
    
    The basic type used for binary data read from or written to a file is
    bytes. Other bytes-like objects are accepted as method arguments too.
    In some cases (such as readinto), a writable object is required. Text
    I/O classes work with str data.
    
    Note that calling any method (except additional calls to close(),
    which are ignored) on a closed stream should raise a ValueError.
    
    IOBase (and its subclasses) support the iterator protocol, meaning
    that an IOBase object can be iterated over yielding the lines in a
    stream.
    
    IOBase also supports the :keyword:`with` statement. In this example,
    fp is closed after the suite of the with statement is complete:
    
    with open('spam.txt', 'r') as fp:
        fp.write('Spam and eggs!')
    """
    def __init__(self, and_its_subclasses): # real signature unknown; restored from __doc__
        pass

    _abc_impl = None # (!) real value is '<_abc._abc_data object at 0x000001970B540D80>'
    __abstractmethods__ = frozenset()


