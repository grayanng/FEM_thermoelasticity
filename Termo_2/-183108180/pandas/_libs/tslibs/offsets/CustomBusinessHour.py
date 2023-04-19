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


from .BusinessHour import BusinessHour

class CustomBusinessHour(BusinessHour):
    """
    DateOffset subclass representing possibly n custom business days.
    
        Parameters
        ----------
        n : int, default 1
            The number of months represented.
        normalize : bool, default False
            Normalize start/end dates to midnight before generating date range.
        weekmask : str, Default 'Mon Tue Wed Thu Fri'
            Weekmask of valid business days, passed to ``numpy.busdaycalendar``.
        start : str, default "09:00"
            Start time of your custom business hour in 24h format.
        end : str, default: "17:00"
            End time of your custom business hour in 24h format.
    
        Examples
        --------
        >>> ts = pd.Timestamp(2022, 8, 5, 16)
        >>> ts + pd.offsets.CustomBusinessHour()
        Timestamp('2022-08-08 09:00:00')
    """
    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    _anchor = 0
    _attributes = (
        'n',
        'normalize',
        'weekmask',
        'holidays',
        'calendar',
        'start',
        'end',
        'offset',
    )
    _prefix = 'CBH'
    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x00000215D893C8D0>'


