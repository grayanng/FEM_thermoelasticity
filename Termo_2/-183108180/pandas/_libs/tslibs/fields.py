# encoding: utf-8
# module pandas._libs.tslibs.fields
# from C:\Users\akharin\PycharmProjects\pythonProject\venv\lib\site-packages\pandas\_libs\tslibs\fields.cp39-win_amd64.pyd
# by generator 1.147
"""
Functions for accessing attributes of Timestamp/datetime64/datetime-like
objects and arrays
"""

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import numpy as np # C:\Users\akharin\PycharmProjects\pythonProject\venv\lib\site-packages\numpy\__init__.py

# Variables with simple values

LC_TIME = 5

# functions

def build_field_sarray(*args, **kwargs): # real signature unknown
    """ Datetime as int64 representation to a structured array of fields """
    pass

def build_isocalendar_sarray(*args, **kwargs): # real signature unknown
    """
    Given a int64-based datetime array, return the ISO 8601 year, week, and day
        as a structured array.
    """
    pass

def get_date_field(*args, **kwargs): # real signature unknown
    """
    Given a int64-based datetime index, extract the year, month, etc.,
        field and return an array of these values.
    """
    pass

def get_date_name_field(*args, **kwargs): # real signature unknown
    """
    Given a int64-based datetime index, return array of strings of date
        name based on requested field (e.g. day_name)
    """
    pass

def get_start_end_field(*args, **kwargs): # real signature unknown
    """
    Given an int64-based datetime index return array of indicators
        of whether timestamps are at the start/end of the month/quarter/year
        (defined by frequency).
    
        Parameters
        ----------
        dtindex : ndarray[int64]
        field : str
        frestr : str or None, default None
        month_kw : int, default 12
        reso : NPY_DATETIMEUNIT, default NPY_FR_ns
    
        Returns
        -------
        ndarray[bool]
    """
    pass

def get_timedelta_field(*args, **kwargs): # real signature unknown
    """
    Given a int64-based timedelta index, extract the days, hrs, sec.,
        field and return an array of these values.
    """
    pass

def isleapyear_arr(*args, **kwargs): # real signature unknown
    """ vectorized version of isleapyear; NaT evaluates as False """
    pass

def month_position_check(*args, **kwargs): # real signature unknown
    pass

def round_nsint64(*args, **kwargs): # real signature unknown
    """
    Applies rounding mode at given frequency
    
        Parameters
        ----------
        values : np.ndarray[int64_t]`
        mode : instance of `RoundTo` enumeration
        nanos : np.int64
            Freq to round to, expressed in nanoseconds
    
        Returns
        -------
        np.ndarray[int64_t]
    """
    pass

def set_locale(*args, **kwds): # reliably restored by inspect
    """
    Context manager for temporarily setting a locale.
    
        Parameters
        ----------
        new_locale : str or tuple
            A string of the form <language_country>.<encoding>. For example to set
            the current locale to US English with a UTF8 encoding, you would pass
            "en_US.UTF-8".
        lc_var : int, default `locale.LC_ALL`
            The category of the locale being set.
    
        Notes
        -----
        This is useful when you want to run a particular block of code under a
        particular locale, without globally setting the locale. This probably isn't
        thread-safe.
    """
    pass

def _get_locale_names(*args, **kwargs): # real signature unknown
    """
    Returns an array of localized day or month names.
    
        Parameters
        ----------
        name_type : str
            Attribute of LocaleTime() in which to return localized names.
        locale : str
    
        Returns
        -------
        list of locale names
    """
    pass

def __pyx_unpickle_Enum(*args, **kwargs): # real signature unknown
    pass

# classes

class LocaleTime(object):
    """
    Stores and handles locale-specific information related to time.
    
        ATTRIBUTES:
            f_weekday -- full weekday names (7-item list)
            a_weekday -- abbreviated weekday names (7-item list)
            f_month -- full month names (13-item list; dummy value in [0], which
                        is added by code)
            a_month -- abbreviated month names (13-item list, dummy value in
                        [0], which is added by code)
            am_pm -- AM/PM representation (2-item list)
            LC_date_time -- format string for date/time representation (string)
            LC_date -- format string for date representation (string)
            LC_time -- format string for time representation (string)
            timezone -- daylight- and non-daylight-savings timezone representation
                        (2-item list of sets)
            lang -- Language used by instance (2-item tuple)
    """
    def _LocaleTime__calc_am_pm(self): # reliably restored by inspect
        # no doc
        pass

    def _LocaleTime__calc_date_time(self): # reliably restored by inspect
        # no doc
        pass

    def _LocaleTime__calc_month(self): # reliably restored by inspect
        # no doc
        pass

    def _LocaleTime__calc_timezone(self): # reliably restored by inspect
        # no doc
        pass

    def _LocaleTime__calc_weekday(self): # reliably restored by inspect
        # no doc
        pass

    def __init__(self): # reliably restored by inspect
        """
        Set all attributes.
        
                Order of methods called matters for dependency reasons.
        
                The locale language is set at the offset and then checked again before
                exiting.  This is to make sure that the attributes were not set with a
                mix of information from more than one locale.  This would most likely
                happen when using threads where one thread calls a locale-dependent
                function while another thread changes the locale while the function in
                the other thread is still running.  Proper coding would call for
                locks to prevent changing the locale while locale-dependent code is
                running.  The check here is done in case someone does not think about
                doing this.
        
                Only other possible issue is if someone changed the timezone and did
                not call tz.tzset .  That is an issue for the programmer, though,
                since changing the timezone is worthless without that call.
        """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is "mappingproxy({'__module__': '_strptime', '__doc__': 'Stores and handles locale-specific information related to time.\\n\\n    ATTRIBUTES:\\n        f_weekday -- full weekday names (7-item list)\\n        a_weekday -- abbreviated weekday names (7-item list)\\n        f_month -- full month names (13-item list; dummy value in [0], which\\n                    is added by code)\\n        a_month -- abbreviated month names (13-item list, dummy value in\\n                    [0], which is added by code)\\n        am_pm -- AM/PM representation (2-item list)\\n        LC_date_time -- format string for date/time representation (string)\\n        LC_date -- format string for date representation (string)\\n        LC_time -- format string for time representation (string)\\n        timezone -- daylight- and non-daylight-savings timezone representation\\n                    (2-item list of sets)\\n        lang -- Language used by instance (2-item tuple)\\n    ', '__init__': <function LocaleTime.__init__ at 0x000001CAE4A8A1F0>, '_LocaleTime__calc_weekday': <function LocaleTime.__calc_weekday at 0x000001CAE4B118B0>, '_LocaleTime__calc_month': <function LocaleTime.__calc_month at 0x000001CAE4B11940>, '_LocaleTime__calc_am_pm': <function LocaleTime.__calc_am_pm at 0x000001CAE4B119D0>, '_LocaleTime__calc_date_time': <function LocaleTime.__calc_date_time at 0x000001CAE4B11A60>, '_LocaleTime__calc_timezone': <function LocaleTime.__calc_timezone at 0x000001CAE4B11AF0>, '__dict__': <attribute '__dict__' of 'LocaleTime' objects>, '__weakref__': <attribute '__weakref__' of 'LocaleTime' objects>})"


class RoundTo(object):
    """
    enumeration defining the available rounding modes
    
        Attributes
        ----------
        MINUS_INFTY
            round towards -∞, or floor [2]_
        PLUS_INFTY
            round towards +∞, or ceil [3]_
        NEAREST_HALF_EVEN
            round to nearest, tie-break half to even [6]_
        NEAREST_HALF_MINUS_INFTY
            round to nearest, tie-break half to -∞ [5]_
        NEAREST_HALF_PLUS_INFTY
            round to nearest, tie-break half to +∞ [4]_
    
    
        References
        ----------
        .. [1] "Rounding - Wikipedia"
               https://en.wikipedia.org/wiki/Rounding
        .. [2] "Rounding down"
               https://en.wikipedia.org/wiki/Rounding#Rounding_down
        .. [3] "Rounding up"
               https://en.wikipedia.org/wiki/Rounding#Rounding_up
        .. [4] "Round half up"
               https://en.wikipedia.org/wiki/Rounding#Round_half_up
        .. [5] "Round half down"
               https://en.wikipedia.org/wiki/Rounding#Round_half_down
        .. [6] "Round half to even"
               https://en.wikipedia.org/wiki/Rounding#Round_half_to_even
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    MINUS_INFTY = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    NEAREST_HALF_EVEN = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    NEAREST_HALF_MINUS_INFTY = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    NEAREST_HALF_PLUS_INFTY = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    PLUS_INFTY = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is 'mappingproxy({\'__module__\': \'pandas._libs.tslibs.fields\', \'__doc__\': \'\\n    enumeration defining the available rounding modes\\n\\n    Attributes\\n    ----------\\n    MINUS_INFTY\\n        round towards -?, or floor [2]_\\n    PLUS_INFTY\\n        round towards +?, or ceil [3]_\\n    NEAREST_HALF_EVEN\\n        round to nearest, tie-break half to even [6]_\\n    NEAREST_HALF_MINUS_INFTY\\n        round to nearest, tie-break half to -? [5]_\\n    NEAREST_HALF_PLUS_INFTY\\n        round to nearest, tie-break half to +? [4]_\\n\\n\\n    References\\n    ----------\\n    .. [1] "Rounding - Wikipedia"\\n           https://en.wikipedia.org/wiki/Rounding\\n    .. [2] "Rounding down"\\n           https://en.wikipedia.org/wiki/Rounding#Rounding_down\\n    .. [3] "Rounding up"\\n           https://en.wikipedia.org/wiki/Rounding#Rounding_up\\n    .. [4] "Round half up"\\n           https://en.wikipedia.org/wiki/Rounding#Round_half_up\\n    .. [5] "Round half down"\\n           https://en.wikipedia.org/wiki/Rounding#Round_half_down\\n    .. [6] "Round half to even"\\n           https://en.wikipedia.org/wiki/Rounding#Round_half_to_even\\n    \', \'MINUS_INFTY\': <property object at 0x000001CAE4B289A0>, \'PLUS_INFTY\': <property object at 0x000001CAE4B289F0>, \'NEAREST_HALF_EVEN\': <property object at 0x000001CAE4B28A40>, \'NEAREST_HALF_PLUS_INFTY\': <property object at 0x000001CAE4B28A90>, \'NEAREST_HALF_MINUS_INFTY\': <property object at 0x000001CAE4B28AE0>, \'__dict__\': <attribute \'__dict__\' of \'RoundTo\' objects>, \'__weakref__\': <attribute \'__weakref__\' of \'RoundTo\' objects>})'


# variables with complex values

DAYS_FULL = [
    'Monday',
    'Tuesday',
    'Wednesday',
    'Thursday',
    'Friday',
    'Saturday',
    'Sunday',
]

MONTHS_FULL = [
    '',
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December',
]

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x000001CAE42314F0>'

__spec__ = None # (!) real value is "ModuleSpec(name='pandas._libs.tslibs.fields', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x000001CAE42314F0>, origin='C:\\\\Users\\\\akharin\\\\PycharmProjects\\\\pythonProject\\\\venv\\\\lib\\\\site-packages\\\\pandas\\\\_libs\\\\tslibs\\\\fields.cp39-win_amd64.pyd')"

__test__ = {}

