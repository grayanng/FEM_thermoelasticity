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

class BQuarterBegin(QuarterOffset):
    """
    DateOffset increments between the first business day of each Quarter.
    
        startingMonth = 1 corresponds to dates like 1/01/2007, 4/01/2007, ...
        startingMonth = 2 corresponds to dates like 2/01/2007, 5/01/2007, ...
        startingMonth = 3 corresponds to dates like 3/01/2007, 6/01/2007, ...
    
        Examples
        --------
        >>> from pandas.tseries.offsets import BQuarterBegin
        >>> ts = pd.Timestamp('2020-05-24 05:01:15')
        >>> ts + BQuarterBegin()
        Timestamp('2020-06-01 05:01:15')
        >>> ts + BQuarterBegin(2)
        Timestamp('2020-09-01 05:01:15')
        >>> ts + BQuarterBegin(startingMonth=2)
        Timestamp('2020-08-03 05:01:15')
        >>> ts + BQuarterBegin(-1)
        Timestamp('2020-03-02 05:01:15')
    """
    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    _day_opt = 'business_start'
    _default_starting_month = 3
    _from_name_starting_month = 1
    _output_name = 'BusinessQuarterBegin'
    _prefix = 'BQS'
    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x00000215D894DFC0>'


