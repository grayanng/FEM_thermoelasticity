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


from .RelativeDeltaOffset import RelativeDeltaOffset

class DateOffset(RelativeDeltaOffset):
    """
    Standard kind of date increment used for a date range.
    
        Works exactly like the keyword argument form of relativedelta.
        Note that the positional argument form of relativedelata is not
        supported. Use of the keyword n is discouraged-- you would be better
        off specifying n in the keywords you use, but regardless it is
        there for you. n is needed for DateOffset subclasses.
    
        DateOffset works as follows.  Each offset specify a set of dates
        that conform to the DateOffset.  For example, Bday defines this
        set to be the set of dates that are weekdays (M-F).  To test if a
        date is in the set of a DateOffset dateOffset we can use the
        is_on_offset method: dateOffset.is_on_offset(date).
    
        If a date is not on a valid date, the rollback and rollforward
        methods can be used to roll the date to the nearest valid date
        before/after the date.
    
        DateOffsets can be created to move dates forward a given number of
        valid dates.  For example, Bday(2) can be added to a date to move
        it two business days forward.  If the date does not start on a
        valid date, first it is moved to a valid date.  Thus pseudo code
        is:
    
        def __add__(date):
          date = rollback(date) # does nothing if date is valid
          return date + <n number of periods>
    
        When a date offset is created for a negative number of periods,
        the date is first rolled forward.  The pseudo code is:
    
        def __add__(date):
          date = rollforward(date) # does nothing is date is valid
          return date + <n number of periods>
    
        Zero presents a problem.  Should it roll forward or back?  We
        arbitrarily have it rollforward:
    
        date + BDay(0) == BDay.rollforward(date)
    
        Since 0 is a bit weird, we suggest avoiding its use.
    
        Besides, adding a DateOffsets specified by the singular form of the date
        component can be used to replace certain component of the timestamp.
    
        Parameters
        ----------
        n : int, default 1
            The number of time periods the offset represents.
            If specified without a temporal pattern, defaults to n days.
        normalize : bool, default False
            Whether to round the result of a DateOffset addition down to the
            previous midnight.
        **kwds
            Temporal parameter that add to or replace the offset value.
    
            Parameters that **add** to the offset (like Timedelta):
    
            - years
            - months
            - weeks
            - days
            - hours
            - minutes
            - seconds
            - milliseconds
            - microseconds
            - nanoseconds
    
            Parameters that **replace** the offset value:
    
            - year
            - month
            - day
            - weekday
            - hour
            - minute
            - second
            - microsecond
            - nanosecond.
    
        See Also
        --------
        dateutil.relativedelta.relativedelta : The relativedelta type is designed
            to be applied to an existing datetime an can replace specific components of
            that datetime, or represents an interval of time.
    
        Examples
        --------
        >>> from pandas.tseries.offsets import DateOffset
        >>> ts = pd.Timestamp('2017-01-01 09:10:11')
        >>> ts + DateOffset(months=3)
        Timestamp('2017-04-01 09:10:11')
    
        >>> ts = pd.Timestamp('2017-01-01 09:10:11')
        >>> ts + DateOffset(months=2)
        Timestamp('2017-03-01 09:10:11')
        >>> ts + DateOffset(day=31)
        Timestamp('2017-01-31 09:10:11')
    
        >>> ts + pd.DateOffset(hour=8)
        Timestamp('2017-01-01 08:10:11')
    """
    def __init__(self, months=3): # real signature unknown; restored from __doc__
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is 'mappingproxy({\'__module__\': \'pandas._libs.tslibs.offsets\', \'__doc__\': "\\n    Standard kind of date increment used for a date range.\\n\\n    Works exactly like the keyword argument form of relativedelta.\\n    Note that the positional argument form of relativedelata is not\\n    supported. Use of the keyword n is discouraged-- you would be better\\n    off specifying n in the keywords you use, but regardless it is\\n    there for you. n is needed for DateOffset subclasses.\\n\\n    DateOffset works as follows.  Each offset specify a set of dates\\n    that conform to the DateOffset.  For example, Bday defines this\\n    set to be the set of dates that are weekdays (M-F).  To test if a\\n    date is in the set of a DateOffset dateOffset we can use the\\n    is_on_offset method: dateOffset.is_on_offset(date).\\n\\n    If a date is not on a valid date, the rollback and rollforward\\n    methods can be used to roll the date to the nearest valid date\\n    before/after the date.\\n\\n    DateOffsets can be created to move dates forward a given number of\\n    valid dates.  For example, Bday(2) can be added to a date to move\\n    it two business days forward.  If the date does not start on a\\n    valid date, first it is moved to a valid date.  Thus pseudo code\\n    is:\\n\\n    def __add__(date):\\n      date = rollback(date) # does nothing if date is valid\\n      return date + <n number of periods>\\n\\n    When a date offset is created for a negative number of periods,\\n    the date is first rolled forward.  The pseudo code is:\\n\\n    def __add__(date):\\n      date = rollforward(date) # does nothing is date is valid\\n      return date + <n number of periods>\\n\\n    Zero presents a problem.  Should it roll forward or back?  We\\n    arbitrarily have it rollforward:\\n\\n    date + BDay(0) == BDay.rollforward(date)\\n\\n    Since 0 is a bit weird, we suggest avoiding its use.\\n\\n    Besides, adding a DateOffsets specified by the singular form of the date\\n    component can be used to replace certain component of the timestamp.\\n\\n    Parameters\\n    ----------\\n    n : int, default 1\\n        The number of time periods the offset represents.\\n        If specified without a temporal pattern, defaults to n days.\\n    normalize : bool, default False\\n        Whether to round the result of a DateOffset addition down to the\\n        previous midnight.\\n    **kwds\\n        Temporal parameter that add to or replace the offset value.\\n\\n        Parameters that **add** to the offset (like Timedelta):\\n\\n        - years\\n        - months\\n        - weeks\\n        - days\\n        - hours\\n        - minutes\\n        - seconds\\n        - milliseconds\\n        - microseconds\\n        - nanoseconds\\n\\n        Parameters that **replace** the offset value:\\n\\n        - year\\n        - month\\n        - day\\n        - weekday\\n        - hour\\n        - minute\\n        - second\\n        - microsecond\\n        - nanosecond.\\n\\n    See Also\\n    --------\\n    dateutil.relativedelta.relativedelta : The relativedelta type is designed\\n        to be applied to an existing datetime an can replace specific components of\\n        that datetime, or represents an interval of time.\\n\\n    Examples\\n    --------\\n    >>> from pandas.tseries.offsets import DateOffset\\n    >>> ts = pd.Timestamp(\'2017-01-01 09:10:11\')\\n    >>> ts + DateOffset(months=3)\\n    Timestamp(\'2017-04-01 09:10:11\')\\n\\n    >>> ts = pd.Timestamp(\'2017-01-01 09:10:11\')\\n    >>> ts + DateOffset(months=2)\\n    Timestamp(\'2017-03-01 09:10:11\')\\n    >>> ts + DateOffset(day=31)\\n    Timestamp(\'2017-01-31 09:10:11\')\\n\\n    >>> ts + pd.DateOffset(hour=8)\\n    Timestamp(\'2017-01-01 08:10:11\')\\n    ", \'__setattr__\': <cyfunction DateOffset.__setattr__ at 0x00000215D9247790>, \'__dict__\': <attribute \'__dict__\' of \'DateOffset\' objects>, \'__weakref__\': <attribute \'__weakref__\' of \'DateOffset\' objects>})'


