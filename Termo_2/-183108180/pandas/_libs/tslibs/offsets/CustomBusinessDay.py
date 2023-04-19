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


from .BusinessDay import BusinessDay

class CustomBusinessDay(BusinessDay):
    """
    DateOffset subclass representing custom business days excluding holidays.
    
        Parameters
        ----------
        n : int, default 1
        normalize : bool, default False
            Normalize start/end dates to midnight before generating date range.
        weekmask : str, Default 'Mon Tue Wed Thu Fri'
            Weekmask of valid business days, passed to ``numpy.busdaycalendar``.
        holidays : list
            List/array of dates to exclude from the set of valid business days,
            passed to ``numpy.busdaycalendar``.
        calendar : np.busdaycalendar
        offset : timedelta, default timedelta(0)
    
        Examples
        --------
        >>> ts = pd.Timestamp(2022, 8, 5)
        >>> ts + pd.offsets.CustomBusinessDay(1)
        Timestamp('2022-08-08 00:00:00')
    """
    def is_on_offset(self, *args, **kwargs): # real signature unknown
        pass

    def _apply(self, *args, **kwargs): # real signature unknown
        pass

    def _apply_array(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    _attributes = (
        'n',
        'normalize',
        'weekmask',
        'holidays',
        'calendar',
        'offset',
    )
    _prefix = 'C'
    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x00000215D893C930>'


