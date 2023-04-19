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


from .QuarterOffset import QuarterOffset

class QuarterBegin(QuarterOffset):
    """
    DateOffset increments between Quarter start dates.
    
        startingMonth = 1 corresponds to dates like 1/01/2007, 4/01/2007, ...
        startingMonth = 2 corresponds to dates like 2/01/2007, 5/01/2007, ...
        startingMonth = 3 corresponds to dates like 3/01/2007, 6/01/2007, ...
    
        Examples
        --------
        >>> ts = pd.Timestamp(2022, 1, 1)
        >>> ts + pd.offsets.QuarterBegin()
        Timestamp('2022-03-01 00:00:00')
    """
    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    _day_opt = 'start'
    _default_starting_month = 3
    _from_name_starting_month = 1
    _prefix = 'QS'
    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x00000215D893CF30>'


