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


from .YearOffset import YearOffset

class YearEnd(YearOffset):
    """
    DateOffset increments between calendar year ends.
    
        Examples
        --------
        >>> ts = pd.Timestamp(2022, 1, 1)
        >>> ts + pd.offsets.YearEnd()
        Timestamp('2022-12-31 00:00:00')
    """
    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    _period_dtype_code = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    _day_opt = 'end'
    _default_month = 12
    _prefix = 'A'
    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x00000215D894DE40>'


