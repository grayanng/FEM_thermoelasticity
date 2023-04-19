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


from .FileFormat import FileFormat

class CsvFileFormat(FileFormat):
    """
    CsvFileFormat(ParseOptions parse_options=None, default_fragment_scan_options=None, ConvertOptions convert_options=None, ReadOptions read_options=None)
    
        FileFormat for CSV files.
    
        Parameters
        ----------
        parse_options : pyarrow.csv.ParseOptions
            Options regarding CSV parsing.
        default_fragment_scan_options : CsvFragmentScanOptions
            Default options for fragments scan.
        convert_options : pyarrow.csv.ConvertOptions
            Options regarding value conversion.
        read_options : pyarrow.csv.ReadOptions
            General read options.
    """
    def equals(self, CsvFileFormat_other): # real signature unknown; restored from __doc__
        """ CsvFileFormat.equals(self, CsvFileFormat other) """
        pass

    def make_write_options(self, **kwargs): # real signature unknown; restored from __doc__
        """ CsvFileFormat.make_write_options(self, **kwargs) """
        pass

    def __init__(self, ParseOptions_parse_options=None, default_fragment_scan_options=None, ConvertOptions_convert_options=None, ReadOptions_read_options=None): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self): # real signature unknown; restored from __doc__
        """ CsvFileFormat.__reduce__(self) """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    parse_options = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _read_options_py = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """_read_options_py: pyarrow._csv.ReadOptions"""


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x00000187AB21E960>'
    __slots__ = ()


