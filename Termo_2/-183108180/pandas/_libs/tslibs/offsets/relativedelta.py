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


from .object import object

class relativedelta(object):
    """
    The relativedelta type is designed to be applied to an existing datetime and
        can replace specific components of that datetime, or represents an interval
        of time.
    
        It is based on the specification of the excellent work done by M.-A. Lemburg
        in his
        `mx.DateTime <https://www.egenix.com/products/python/mxBase/mxDateTime/>`_ extension.
        However, notice that this type does *NOT* implement the same algorithm as
        his work. Do *NOT* expect it to behave like mx.DateTime's counterpart.
    
        There are two different ways to build a relativedelta instance. The
        first one is passing it two date/datetime classes::
    
            relativedelta(datetime1, datetime2)
    
        The second one is passing it any number of the following keyword arguments::
    
            relativedelta(arg1=x,arg2=y,arg3=z...)
    
            year, month, day, hour, minute, second, microsecond:
                Absolute information (argument is singular); adding or subtracting a
                relativedelta with absolute information does not perform an arithmetic
                operation, but rather REPLACES the corresponding value in the
                original datetime with the value(s) in relativedelta.
    
            years, months, weeks, days, hours, minutes, seconds, microseconds:
                Relative information, may be negative (argument is plural); adding
                or subtracting a relativedelta with relative information performs
                the corresponding arithmetic operation on the original datetime value
                with the information in the relativedelta.
    
            weekday: 
                One of the weekday instances (MO, TU, etc) available in the
                relativedelta module. These instances may receive a parameter N,
                specifying the Nth weekday, which could be positive or negative
                (like MO(+1) or MO(-2)). Not specifying it is the same as specifying
                +1. You can also use an integer, where 0=MO. This argument is always
                relative e.g. if the calculated date is already Monday, using MO(1)
                or MO(-1) won't change the day. To effectively make it absolute, use
                it in combination with the day argument (e.g. day=1, MO(1) for first
                Monday of the month).
    
            leapdays:
                Will add given days to the date found, if year is a leap
                year, and the date found is post 28 of february.
    
            yearday, nlyearday:
                Set the yearday or the non-leap year day (jump leap days).
                These are converted to day/month/leapdays information.
    
        There are relative and absolute forms of the keyword
        arguments. The plural is relative, and the singular is
        absolute. For each argument in the order below, the absolute form
        is applied first (by setting each attribute to that value) and
        then the relative form (by adding the value to the attribute).
    
        The order of attributes considered when this relativedelta is
        added to a datetime is:
    
        1. Year
        2. Month
        3. Day
        4. Hours
        5. Minutes
        6. Seconds
        7. Microseconds
    
        Finally, weekday is applied, using the rule described above.
    
        For example
    
        >>> from datetime import datetime
        >>> from dateutil.relativedelta import relativedelta, MO
        >>> dt = datetime(2018, 4, 9, 13, 37, 0)
        >>> delta = relativedelta(hours=25, day=1, weekday=MO(1))
        >>> dt + delta
        datetime.datetime(2018, 4, 2, 14, 37)
    
        First, the day is set to 1 (the first of the month), then 25 hours
        are added, to get to the 2nd day and 14th hour, finally the
        weekday is applied, but since the 2nd is already a Monday there is
        no effect.
    """
    def normalized(self): # reliably restored by inspect
        """
        Return a version of this object represented entirely using integer
                values for the relative attributes.
        
                >>> relativedelta(days=1.5, hours=2).normalized()
                relativedelta(days=+1, hours=+14)
        
                :return:
                    Returns a :class:`dateutil.relativedelta.relativedelta` object.
        """
        pass

    def _fix(self): # reliably restored by inspect
        # no doc
        pass

    def _set_months(self, months): # reliably restored by inspect
        # no doc
        pass

    def __abs__(self): # reliably restored by inspect
        # no doc
        pass

    def __add__(self, other): # reliably restored by inspect
        # no doc
        pass

    def __bool__(self): # reliably restored by inspect
        # no doc
        pass

    def __div__(self, other): # reliably restored by inspect
        # no doc
        pass

    def __eq__(self, other): # reliably restored by inspect
        # no doc
        pass

    def __hash__(self): # reliably restored by inspect
        # no doc
        pass

    def __init__(self, dt1=None, dt2=None, years=0, months=0, days=0, leapdays=0, weeks=0, hours=0, minutes=0, seconds=0, microseconds=0, year=None, month=None, day=None, weekday=None, yearday=None, nlyearday=None, hour=None, minute=None, second=None, microsecond=None): # reliably restored by inspect
        # no doc
        pass

    def __mul__(self, other): # reliably restored by inspect
        # no doc
        pass

    def __neg__(self): # reliably restored by inspect
        # no doc
        pass

    def __ne__(self, other): # reliably restored by inspect
        # no doc
        pass

    def __nonzero__(self): # reliably restored by inspect
        # no doc
        pass

    def __radd__(self, other): # reliably restored by inspect
        # no doc
        pass

    def __repr__(self): # reliably restored by inspect
        # no doc
        pass

    def __rmul__(self, other): # reliably restored by inspect
        # no doc
        pass

    def __rsub__(self, other): # reliably restored by inspect
        # no doc
        pass

    def __sub__(self, other): # reliably restored by inspect
        # no doc
        pass

    def __truediv__(self, other): # reliably restored by inspect
        # no doc
        pass

    weeks = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is 'mappingproxy({\'__module__\': \'dateutil.relativedelta\', \'__doc__\': "\\n    The relativedelta type is designed to be applied to an existing datetime and\\n    can replace specific components of that datetime, or represents an interval\\n    of time.\\n\\n    It is based on the specification of the excellent work done by M.-A. Lemburg\\n    in his\\n    `mx.DateTime <https://www.egenix.com/products/python/mxBase/mxDateTime/>`_ extension.\\n    However, notice that this type does *NOT* implement the same algorithm as\\n    his work. Do *NOT* expect it to behave like mx.DateTime\'s counterpart.\\n\\n    There are two different ways to build a relativedelta instance. The\\n    first one is passing it two date/datetime classes::\\n\\n        relativedelta(datetime1, datetime2)\\n\\n    The second one is passing it any number of the following keyword arguments::\\n\\n        relativedelta(arg1=x,arg2=y,arg3=z...)\\n\\n        year, month, day, hour, minute, second, microsecond:\\n            Absolute information (argument is singular); adding or subtracting a\\n            relativedelta with absolute information does not perform an arithmetic\\n            operation, but rather REPLACES the corresponding value in the\\n            original datetime with the value(s) in relativedelta.\\n\\n        years, months, weeks, days, hours, minutes, seconds, microseconds:\\n            Relative information, may be negative (argument is plural); adding\\n            or subtracting a relativedelta with relative information performs\\n            the corresponding arithmetic operation on the original datetime value\\n            with the information in the relativedelta.\\n\\n        weekday: \\n            One of the weekday instances (MO, TU, etc) available in the\\n            relativedelta module. These instances may receive a parameter N,\\n            specifying the Nth weekday, which could be positive or negative\\n            (like MO(+1) or MO(-2)). Not specifying it is the same as specifying\\n            +1. You can also use an integer, where 0=MO. This argument is always\\n            relative e.g. if the calculated date is already Monday, using MO(1)\\n            or MO(-1) won\'t change the day. To effectively make it absolute, use\\n            it in combination with the day argument (e.g. day=1, MO(1) for first\\n            Monday of the month).\\n\\n        leapdays:\\n            Will add given days to the date found, if year is a leap\\n            year, and the date found is post 28 of february.\\n\\n        yearday, nlyearday:\\n            Set the yearday or the non-leap year day (jump leap days).\\n            These are converted to day/month/leapdays information.\\n\\n    There are relative and absolute forms of the keyword\\n    arguments. The plural is relative, and the singular is\\n    absolute. For each argument in the order below, the absolute form\\n    is applied first (by setting each attribute to that value) and\\n    then the relative form (by adding the value to the attribute).\\n\\n    The order of attributes considered when this relativedelta is\\n    added to a datetime is:\\n\\n    1. Year\\n    2. Month\\n    3. Day\\n    4. Hours\\n    5. Minutes\\n    6. Seconds\\n    7. Microseconds\\n\\n    Finally, weekday is applied, using the rule described above.\\n\\n    For example\\n\\n    >>> from datetime import datetime\\n    >>> from dateutil.relativedelta import relativedelta, MO\\n    >>> dt = datetime(2018, 4, 9, 13, 37, 0)\\n    >>> delta = relativedelta(hours=25, day=1, weekday=MO(1))\\n    >>> dt + delta\\n    datetime.datetime(2018, 4, 2, 14, 37)\\n\\n    First, the day is set to 1 (the first of the month), then 25 hours\\n    are added, to get to the 2nd day and 14th hour, finally the\\n    weekday is applied, but since the 2nd is already a Monday there is\\n    no effect.\\n\\n    ", \'__init__\': <function relativedelta.__init__ at 0x00000215D92403A0>, \'_fix\': <function relativedelta._fix at 0x00000215D9240790>, \'weeks\': <property object at 0x00000215D924A1D0>, \'_set_months\': <function relativedelta._set_months at 0x00000215D9240940>, \'normalized\': <function relativedelta.normalized at 0x00000215D92409D0>, \'__add__\': <function relativedelta.__add__ at 0x00000215D9240A60>, \'__radd__\': <function relativedelta.__radd__ at 0x00000215D9240AF0>, \'__rsub__\': <function relativedelta.__rsub__ at 0x00000215D9240B80>, \'__sub__\': <function relativedelta.__sub__ at 0x00000215D9240C10>, \'__abs__\': <function relativedelta.__abs__ at 0x00000215D9240CA0>, \'__neg__\': <function relativedelta.__neg__ at 0x00000215D9240D30>, \'__bool__\': <function relativedelta.__bool__ at 0x00000215D9240DC0>, \'__nonzero__\': <function relativedelta.__bool__ at 0x00000215D9240DC0>, \'__mul__\': <function relativedelta.__mul__ at 0x00000215D9240E50>, \'__rmul__\': <function relativedelta.__mul__ at 0x00000215D9240E50>, \'__eq__\': <function relativedelta.__eq__ at 0x00000215D9240EE0>, \'__hash__\': <function relativedelta.__hash__ at 0x00000215D9240F70>, \'__ne__\': <function relativedelta.__ne__ at 0x00000215D924C040>, \'__div__\': <function relativedelta.__div__ at 0x00000215D924C0D0>, \'__truediv__\': <function relativedelta.__div__ at 0x00000215D924C0D0>, \'__repr__\': <function relativedelta.__repr__ at 0x00000215D924C160>, \'__dict__\': <attribute \'__dict__\' of \'relativedelta\' objects>, \'__weakref__\': <attribute \'__weakref__\' of \'relativedelta\' objects>})'


