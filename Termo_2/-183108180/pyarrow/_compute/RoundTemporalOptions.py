# encoding: utf-8
# module pyarrow._compute
# from C:\Users\akharin\PycharmProjects\pythonProject\venv\lib\site-packages\pyarrow\_compute.cp39-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import sys as sys # <module 'sys' (built-in)>
import pyarrow.lib as lib # C:\Users\akharin\PycharmProjects\pythonProject\venv\lib\site-packages\pyarrow\lib.cp39-win_amd64.pyd
import inspect as inspect # C:\Users\akharin\AppData\Local\Programs\Python\Python39\lib\inspect.py
import numpy as np # C:\Users\akharin\PycharmProjects\pythonProject\venv\lib\site-packages\numpy\__init__.py
from pyarrow.lib import ArrowInvalid, frombytes, tobytes

import pyarrow.lib as __pyarrow_lib


from ._RoundTemporalOptions import _RoundTemporalOptions

class RoundTemporalOptions(_RoundTemporalOptions):
    """
    Options for rounding temporal values.
    
        Parameters
        ----------
        multiple : int, default 1
            Number of units to round to.
        unit : str, default "day"
            The unit in which `multiple` is expressed.
            Accepted values are "year", "quarter", "month", "week", "day",
            "hour", "minute", "second", "millisecond", "microsecond",
            "nanosecond".
        week_starts_monday : bool, default True
            If True, weeks start on Monday; if False, on Sunday.
        ceil_is_strictly_greater : bool, default False
            If True, ceil returns a rounded value that is strictly greater than the
            input. For example: ceiling 1970-01-01T00:00:00 to 3 hours would
            yield 1970-01-01T03:00:00 if set to True and 1970-01-01T00:00:00
            if set to False.
            This applies to the ceil_temporal function only.
        calendar_based_origin : bool, default False
            By default, the origin is 1970-01-01T00:00:00. By setting this to True,
            rounding origin will be beginning of one less precise calendar unit.
            E.g.: rounding to hours will use beginning of day as origin.
    
            By default time is rounded to a multiple of units since
            1970-01-01T00:00:00. By setting calendar_based_origin to true,
            time will be rounded to number of units since the last greater
            calendar unit.
            For example: rounding to multiple of days since the beginning of the
            month or to hours since the beginning of the day.
            Exceptions: week and quarter are not used as greater units,
            therefore days will be rounded to the beginning of the month not
            week. Greater unit of week is a year.
            Note that ceiling and rounding might change sorting order of an array
            near greater unit change. For example rounding YYYY-mm-dd 23:00:00 to
            5 hours will ceil and round to YYYY-mm-dd+1 01:00:00 and floor to
            YYYY-mm-dd 20:00:00. On the other hand YYYY-mm-dd+1 00:00:00 will
            ceil, round and floor to YYYY-mm-dd+1 00:00:00. This can break the
            order of an already ordered array.
    """
    def __init__(self, multiple=1, unit=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ RoundTemporalOptions.__init__(self, multiple=1, unit=u'day', *, week_starts_monday=True, ceil_is_strictly_greater=False, calendar_based_origin=False) """
        pass

    __dict__ = None # (!) real value is 'mappingproxy({\'__module__\': \'pyarrow._compute\', \'__doc__\': \'\\n    Options for rounding temporal values.\\n\\n    Parameters\\n    ----------\\n    multiple : int, default 1\\n        Number of units to round to.\\n    unit : str, default "day"\\n        The unit in which `multiple` is expressed.\\n        Accepted values are "year", "quarter", "month", "week", "day",\\n        "hour", "minute", "second", "millisecond", "microsecond",\\n        "nanosecond".\\n    week_starts_monday : bool, default True\\n        If True, weeks start on Monday; if False, on Sunday.\\n    ceil_is_strictly_greater : bool, default False\\n        If True, ceil returns a rounded value that is strictly greater than the\\n        input. For example: ceiling 1970-01-01T00:00:00 to 3 hours would\\n        yield 1970-01-01T03:00:00 if set to True and 1970-01-01T00:00:00\\n        if set to False.\\n        This applies to the ceil_temporal function only.\\n    calendar_based_origin : bool, default False\\n        By default, the origin is 1970-01-01T00:00:00. By setting this to True,\\n        rounding origin will be beginning of one less precise calendar unit.\\n        E.g.: rounding to hours will use beginning of day as origin.\\n\\n        By default time is rounded to a multiple of units since\\n        1970-01-01T00:00:00. By setting calendar_based_origin to true,\\n        time will be rounded to number of units since the last greater\\n        calendar unit.\\n        For example: rounding to multiple of days since the beginning of the\\n        month or to hours since the beginning of the day.\\n        Exceptions: week and quarter are not used as greater units,\\n        therefore days will be rounded to the beginning of the month not\\n        week. Greater unit of week is a year.\\n        Note that ceiling and rounding might change sorting order of an array\\n        near greater unit change. For example rounding YYYY-mm-dd 23:00:00 to\\n        5 hours will ceil and round to YYYY-mm-dd+1 01:00:00 and floor to\\n        YYYY-mm-dd 20:00:00. On the other hand YYYY-mm-dd+1 00:00:00 will\\n        ceil, round and floor to YYYY-mm-dd+1 00:00:00. This can break the\\n        order of an already ordered array.\\n\\n    \', \'__init__\': <cyfunction RoundTemporalOptions.__init__ at 0x000001FC28B1A860>, \'__dict__\': <attribute \'__dict__\' of \'RoundTemporalOptions\' objects>})'


