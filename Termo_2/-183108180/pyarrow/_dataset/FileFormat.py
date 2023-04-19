# encoding: utf-8
# module pyarrow._dataset
# from C:\Users\akharin\PycharmProjects\pythonProject\venv\lib\site-packages\pyarrow\_dataset.cp39-win_amd64.pyd
# by generator 1.147
""" Dataset is currently unstable. APIs subject to change without notice. """

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import codecs as codecs # C:\Users\akharin\AppData\Local\Programs\Python\Python39\lib\codecs.py
import collections as collections # C:\Users\akharin\AppData\Local\Programs\Python\Python39\lib\collections\__init__.py
import os as os # C:\Users\akharin\AppData\Local\Programs\Python\Python39\lib\os.py
import warnings as warnings # C:\Users\akharin\AppData\Local\Programs\Python\Python39\lib\warnings.py
import pyarrow as pa # C:\Users\akharin\PycharmProjects\pythonProject\venv\lib\site-packages\pyarrow\__init__.py
from pyarrow.lib import ArrowTypeError, _pc, frombytes, tobytes

import importlib._bootstrap as __importlib__bootstrap
import pyarrow.lib as __pyarrow_lib


class FileFormat(__pyarrow_lib._Weakrefable):
    """ FileFormat() """
    def inspect(self, file, filesystem=None): # real signature unknown; restored from __doc__
        """
        FileFormat.inspect(self, file, filesystem=None)
        
                Infer the schema of a file.
        
                Parameters
                ----------
                file : file-like object, path-like or str
                    The file or file path to infer a schema from.
                filesystem : Filesystem, optional
                    If `filesystem` is given, `file` must be a string and specifies
                    the path of the file to read from the filesystem.
        
                Returns
                -------
                schema : Schema
                    The schema inferred from the file
        """
        pass

    def make_fragment(self, file, filesystem=None, Expression_partition_expression=None): # real signature unknown; restored from __doc__
        """
        FileFormat.make_fragment(self, file, filesystem=None, Expression partition_expression=None)
        
                Make a FileFragment from a given file.
        
                Parameters
                ----------
                file : file-like object, path-like or str
                    The file or file path to make a fragment from.
                filesystem : Filesystem, optional
                    If `filesystem` is given, `file` must be a string and specifies
                    the path of the file to read from the filesystem.
                partition_expression : Expression
                    The filter expression.
        """
        pass

    def make_write_options(self): # real signature unknown; restored from __doc__
        """ FileFormat.make_write_options(self) """
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

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ FileFormat.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ FileFormat.__setstate_cython__(self, __pyx_state) """
        pass

    default_extname = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    default_fragment_scan_options = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __hash__ = None
    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x00000187AB21E4B0>'


