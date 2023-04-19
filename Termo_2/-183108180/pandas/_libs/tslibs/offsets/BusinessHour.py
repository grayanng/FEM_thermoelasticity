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


from .BusinessMixin import BusinessMixin

class BusinessHour(BusinessMixin):
    """
    DateOffset subclass representing possibly n business hours.
    
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
        >>> ts + pd.offsets.BusinessHour()
        Timestamp('2022-08-08 09:00:00')
    """
    def is_on_offset(self, *args, **kwargs): # real signature unknown
        pass

    def rollback(self, *args, **kwargs): # real signature unknown
        """ Roll provided date backward to next offset only if not on offset. """
        pass

    def rollforward(self, *args, **kwargs): # real signature unknown
        """ Roll provided date forward to next offset only if not on offset. """
        pass

    def _apply(self, *args, **kwargs): # real signature unknown
        pass

    def _get_business_hours_by_sec(self, *args, **kwargs): # real signature unknown
        """ Return business hours in a day by seconds. """
        pass

    def _get_closing_time(self, *args, **kwargs): # real signature unknown
        """
        Get the closing time of a business hour interval by its opening time.
        
                Parameters
                ----------
                dt : datetime
                    Opening time of a business hour interval.
        
                Returns
                -------
                result : datetime
                    Corresponding closing time.
        """
        pass

    def _is_on_offset(self, *args, **kwargs): # real signature unknown
        """ Slight speedups using calculated values. """
        pass

    def _next_opening_time(self, *args, **kwargs): # real signature unknown
        """
        If self.n and sign have the same sign, return the earliest opening time
                later than or equal to current time.
                Otherwise the latest opening time earlier than or equal to current
                time.
        
                Opening time always locates on BusinessDay.
                However, closing time may not if business hour extends over midnight.
        
                Parameters
                ----------
                other : datetime
                    Current time.
                sign : int, default 1.
                    Either 1 or -1. Going forward in time if it has the same sign as
                    self.n. Going backward in time otherwise.
        
                Returns
                -------
                result : datetime
                    Next opening time.
        """
        pass

    def _prev_opening_time(self, *args, **kwargs): # real signature unknown
        """
        If n is positive, return the latest opening time earlier than or equal
                to current time.
                Otherwise the earliest opening time later than or equal to current
                time.
        
                Parameters
                ----------
                other : datetime
                    Current time.
        
                Returns
                -------
                result : datetime
                    Previous opening time.
        """
        pass

    def _repr_attrs(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    end = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    start = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    next_bday = None # (!) real value is '<pandas._libs.properties.CachedProperty object at 0x00000215D924B740>'
    _adjust_dst = False
    _anchor = 0
    _attributes = (
        'n',
        'normalize',
        'start',
        'end',
        'offset',
    )
    _prefix = 'BH'
    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x00000215D894DC90>'


