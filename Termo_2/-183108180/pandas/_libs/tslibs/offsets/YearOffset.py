# encoding: utf-8
# module pandas._libs.tslibs.offsets
# from C:\Users\akharin\PycharmProjects\pythonProject\venv\lib\site-packages\pandas\_libs\tslibs\offsets.cp39-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import operator as operator # C:\Users\akharin\AppData\Local\Programs\Python\Python39\lib\operator.py
import re as re # C:\Users\akharin\AppData\Local\Programs\Python\Python39\lib\re.py
import time as time # <module 'time' (built-in)>
import warnings as warnings # C:\Users\akharin\AppData\Local\Programs\Python\Python39\lib\warnings.py
import numpy as np # C:\Users\akharin\PycharmProjects\pythonProject\venv\lib\site-packages\numpy\__init__.py
from pandas._libs.properties import cache_readonly

from pandas._libs.tslibs.timedeltas import Timedelta

from pandas._libs.tslibs.timestamps import Timestamp


from .SingleConstructorOffset import SingleConstructorOffset

class YearOffset(SingleConstructorOffset):
    """ DateOffset that just needs a month. """
    def is_on_offset(self, *args, **kwargs): # real signature unknown
        pass

    def _apply(self, *args, **kwargs): # real signature unknown
        pass

    def _apply_array(self, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def _from_name(cls, *args, **kwargs): # real signature unknown
        pass

    def _get_offset_day(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    month = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    rule_code = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    _attributes = (
        'n',
        'normalize',
        'month',
    )
    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x00000215D894DD20>'


