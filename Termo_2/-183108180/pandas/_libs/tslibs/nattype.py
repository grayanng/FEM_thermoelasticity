# encoding: utf-8
# module pandas._libs.tslibs.nattype
# from C:\Users\akharin\PycharmProjects\pythonProject\venv\lib\site-packages\pandas\_libs\tslibs\nattype.cp39-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import warnings as warnings # C:\Users\akharin\AppData\Local\Programs\Python\Python39\lib\warnings.py
import numpy as np # C:\Users\akharin\PycharmProjects\pythonProject\venv\lib\site-packages\numpy\__init__.py
import datetime as __datetime


# Variables with simple values

iNaT = -9223372036854775808

# functions

def find_stack_level(): # reliably restored by inspect
    """
    Find the first place in the stack that is not inside pandas
        (tests notwithstanding).
    """
    pass

def _make_error_func(*args, **kwargs): # real signature unknown
    pass

def _make_nan_func(*args, **kwargs): # real signature unknown
    pass

def _make_nat_func(*args, **kwargs): # real signature unknown
    pass

def __nat_unpickle(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle__NaT(*args, **kwargs): # real signature unknown
    pass

# classes

class _NaT(__datetime.datetime):
    # no doc
    def isoformat(self, *args, **kwargs): # real signature unknown
        pass

    def to_datetime64(self, *args, **kwargs): # real signature unknown
        """ Return a numpy.datetime64 object with 'ns' precision. """
        pass

    def to_numpy(self): # real signature unknown; restored from __doc__
        """
        Convert the Timestamp to a NumPy datetime64 or timedelta64.
        
                .. versionadded:: 0.25.0
        
                With the default 'dtype', this is an alias method for `NaT.to_datetime64()`.
        
                The copy parameter is available here only for compatibility. Its value
                will not affect the return value.
        
                Returns
                -------
                numpy.datetime64 or numpy.timedelta64
        
                See Also
                --------
                DatetimeIndex.to_numpy : Similar method for DatetimeIndex.
        
                Examples
                --------
                >>> ts = pd.Timestamp('2020-03-14T15:32:52.192548651')
                >>> ts.to_numpy()
                numpy.datetime64('2020-03-14T15:32:52.192548651')
        
                Analogous for ``pd.NaT``:
        
                >>> pd.NaT.to_numpy()
                numpy.datetime64('NaT')
        
                >>> pd.NaT.to_numpy("m8[ns]")
                numpy.timedelta64('NaT','ns')
        """
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        """ Return self+value. """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __floordiv__(self, *args, **kwargs): # real signature unknown
        """ Return self//value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __hash__(self, *args, **kwargs): # real signature unknown
        """ Return hash(self). """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __mul__(self, *args, **kwargs): # real signature unknown
        """ Return self*value. """
        pass

    def __neg__(self, *args, **kwargs): # real signature unknown
        """ -self """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __pos__(self, *args, **kwargs): # real signature unknown
        """ +self """
        pass

    def __radd__(self, *args, **kwargs): # real signature unknown
        pass

    def __reduce_cython__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __rfloordiv__(self, *args, **kwargs): # real signature unknown
        """ Return value//self. """
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        """ Return value*self. """
        pass

    def __rsub__(self, *args, **kwargs): # real signature unknown
        pass

    def __rtruediv__(self, *args, **kwargs): # real signature unknown
        """ Return value/self. """
        pass

    def __setstate_cython__(self, *args, **kwargs): # real signature unknown
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    def __sub__(self, *args, **kwargs): # real signature unknown
        """ Return self-value. """
        pass

    def __truediv__(self, *args, **kwargs): # real signature unknown
        """ Return self/value. """
        pass

    asm8 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_leap_year = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_month_end = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_month_start = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_quarter_end = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_quarter_start = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_year_end = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_year_start = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __array_priority__ = 100


class NaTType(_NaT):
    """ (N)ot-(A)-(T)ime, the time equivalent of NaN. """
    def astimezone(self, tz=None): # real signature unknown; restored from __doc__
        """
        Convert timezone-aware Timestamp to another time zone.
        
                Parameters
                ----------
                tz : str, pytz.timezone, dateutil.tz.tzfile or None
                    Time zone for time which Timestamp will be converted to.
                    None will remove timezone holding UTC time.
        
                Returns
                -------
                converted : Timestamp
        
                Raises
                ------
                TypeError
                    If Timestamp is tz-naive.
        
                Examples
                --------
                Create a timestamp object with UTC timezone:
        
                >>> ts = pd.Timestamp('2020-03-14T15:32:52.192548651', tz='UTC')
                >>> ts
                Timestamp('2020-03-14 15:32:52.192548651+0000', tz='UTC')
        
                Change to Tokyo timezone:
        
                >>> ts.tz_convert(tz='Asia/Tokyo')
                Timestamp('2020-03-15 00:32:52.192548651+0900', tz='Asia/Tokyo')
        
                Can also use ``astimezone``:
        
                >>> ts.astimezone(tz='Asia/Tokyo')
                Timestamp('2020-03-15 00:32:52.192548651+0900', tz='Asia/Tokyo')
        
                Analogous for ``pd.NaT``:
        
                >>> pd.NaT.tz_convert(tz='Asia/Tokyo')
                NaT
        """
        pass

    def ceil(self, freq='H'): # real signature unknown; restored from __doc__
        """
        Return a new Timestamp ceiled to this resolution.
        
                Parameters
                ----------
                freq : str
                    Frequency string indicating the ceiling resolution.
                ambiguous : bool or {'raise', 'NaT'}, default 'raise'
                    The behavior is as follows:
        
                    * bool contains flags to determine if time is dst or not (note
                      that this flag is only applicable for ambiguous fall dst dates).
                    * 'NaT' will return NaT for an ambiguous time.
                    * 'raise' will raise an AmbiguousTimeError for an ambiguous time.
        
                nonexistent : {'raise', 'shift_forward', 'shift_backward, 'NaT', timedelta}, default 'raise'
                    A nonexistent time does not exist in a particular timezone
                    where clocks moved forward due to DST.
        
                    * 'shift_forward' will shift the nonexistent time forward to the
                      closest existing time.
                    * 'shift_backward' will shift the nonexistent time backward to the
                      closest existing time.
                    * 'NaT' will return NaT where there are nonexistent times.
                    * timedelta objects will shift nonexistent times by the timedelta.
                    * 'raise' will raise an NonExistentTimeError if there are
                      nonexistent times.
        
                Raises
                ------
                ValueError if the freq cannot be converted.
        
                Notes
                -----
                If the Timestamp has a timezone, ceiling will take place relative to the
                local ("wall") time and re-localized to the same timezone. When ceiling
                near daylight savings time, use ``nonexistent`` and ``ambiguous`` to
                control the re-localization behavior.
        
                Examples
                --------
                Create a timestamp object:
        
                >>> ts = pd.Timestamp('2020-03-14T15:32:52.192548651')
        
                A timestamp can be ceiled using multiple frequency units:
        
                >>> ts.ceil(freq='H') # hour
                Timestamp('2020-03-14 16:00:00')
        
                >>> ts.ceil(freq='T') # minute
                Timestamp('2020-03-14 15:33:00')
        
                >>> ts.ceil(freq='S') # seconds
                Timestamp('2020-03-14 15:32:53')
        
                >>> ts.ceil(freq='U') # microseconds
                Timestamp('2020-03-14 15:32:52.192549')
        
                ``freq`` can also be a multiple of a single unit, like '5T' (i.e.  5 minutes):
        
                >>> ts.ceil(freq='5T')
                Timestamp('2020-03-14 15:35:00')
        
                or a combination of multiple units, like '1H30T' (i.e. 1 hour and 30 minutes):
        
                >>> ts.ceil(freq='1H30T')
                Timestamp('2020-03-14 16:30:00')
        
                Analogous for ``pd.NaT``:
        
                >>> pd.NaT.ceil()
                NaT
        
                When rounding near a daylight savings time transition, use ``ambiguous`` or
                ``nonexistent`` to control how the timestamp should be re-localized.
        
                >>> ts_tz = pd.Timestamp("2021-10-31 01:30:00").tz_localize("Europe/Amsterdam")
        
                >>> ts_tz.ceil("H", ambiguous=False)
                Timestamp('2021-10-31 02:00:00+0100', tz='Europe/Amsterdam')
        
                >>> ts_tz.ceil("H", ambiguous=True)
                Timestamp('2021-10-31 02:00:00+0200', tz='Europe/Amsterdam')
        """
        pass

    def combine(self, date, time): # real signature unknown; restored from __doc__
        """
        Timestamp.combine(date, time)
        
                Combine date, time into datetime with same date and time fields.
        
                Examples
                --------
                >>> from datetime import date, time
                >>> pd.Timestamp.combine(date(2020, 3, 14), time(15, 30, 15))
                Timestamp('2020-03-14 15:30:15')
        """
        pass

    def ctime(self): # real signature unknown; restored from __doc__
        """ Return ctime() style string. """
        pass

    def date(self, *args, **kwargs): # real signature unknown
        """ Return date object with same year, month and day. """
        pass

    def day_name(self): # real signature unknown; restored from __doc__
        """
        Return the day name of the Timestamp with specified locale.
        
                Parameters
                ----------
                locale : str, default None (English locale)
                    Locale determining the language in which to return the day name.
        
                Returns
                -------
                str
        
                Examples
                --------
                >>> ts = pd.Timestamp('2020-03-14T15:32:52.192548651')
                >>> ts.day_name()
                'Saturday'
        
                Analogous for ``pd.NaT``:
        
                >>> pd.NaT.day_name()
                nan
        """
        pass

    def dst(self): # real signature unknown; restored from __doc__
        """ Return self.tzinfo.dst(self). """
        pass

    def floor(self, freq='H'): # real signature unknown; restored from __doc__
        """
        Return a new Timestamp floored to this resolution.
        
                Parameters
                ----------
                freq : str
                    Frequency string indicating the flooring resolution.
                ambiguous : bool or {'raise', 'NaT'}, default 'raise'
                    The behavior is as follows:
        
                    * bool contains flags to determine if time is dst or not (note
                      that this flag is only applicable for ambiguous fall dst dates).
                    * 'NaT' will return NaT for an ambiguous time.
                    * 'raise' will raise an AmbiguousTimeError for an ambiguous time.
        
                nonexistent : {'raise', 'shift_forward', 'shift_backward, 'NaT', timedelta}, default 'raise'
                    A nonexistent time does not exist in a particular timezone
                    where clocks moved forward due to DST.
        
                    * 'shift_forward' will shift the nonexistent time forward to the
                      closest existing time.
                    * 'shift_backward' will shift the nonexistent time backward to the
                      closest existing time.
                    * 'NaT' will return NaT where there are nonexistent times.
                    * timedelta objects will shift nonexistent times by the timedelta.
                    * 'raise' will raise an NonExistentTimeError if there are
                      nonexistent times.
        
                Raises
                ------
                ValueError if the freq cannot be converted.
        
                Notes
                -----
                If the Timestamp has a timezone, flooring will take place relative to the
                local ("wall") time and re-localized to the same timezone. When flooring
                near daylight savings time, use ``nonexistent`` and ``ambiguous`` to
                control the re-localization behavior.
        
                Examples
                --------
                Create a timestamp object:
        
                >>> ts = pd.Timestamp('2020-03-14T15:32:52.192548651')
        
                A timestamp can be floored using multiple frequency units:
        
                >>> ts.floor(freq='H') # hour
                Timestamp('2020-03-14 15:00:00')
        
                >>> ts.floor(freq='T') # minute
                Timestamp('2020-03-14 15:32:00')
        
                >>> ts.floor(freq='S') # seconds
                Timestamp('2020-03-14 15:32:52')
        
                >>> ts.floor(freq='N') # nanoseconds
                Timestamp('2020-03-14 15:32:52.192548651')
        
                ``freq`` can also be a multiple of a single unit, like '5T' (i.e.  5 minutes):
        
                >>> ts.floor(freq='5T')
                Timestamp('2020-03-14 15:30:00')
        
                or a combination of multiple units, like '1H30T' (i.e. 1 hour and 30 minutes):
        
                >>> ts.floor(freq='1H30T')
                Timestamp('2020-03-14 15:00:00')
        
                Analogous for ``pd.NaT``:
        
                >>> pd.NaT.floor()
                NaT
        
                When rounding near a daylight savings time transition, use ``ambiguous`` or
                ``nonexistent`` to control how the timestamp should be re-localized.
        
                >>> ts_tz = pd.Timestamp("2021-10-31 03:30:00").tz_localize("Europe/Amsterdam")
        
                >>> ts_tz.floor("2H", ambiguous=False)
                Timestamp('2021-10-31 02:00:00+0100', tz='Europe/Amsterdam')
        
                >>> ts_tz.floor("2H", ambiguous=True)
                Timestamp('2021-10-31 02:00:00+0200', tz='Europe/Amsterdam')
        """
        pass

    def fromisocalendar(self, *args, **kwargs): # real signature unknown
        """
        int, int, int -> Construct a date from the ISO year, week number and weekday.
        
        This is the inverse of the date.isocalendar() function
        """
        pass

    def fromordinal(self, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        Construct a timestamp from a a proleptic Gregorian ordinal.
        
                Parameters
                ----------
                ordinal : int
                    Date corresponding to a proleptic Gregorian ordinal.
                freq : str, DateOffset
                    Offset to apply to the Timestamp.
                tz : str, pytz.timezone, dateutil.tz.tzfile or None
                    Time zone for the Timestamp.
        
                Notes
                -----
                By definition there cannot be any tz info on the ordinal itself.
        
                Examples
                --------
                >>> pd.Timestamp.fromordinal(737425)
                Timestamp('2020-01-01 00:00:00')
        """
        pass

    def fromtimestamp(self, ts): # real signature unknown; restored from __doc__
        """
        Timestamp.fromtimestamp(ts)
        
                Transform timestamp[, tz] to tz's local time from POSIX timestamp.
        
                Examples
                --------
                >>> pd.Timestamp.fromtimestamp(1584199972)
                Timestamp('2020-03-14 15:32:52')
        
                Note that the output may change depending on your local time.
        """
        pass

    def isocalendar(self, *args, **kwargs): # real signature unknown
        """ Return a named tuple containing ISO year, week number, and weekday. """
        pass

    def isoweekday(self, *args, **kwargs): # real signature unknown
        """
        Return the day of the week represented by the date.
        
                Monday == 1 ... Sunday == 7.
        """
        pass

    def month_name(self): # real signature unknown; restored from __doc__
        """
        Return the month name of the Timestamp with specified locale.
        
                Parameters
                ----------
                locale : str, default None (English locale)
                    Locale determining the language in which to return the month name.
        
                Returns
                -------
                str
        
                Examples
                --------
                >>> ts = pd.Timestamp('2020-03-14T15:32:52.192548651')
                >>> ts.month_name()
                'March'
        
                Analogous for ``pd.NaT``:
        
                >>> pd.NaT.month_name()
                nan
        """
        pass

    def now(self): # real signature unknown; restored from __doc__
        """
        Return new Timestamp object representing current time local to tz.
        
                Parameters
                ----------
                tz : str or timezone object, default None
                    Timezone to localize to.
        
                Examples
                --------
                >>> pd.Timestamp.now()  # doctest: +SKIP
                Timestamp('2020-11-16 22:06:16.378782')
        
                Analogous for ``pd.NaT``:
        
                >>> pd.NaT.now()
                NaT
        """
        pass

    def replace(self, year=1999, hour=10): # real signature unknown; restored from __doc__
        """
        Implements datetime.replace, handles nanoseconds.
        
                Parameters
                ----------
                year : int, optional
                month : int, optional
                day : int, optional
                hour : int, optional
                minute : int, optional
                second : int, optional
                microsecond : int, optional
                nanosecond : int, optional
                tzinfo : tz-convertible, optional
                fold : int, optional
        
                Returns
                -------
                Timestamp with fields replaced
        
                Examples
                --------
                Create a timestamp object:
        
                >>> ts = pd.Timestamp('2020-03-14T15:32:52.192548651', tz='UTC')
                >>> ts
                Timestamp('2020-03-14 15:32:52.192548651+0000', tz='UTC')
        
                Replace year and the hour:
        
                >>> ts.replace(year=1999, hour=10)
                Timestamp('1999-03-14 10:32:52.192548651+0000', tz='UTC')
        
                Replace timezone (not a conversion):
        
                >>> import pytz
                >>> ts.replace(tzinfo=pytz.timezone('US/Pacific'))
                Timestamp('2020-03-14 15:32:52.192548651-0700', tz='US/Pacific')
        
                Analogous for ``pd.NaT``:
        
                >>> pd.NaT.replace(tzinfo=pytz.timezone('US/Pacific'))
                NaT
        """
        pass

    def round(self, freq='H'): # real signature unknown; restored from __doc__
        """
        Round the Timestamp to the specified resolution.
        
                Parameters
                ----------
                freq : str
                    Frequency string indicating the rounding resolution.
                ambiguous : bool or {'raise', 'NaT'}, default 'raise'
                    The behavior is as follows:
        
                    * bool contains flags to determine if time is dst or not (note
                      that this flag is only applicable for ambiguous fall dst dates).
                    * 'NaT' will return NaT for an ambiguous time.
                    * 'raise' will raise an AmbiguousTimeError for an ambiguous time.
        
                nonexistent : {'raise', 'shift_forward', 'shift_backward, 'NaT', timedelta}, default 'raise'
                    A nonexistent time does not exist in a particular timezone
                    where clocks moved forward due to DST.
        
                    * 'shift_forward' will shift the nonexistent time forward to the
                      closest existing time.
                    * 'shift_backward' will shift the nonexistent time backward to the
                      closest existing time.
                    * 'NaT' will return NaT where there are nonexistent times.
                    * timedelta objects will shift nonexistent times by the timedelta.
                    * 'raise' will raise an NonExistentTimeError if there are
                      nonexistent times.
        
                Returns
                -------
                a new Timestamp rounded to the given resolution of `freq`
        
                Raises
                ------
                ValueError if the freq cannot be converted
        
                Notes
                -----
                If the Timestamp has a timezone, rounding will take place relative to the
                local ("wall") time and re-localized to the same timezone. When rounding
                near daylight savings time, use ``nonexistent`` and ``ambiguous`` to
                control the re-localization behavior.
        
                Examples
                --------
                Create a timestamp object:
        
                >>> ts = pd.Timestamp('2020-03-14T15:32:52.192548651')
        
                A timestamp can be rounded using multiple frequency units:
        
                >>> ts.round(freq='H') # hour
                Timestamp('2020-03-14 16:00:00')
        
                >>> ts.round(freq='T') # minute
                Timestamp('2020-03-14 15:33:00')
        
                >>> ts.round(freq='S') # seconds
                Timestamp('2020-03-14 15:32:52')
        
                >>> ts.round(freq='L') # milliseconds
                Timestamp('2020-03-14 15:32:52.193000')
        
                ``freq`` can also be a multiple of a single unit, like '5T' (i.e.  5 minutes):
        
                >>> ts.round(freq='5T')
                Timestamp('2020-03-14 15:35:00')
        
                or a combination of multiple units, like '1H30T' (i.e. 1 hour and 30 minutes):
        
                >>> ts.round(freq='1H30T')
                Timestamp('2020-03-14 15:00:00')
        
                Analogous for ``pd.NaT``:
        
                >>> pd.NaT.round()
                NaT
        
                When rounding near a daylight savings time transition, use ``ambiguous`` or
                ``nonexistent`` to control how the timestamp should be re-localized.
        
                >>> ts_tz = pd.Timestamp("2021-10-31 01:30:00").tz_localize("Europe/Amsterdam")
        
                >>> ts_tz.round("H", ambiguous=False)
                Timestamp('2021-10-31 02:00:00+0100', tz='Europe/Amsterdam')
        
                >>> ts_tz.round("H", ambiguous=True)
                Timestamp('2021-10-31 02:00:00+0200', tz='Europe/Amsterdam')
        """
        pass

    def strftime(self, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        Return a formatted string of the Timestamp.
        
                Parameters
                ----------
                format : str
                    Format string to convert Timestamp to string.
                    See strftime documentation for more information on the format string:
                    https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior.
        
                Examples
                --------
                >>> ts = pd.Timestamp('2020-03-14T15:32:52.192548651')
                >>> ts.strftime('%Y-%m-%d %X')
                '2020-03-14 15:32:52'
        """
        pass

    def strptime(self, string, format): # real signature unknown; restored from __doc__
        """
        Timestamp.strptime(string, format)
        
                Function is not implemented. Use pd.to_datetime().
        """
        pass

    def time(self, *args, **kwargs): # real signature unknown
        """ Return time object with same time but with tzinfo=None. """
        pass

    def timestamp(self): # real signature unknown; restored from __doc__
        """
        Return POSIX timestamp as float.
        
                Examples
                --------
                >>> ts = pd.Timestamp('2020-03-14T15:32:52.192548')
                >>> ts.timestamp()
                1584199972.192548
        """
        pass

    def timetuple(self, *args, **kwargs): # real signature unknown
        """ Return time tuple, compatible with time.localtime(). """
        pass

    def timetz(self, *args, **kwargs): # real signature unknown
        """ Return time object with same time and tzinfo. """
        pass

    def today(self): # real signature unknown; restored from __doc__
        """
        Return the current time in the local timezone.
        
                This differs from datetime.today() in that it can be localized to a
                passed timezone.
        
                Parameters
                ----------
                tz : str or timezone object, default None
                    Timezone to localize to.
        
                Examples
                --------
                >>> pd.Timestamp.today()    # doctest: +SKIP
                Timestamp('2020-11-16 22:37:39.969883')
        
                Analogous for ``pd.NaT``:
        
                >>> pd.NaT.today()
                NaT
        """
        pass

    def toordinal(self, *args, **kwargs): # real signature unknown
        """ Return proleptic Gregorian ordinal.  January 1 of year 1 is day 1. """
        pass

    def total_seconds(self, *args, **kwargs): # real signature unknown
        """ Total seconds in the duration. """
        pass

    def to_pydatetime(self): # real signature unknown; restored from __doc__
        """
        Convert a Timestamp object to a native Python datetime object.
        
                If warn=True, issue a warning if nanoseconds is nonzero.
        
                Examples
                --------
                >>> ts = pd.Timestamp('2020-03-14T15:32:52.192548')
                >>> ts.to_pydatetime()
                datetime.datetime(2020, 3, 14, 15, 32, 52, 192548)
        
                Analogous for ``pd.NaT``:
        
                >>> pd.NaT.to_pydatetime()
                NaT
        """
        pass

    def tzname(self): # real signature unknown; restored from __doc__
        """ Return self.tzinfo.tzname(self). """
        pass

    def tz_convert(self, tz=None): # real signature unknown; restored from __doc__
        """
        Convert timezone-aware Timestamp to another time zone.
        
                Parameters
                ----------
                tz : str, pytz.timezone, dateutil.tz.tzfile or None
                    Time zone for time which Timestamp will be converted to.
                    None will remove timezone holding UTC time.
        
                Returns
                -------
                converted : Timestamp
        
                Raises
                ------
                TypeError
                    If Timestamp is tz-naive.
        
                Examples
                --------
                Create a timestamp object with UTC timezone:
        
                >>> ts = pd.Timestamp('2020-03-14T15:32:52.192548651', tz='UTC')
                >>> ts
                Timestamp('2020-03-14 15:32:52.192548651+0000', tz='UTC')
        
                Change to Tokyo timezone:
        
                >>> ts.tz_convert(tz='Asia/Tokyo')
                Timestamp('2020-03-15 00:32:52.192548651+0900', tz='Asia/Tokyo')
        
                Can also use ``astimezone``:
        
                >>> ts.astimezone(tz='Asia/Tokyo')
                Timestamp('2020-03-15 00:32:52.192548651+0900', tz='Asia/Tokyo')
        
                Analogous for ``pd.NaT``:
        
                >>> pd.NaT.tz_convert(tz='Asia/Tokyo')
                NaT
        """
        pass

    def tz_localize(self, tz=None): # real signature unknown; restored from __doc__
        """
        Localize the Timestamp to a timezone.
        
                Convert naive Timestamp to local time zone or remove
                timezone from timezone-aware Timestamp.
        
                Parameters
                ----------
                tz : str, pytz.timezone, dateutil.tz.tzfile or None
                    Time zone for time which Timestamp will be converted to.
                    None will remove timezone holding local time.
        
                ambiguous : bool, 'NaT', default 'raise'
                    When clocks moved backward due to DST, ambiguous times may arise.
                    For example in Central European Time (UTC+01), when going from
                    03:00 DST to 02:00 non-DST, 02:30:00 local time occurs both at
                    00:30:00 UTC and at 01:30:00 UTC. In such a situation, the
                    `ambiguous` parameter dictates how ambiguous times should be
                    handled.
        
                    The behavior is as follows:
        
                    * bool contains flags to determine if time is dst or not (note
                      that this flag is only applicable for ambiguous fall dst dates).
                    * 'NaT' will return NaT for an ambiguous time.
                    * 'raise' will raise an AmbiguousTimeError for an ambiguous time.
        
                nonexistent : 'shift_forward', 'shift_backward, 'NaT', timedelta, default 'raise'
                    A nonexistent time does not exist in a particular timezone
                    where clocks moved forward due to DST.
        
                    The behavior is as follows:
        
                    * 'shift_forward' will shift the nonexistent time forward to the
                      closest existing time.
                    * 'shift_backward' will shift the nonexistent time backward to the
                      closest existing time.
                    * 'NaT' will return NaT where there are nonexistent times.
                    * timedelta objects will shift nonexistent times by the timedelta.
                    * 'raise' will raise an NonExistentTimeError if there are
                      nonexistent times.
        
                Returns
                -------
                localized : Timestamp
        
                Raises
                ------
                TypeError
                    If the Timestamp is tz-aware and tz is not None.
        
                Examples
                --------
                Create a naive timestamp object:
        
                >>> ts = pd.Timestamp('2020-03-14T15:32:52.192548651')
                >>> ts
                Timestamp('2020-03-14 15:32:52.192548651')
        
                Add 'Europe/Stockholm' as timezone:
        
                >>> ts.tz_localize(tz='Europe/Stockholm')
                Timestamp('2020-03-14 15:32:52.192548651+0100', tz='Europe/Stockholm')
        
                Analogous for ``pd.NaT``:
        
                >>> pd.NaT.tz_localize()
                NaT
        """
        pass

    def utcfromtimestamp(self, ts): # real signature unknown; restored from __doc__
        """
        Timestamp.utcfromtimestamp(ts)
        
                Construct a naive UTC datetime from a POSIX timestamp.
        
                Examples
                --------
                >>> pd.Timestamp.utcfromtimestamp(1584199972)
                Timestamp('2020-03-14 15:32:52')
        """
        pass

    def utcnow(self): # real signature unknown; restored from __doc__
        """
        Timestamp.utcnow()
        
                Return a new Timestamp representing UTC day and time.
        
                Examples
                --------
                >>> pd.Timestamp.utcnow()   # doctest: +SKIP
                Timestamp('2020-11-16 22:50:18.092888+0000', tz='UTC')
        """
        pass

    def utcoffset(self): # real signature unknown; restored from __doc__
        """ Return self.tzinfo.utcoffset(self). """
        pass

    def utctimetuple(self, *args, **kwargs): # real signature unknown
        """ Return UTC time tuple, compatible with time.localtime(). """
        pass

    def weekday(self, *args, **kwargs): # real signature unknown
        """
        Return the day of the week represented by the date.
        
                Monday == 0 ... Sunday == 6.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        pass

    def __reduce_ex__(self, *args, **kwargs): # real signature unknown
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __rfloordiv__(self, *args, **kwargs): # real signature unknown
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        pass

    def __rtruediv__(self, *args, **kwargs): # real signature unknown
        pass

    day = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dayofweek = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dayofyear = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    days = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    daysinmonth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    days_in_month = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    day_of_week = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    day_of_year = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    freq = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    hour = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    microsecond = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    microseconds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    millisecond = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    minute = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    month = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    nanosecond = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    nanoseconds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    quarter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qyear = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    second = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    seconds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tz = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tzinfo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    week = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    weekofyear = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    year = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'pandas._libs.tslibs.nattype', '__doc__': '\\n    (N)ot-(A)-(T)ime, the time equivalent of NaN.\\n    ', '__new__': <cyfunction NaTType.__new__ at 0x000001734EF0E790>, 'freq': <property object at 0x000001734EF69360>, '__reduce_ex__': <cyfunction NaTType.__reduce_ex__ at 0x000001734EF0E930>, '__reduce__': <cyfunction NaTType.__reduce__ at 0x000001734EF0EA00>, '__rtruediv__': <cyfunction NaTType.__rtruediv__ at 0x000001734EF0EAD0>, '__rfloordiv__': <cyfunction NaTType.__rfloordiv__ at 0x000001734EF0EBA0>, '__rmul__': <cyfunction NaTType.__rmul__ at 0x000001734EF0EC70>, 'year': <property object at 0x000001734EF693B0>, 'quarter': <property object at 0x000001734EF69400>, 'month': <property object at 0x000001734EF69450>, 'day': <property object at 0x000001734EF694A0>, 'hour': <property object at 0x000001734EF694F0>, 'minute': <property object at 0x000001734EF69540>, 'second': <property object at 0x000001734EF69590>, 'millisecond': <property object at 0x000001734EF695E0>, 'microsecond': <property object at 0x000001734EF69630>, 'nanosecond': <property object at 0x000001734EF69680>, 'week': <property object at 0x000001734EF696D0>, 'dayofyear': <property object at 0x000001734EF69720>, 'day_of_year': <property object at 0x000001734EF69770>, 'weekofyear': <property object at 0x000001734EF697C0>, 'days_in_month': <property object at 0x000001734EF69810>, 'daysinmonth': <property object at 0x000001734EF69860>, 'dayofweek': <property object at 0x000001734EF698B0>, 'day_of_week': <property object at 0x000001734EF69900>, 'days': <property object at 0x000001734EF69950>, 'seconds': <property object at 0x000001734EF699A0>, 'microseconds': <property object at 0x000001734EF699F0>, 'nanoseconds': <property object at 0x000001734EF69A40>, 'qyear': <property object at 0x000001734EF69A90>, 'weekday': <cyfunction _make_nan_func.<locals>.f at 0x000001734EF6D110>, 'isoweekday': <cyfunction _make_nan_func.<locals>.f at 0x000001734EF6D1E0>, 'total_seconds': <cyfunction _make_nan_func.<locals>.f at 0x000001734EF6D2B0>, 'month_name': <cyfunction _make_nan_func.<locals>.f at 0x000001734EF6D380>, 'day_name': <cyfunction _make_nan_func.<locals>.f at 0x000001734EF6D450>, 'date': <cyfunction _make_nat_func.<locals>.f at 0x000001734EF6D520>, 'utctimetuple': <cyfunction _make_error_func.<locals>.f at 0x000001734EF6D5F0>, 'timetz': <cyfunction _make_error_func.<locals>.f at 0x000001734EF6D6C0>, 'timetuple': <cyfunction _make_error_func.<locals>.f at 0x000001734EF6D790>, 'isocalendar': <cyfunction _make_error_func.<locals>.f at 0x000001734EF6D860>, 'dst': <cyfunction _make_error_func.<locals>.f at 0x000001734EF6D930>, 'ctime': <cyfunction _make_error_func.<locals>.f at 0x000001734EF6DA00>, 'time': <cyfunction _make_error_func.<locals>.f at 0x000001734EF6DAD0>, 'toordinal': <cyfunction _make_error_func.<locals>.f at 0x000001734EF6DBA0>, 'tzname': <cyfunction _make_error_func.<locals>.f at 0x000001734EF6DC70>, 'utcoffset': <cyfunction _make_error_func.<locals>.f at 0x000001734EF6DD40>, 'fromisocalendar': <cyfunction _make_error_func.<locals>.f at 0x000001734EF6DE10>, 'strftime': <cyfunction _make_error_func.<locals>.f at 0x000001734EF6DEE0>, 'strptime': <cyfunction _make_error_func.<locals>.f at 0x000001734EF6E040>, 'utcfromtimestamp': <cyfunction _make_error_func.<locals>.f at 0x000001734EF6E110>, 'fromtimestamp': <cyfunction _make_error_func.<locals>.f at 0x000001734EF6E1E0>, 'combine': <cyfunction _make_error_func.<locals>.f at 0x000001734EF6E2B0>, 'utcnow': <cyfunction _make_error_func.<locals>.f at 0x000001734EF6E380>, 'timestamp': <cyfunction _make_error_func.<locals>.f at 0x000001734EF6E450>, 'astimezone': <cyfunction _make_error_func.<locals>.f at 0x000001734EF6E520>, 'fromordinal': <cyfunction _make_error_func.<locals>.f at 0x000001734EF6E5F0>, 'to_pydatetime': <cyfunction _make_nat_func.<locals>.f at 0x000001734EF6E6C0>, 'now': <cyfunction _make_nat_func.<locals>.f at 0x000001734EF6E790>, 'today': <cyfunction _make_nat_func.<locals>.f at 0x000001734EF6E860>, 'round': <cyfunction _make_nat_func.<locals>.f at 0x000001734EF6E930>, 'floor': <cyfunction _make_nat_func.<locals>.f at 0x000001734EF6EA00>, 'ceil': <cyfunction _make_nat_func.<locals>.f at 0x000001734EF6EAD0>, 'tz_convert': <cyfunction _make_nat_func.<locals>.f at 0x000001734EF6EBA0>, 'tz_localize': <cyfunction _make_nat_func.<locals>.f at 0x000001734EF6EC70>, 'replace': <cyfunction _make_nat_func.<locals>.f at 0x000001734EF6ED40>, 'tz': <property object at 0x000001734EF69BD0>, 'tzinfo': <property object at 0x000001734EF69C20>, '__dict__': <attribute '__dict__' of 'NaTType' objects>, '__weakref__': <attribute '__weakref__' of 'NaTType' objects>})"


# variables with complex values

NaT = None # (!) real value is 'NaT'

nat_strings = None # (!) real value is "{'nan', 'nat', 'NaN', 'NaT', 'NAT', 'NAN'}"

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x000001734EF61910>'

__pyx_capi__ = {
    'NPY_NAT': None, # (!) real value is '<capsule object "__pyx_t_5numpy_int64_t" at 0x000001734EF619F0>'
    'c_NaT': None, # (!) real value is '<capsule object "struct __pyx_obj_6pandas_5_libs_6tslibs_7nattype__NaT *" at 0x000001734EF61A50>'
    'c_nat_strings': None, # (!) real value is '<capsule object "PyObject *" at 0x000001734EF61A20>'
    'checknull_with_nat': None, # (!) real value is '<capsule object "int (PyObject *)" at 0x000001734EF61A80>'
    'is_dt64nat': None, # (!) real value is '<capsule object "int (PyObject *)" at 0x000001734EF61AB0>'
    'is_td64nat': None, # (!) real value is '<capsule object "int (PyObject *)" at 0x000001734EF61AE0>'
}

__spec__ = None # (!) real value is "ModuleSpec(name='pandas._libs.tslibs.nattype', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x000001734EF61910>, origin='C:\\\\Users\\\\akharin\\\\PycharmProjects\\\\pythonProject\\\\venv\\\\lib\\\\site-packages\\\\pandas\\\\_libs\\\\tslibs\\\\nattype.cp39-win_amd64.pyd')"

__test__ = {
    '_NaT.to_numpy (line 277)': '\n        Convert the Timestamp to a NumPy datetime64 or timedelta64.\n\n        .. versionadded:: 0.25.0\n\n        With the default \'dtype\', this is an alias method for `NaT.to_datetime64()`.\n\n        The copy parameter is available here only for compatibility. Its value\n        will not affect the return value.\n\n        Returns\n        -------\n        numpy.datetime64 or numpy.timedelta64\n\n        See Also\n        --------\n        DatetimeIndex.to_numpy : Similar method for DatetimeIndex.\n\n        Examples\n        --------\n        >>> ts = pd.Timestamp(\'2020-03-14T15:32:52.192548651\')\n        >>> ts.to_numpy()\n        numpy.datetime64(\'2020-03-14T15:32:52.192548651\')\n\n        Analogous for ``pd.NaT``:\n\n        >>> pd.NaT.to_numpy()\n        numpy.datetime64(\'NaT\')\n\n        >>> pd.NaT.to_numpy("m8[ns]")\n        numpy.timedelta64(\'NaT\',\'ns\')\n        ',
}

