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

class BYearEnd(YearOffset):
    """
    DateOffset increments between the last business day of the year.
    
        Examples
        --------
        >>> from pandas.tseries.offsets import BYearEnd
        >>> ts = pd.Timestamp('2020-05-24 05:01:15')
        >>> ts - BYearEnd()
        Timestamp('2019-12-31 05:01:15')
        >>> ts + BYearEnd()
        Timestamp('2020-12-31 05:01:15')
        >>> ts + BYearEnd(3)
        Timestamp('2022-12-30 05:01:15')
        >>> ts + BYearEnd(-3)
        Timestamp('2017-12-29 05:01:15')
        >>> ts + BYearEnd(month=11)
        Timestamp('2020-11-30 05:01:15')
    """
    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    _day_opt = 'business_end'
    _default_month = 12
    _outputName = 'BusinessYearEnd'
    _prefix = 'BA'
    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x00000215D894DD80>'


