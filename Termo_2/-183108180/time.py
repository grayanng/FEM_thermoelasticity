# encoding: utf-8
# module time
# from (built-in)
# by generator 1.147
"""
This module provides various functions to manipulate time values.

There are two standard representations of time.  One is the number
of seconds since the Epoch, in UTC (a.k.a. GMT).  It may be an integer
or a floating point number (to represent fractions of seconds).
The Epoch is system-defined; on Unix, it is generally January 1st, 1970.
The actual value can be retrieved by calling gmtime(0).

The other representation is a tuple of 9 integers giving local time.
The tuple items are:
  year (including century, e.g. 1998)
  month (1-12)
  day (1-31)
  hours (0-23)
  minutes (0-59)
  seconds (0-59)
  weekday (0-6, Monday is 0)
  Julian day (day in the year, 1-366)
  DST (Daylight Savings Time) flag (-1, 0 or 1)
If the DST flag is 0, the time is given in the regular time zone;
if it is 1, the time is given in the DST time zone;
if it is -1, mktime() should guess based on the date and time.
"""
# no imports

# Variables with simple values

altzone = -3600

daylight = 0

timezone = 0

_STRUCT_TM_ITEMS = 11

# functions

def asctime(p_tuple=None): # real signature unknown; restored from __doc__
    """
    asctime([tuple]) -> string
    
    Convert a time tuple to a string, e.g. 'Sat Jun 06 16:26:11 1998'.
    When the time tuple is not present, current time as returned by localtime()
    is used.
    """
    return ""

def ctime(seconds=None): # known case of time.ctime
    """
    ctime(seconds) -> string
    
    Convert a time in seconds since the Epoch to a string in local time.
    This is equivalent to asctime(localtime(seconds)). When the time tuple is
    not present, current time as returned by localtime() is used.
    """
    return ""

def get_clock_info(name): # real signature unknown; restored from __doc__
    """
    get_clock_info(name: str) -> dict
    
    Get information of the specified clock.
    """
    return {}

def gmtime(seconds=None): # real signature unknown; restored from __doc__
    """
    gmtime([seconds]) -> (tm_year, tm_mon, tm_mday, tm_hour, tm_min,
                           tm_sec, tm_wday, tm_yday, tm_isdst)
    
    Convert seconds since the Epoch to a time tuple expressing UTC (a.k.a.
    GMT).  When 'seconds' is not passed in, convert the current time instead.
    
    If the platform supports the tm_gmtoff and tm_zone, they are available as
    attributes only.
    """
    pass

def localtime(seconds=None): # real signature unknown; restored from __doc__
    """
    localtime([seconds]) -> (tm_year,tm_mon,tm_mday,tm_hour,tm_min,
                              tm_sec,tm_wday,tm_yday,tm_isdst)
    
    Convert seconds since the Epoch to a time tuple expressing local time.
    When 'seconds' is not passed in, convert the current time instead.
    """
    pass

def mktime(p_tuple): # real signature unknown; restored from __doc__
    """
    mktime(tuple) -> floating point number
    
    Convert a time tuple in local time to seconds since the Epoch.
    Note that mktime(gmtime(0)) will not generally return zero for most
    time zones; instead the returned value will either be equal to that
    of the timezone or altzone attributes on the time module.
    """
    return 0.0

def monotonic(): # real signature unknown; restored from __doc__
    """
    monotonic() -> float
    
    Monotonic clock, cannot go backward.
    """
    return 0.0

def monotonic_ns(): # real signature unknown; restored from __doc__
    """
    monotonic_ns() -> int
    
    Monotonic clock, cannot go backward, as nanoseconds.
    """
    return 0

def perf_counter(): # real signature unknown; restored from __doc__
    """
    perf_counter() -> float
    
    Performance counter for benchmarking.
    """
    return 0.0

def perf_counter_ns(): # real signature unknown; restored from __doc__
    """
    perf_counter_ns() -> int
    
    Performance counter for benchmarking as nanoseconds.
    """
    return 0

def process_time(): # real signature unknown; restored from __doc__
    """
    process_time() -> float
    
    Process time for profiling: sum of the kernel and user-space CPU time.
    """
    return 0.0

def process_time_ns(*args, **kwargs): # real signature unknown
    """
    process_time() -> int
    
    Process time for profiling as nanoseconds:
    sum of the kernel and user-space CPU time.
    """
    pass

def sleep(seconds): # real signature unknown; restored from __doc__
    """
    sleep(seconds)
    
    Delay execution for a given number of seconds.  The argument may be
    a floating point number for subsecond precision.
    """
    pass

def strftime(format, p_tuple=None): # real signature unknown; restored from __doc__
    """
    strftime(format[, tuple]) -> string
    
    Convert a time tuple to a string according to a format specification.
    See the library reference manual for formatting codes. When the time tuple
    is not present, current time as returned by localtime() is used.
    
    Commonly used format codes:
    
    %Y  Year with century as a decimal number.
    %m  Month as a decimal number [01,12].
    %d  Day of the month as a decimal number [01,31].
    %H  Hour (24-hour clock) as a decimal number [00,23].
    %M  Minute as a decimal number [00,59].
    %S  Second as a decimal number [00,61].
    %z  Time zone offset from UTC.
    %a  Locale's abbreviated weekday name.
    %A  Locale's full weekday name.
    %b  Locale's abbreviated month name.
    %B  Locale's full month name.
    %c  Locale's appropriate date and time representation.
    %I  Hour (12-hour clock) as a decimal number [01,12].
    %p  Locale's equivalent of either AM or PM.
    
    Other codes may be available on your platform.  See documentation for
    the C library strftime function.
    """
    return ""

def strptime(string, format): # real signature unknown; restored from __doc__
    """
    strptime(string, format) -> struct_time
    
    Parse a string to a time tuple according to a format specification.
    See the library reference manual for formatting codes (same as
    strftime()).
    
    Commonly used format codes:
    
    %Y  Year with century as a decimal number.
    %m  Month as a decimal number [01,12].
    %d  Day of the month as a decimal number [01,31].
    %H  Hour (24-hour clock) as a decimal number [00,23].
    %M  Minute as a decimal number [00,59].
    %S  Second as a decimal number [00,61].
    %z  Time zone offset from UTC.
    %a  Locale's abbreviated weekday name.
    %A  Locale's full weekday name.
    %b  Locale's abbreviated month name.
    %B  Locale's full month name.
    %c  Locale's appropriate date and time representation.
    %I  Hour (12-hour clock) as a decimal number [01,12].
    %p  Locale's equivalent of either AM or PM.
    
    Other codes may be available on your platform.  See documentation for
    the C library strftime function.
    """
    return struct_time

def thread_time(): # real signature unknown; restored from __doc__
    """
    thread_time() -> float
    
    Thread time for profiling: sum of the kernel and user-space CPU time.
    """
    return 0.0

def thread_time_ns(*args, **kwargs): # real signature unknown
    """
    thread_time() -> int
    
    Thread time for profiling as nanoseconds:
    sum of the kernel and user-space CPU time.
    """
    pass

def time(): # real signature unknown; restored from __doc__
    """
    time() -> floating point number
    
    Return the current time in seconds since the Epoch.
    Fractions of a second may be present if the system clock provides them.
    """
    return 0.0

def time_ns(): # real signature unknown; restored from __doc__
    """
    time_ns() -> int
    
    Return the current time in nanoseconds since the Epoch.
    """
    return 0

# classes

class struct_time(tuple):
    """
    The time value as returned by gmtime(), localtime(), and strptime(), and
     accepted by asctime(), mktime() and strftime().  May be considered as a
     sequence of 9 integers.
    
     Note that several fields' values are not the same as those defined by
     the C language standard for struct tm.  For example, the value of the
     field tm_year is the actual year, not year - 1900.  See individual
     fields' descriptions for details.
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    tm_gmtoff = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """offset from UTC in seconds"""

    tm_hour = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """hours, range [0, 23]"""

    tm_isdst = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """1 if summer time is in effect, 0 if not, and -1 if unknown"""

    tm_mday = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """day of month, range [1, 31]"""

    tm_min = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """minutes, range [0, 59]"""

    tm_mon = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """month of year, range [1, 12]"""

    tm_sec = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """seconds, range [0, 61])"""

    tm_wday = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """day of week, range [0, 6], Monday is 0"""

    tm_yday = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """day of year, range [1, 366]"""

    tm_year = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """year, for example, 1993"""

    tm_zone = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """abbreviation of timezone name"""


    n_fields = 11
    n_sequence_fields = 9
    n_unnamed_fields = 0


class __loader__(object):
    """
    Meta path import for built-in modules.
    
        All methods are either class or static methods to avoid the need to
        instantiate the class.
    """
    @classmethod
    def create_module(cls, *args, **kwargs): # real signature unknown
        """ Create a built-in module """
        pass

    @classmethod
    def exec_module(cls, *args, **kwargs): # real signature unknown
        """ Exec a built-in module """
        pass

    @classmethod
    def find_module(cls, *args, **kwargs): # real signature unknown
        """
        Find the built-in module.
        
                If 'path' is ever specified then the search is considered a failure.
        
                This method is deprecated.  Use find_spec() instead.
        """
        pass

    @classmethod
    def find_spec(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def get_code(cls, *args, **kwargs): # real signature unknown
        """ Return None as built-in modules do not have code objects. """
        pass

    @classmethod
    def get_source(cls, *args, **kwargs): # real signature unknown
        """ Return None as built-in modules do not have source code. """
        pass

    @classmethod
    def is_package(cls, *args, **kwargs): # real signature unknown
        """ Return False as built-in modules are never packages. """
        pass

    @classmethod
    def load_module(cls, *args, **kwargs): # real signature unknown
        """
        Load the specified module into sys.modules and return it.
        
            This method is deprecated.  Use loader.exec_module instead.
        """
        pass

    def module_repr(module): # reliably restored by inspect
        """
        Return repr for the module.
        
                The method is deprecated.  The import machinery does the job itself.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    _ORIGIN = 'built-in'
    __dict__ = None # (!) real value is "mappingproxy({'__module__': '_frozen_importlib', '__doc__': 'Meta path import for built-in modules.\\n\\n    All methods are either class or static methods to avoid the need to\\n    instantiate the class.\\n\\n    ', '_ORIGIN': 'built-in', 'module_repr': <staticmethod object at 0x000001AF9E9F6460>, 'find_spec': <classmethod object at 0x000001AF9E9F6490>, 'find_module': <classmethod object at 0x000001AF9E9F64C0>, 'create_module': <classmethod object at 0x000001AF9E9F64F0>, 'exec_module': <classmethod object at 0x000001AF9E9F6520>, 'get_code': <classmethod object at 0x000001AF9E9F65B0>, 'get_source': <classmethod object at 0x000001AF9E9F6640>, 'is_package': <classmethod object at 0x000001AF9E9F66D0>, 'load_module': <classmethod object at 0x000001AF9E9F6700>, '__dict__': <attribute '__dict__' of 'BuiltinImporter' objects>, '__weakref__': <attribute '__weakref__' of 'BuiltinImporter' objects>})"


# variables with complex values

tzname = (
    'Coordinated Universal Time',
    'Coordinated Universal Time',
)

__spec__ = None # (!) real value is "ModuleSpec(name='time', loader=<class '_frozen_importlib.BuiltinImporter'>, origin='built-in')"

