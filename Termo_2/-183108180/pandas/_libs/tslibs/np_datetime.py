# encoding: utf-8
# module pandas._libs.tslibs.np_datetime
# from C:\Users\akharin\PycharmProjects\pythonProject\venv\lib\site-packages\pandas\_libs\tslibs\np_datetime.cp39-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import numpy as np # C:\Users\akharin\PycharmProjects\pythonProject\venv\lib\site-packages\numpy\__init__.py
import operator as operator # C:\Users\akharin\AppData\Local\Programs\Python\Python39\lib\operator.py

# functions

def astype_overflowsafe(*args, **kwargs): # real signature unknown
    """
    Convert an ndarray with datetime64[X] to datetime64[Y]
        or timedelta64[X] to timedelta64[Y],
        raising on overflow.
    """
    pass

def compare_mismatched_resolutions(*args, **kwargs): # real signature unknown
    """
    Overflow-safe comparison of timedelta64/datetime64 with mismatched resolutions.
    
        >>> left = np.array([500], dtype="M8[Y]")
        >>> right = np.array([0], dtype="M8[ns]")
        >>> left < right  # <- wrong!
        array([ True])
    """
    pass

def is_unitless(*args, **kwargs): # real signature unknown
    """ Check if a datetime64 or timedelta64 dtype has no attached unit. """
    pass

def py_get_unit_from_dtype(*args, **kwargs): # real signature unknown
    pass

def py_td64_to_tdstruct(*args, **kwargs): # real signature unknown
    pass

# classes

class OutOfBoundsDatetime(ValueError):
    """ Raised when the datetime is outside the range that can be represented. """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class OutOfBoundsTimedelta(ValueError):
    """
    Raised when encountering a timedelta value that cannot be represented.
    
        Representation should be within a timedelta64[ns].
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x0000020CFFD0CB50>'

__pyx_capi__ = {
    'astype_overflowsafe': None, # (!) real value is '<capsule object "PyArrayObject *(PyArrayObject *, PyArray_Descr *, int __pyx_skip_dispatch, struct __pyx_opt_args_6pandas_5_libs_6tslibs_11np_datetime_astype_overflowsafe *__pyx_optional_args)" at 0x0000020CFFD0CEA0>'
    'check_dts_bounds': None, # (!) real value is '<capsule object "PyObject *(npy_datetimestruct *, struct __pyx_opt_args_6pandas_5_libs_6tslibs_11np_datetime_check_dts_bounds *__pyx_optional_args)" at 0x0000020CFFD0CC90>'
    'cmp_dtstructs': None, # (!) real value is '<capsule object "int (npy_datetimestruct *, npy_datetimestruct *, int)" at 0x0000020CFFD0CF00>'
    'cmp_scalar': None, # (!) real value is '<capsule object "int (__pyx_t_5numpy_int64_t, __pyx_t_5numpy_int64_t, int)" at 0x0000020CFFD0CC60>'
    'convert_reso': None, # (!) real value is '<capsule object "__pyx_t_5numpy_int64_t (__pyx_t_5numpy_int64_t, NPY_DATETIMEUNIT, NPY_DATETIMEUNIT, int)" at 0x0000020CFFD0CF60>'
    'dtstruct_to_dt64': None, # (!) real value is '<capsule object "__pyx_t_5numpy_int64_t (npy_datetimestruct *)" at 0x0000020CFFD0CCC0>'
    'get_conversion_factor': None, # (!) real value is '<capsule object "__pyx_t_5numpy_int64_t (NPY_DATETIMEUNIT, NPY_DATETIMEUNIT)" at 0x0000020CFFD0CED0>'
    'get_datetime64_unit': None, # (!) real value is '<capsule object "NPY_DATETIMEUNIT (PyObject *)" at 0x0000020CFFD0CE10>'
    'get_datetime64_value': None, # (!) real value is '<capsule object "npy_datetime (PyObject *)" at 0x0000020CFFD0CDB0>'
    'get_implementation_bounds': None, # (!) real value is '<capsule object "PyObject *(NPY_DATETIMEUNIT, npy_datetimestruct *, npy_datetimestruct *)" at 0x0000020CFFD0CF30>'
    'get_timedelta64_value': None, # (!) real value is '<capsule object "npy_timedelta (PyObject *)" at 0x0000020CFFD0CDE0>'
    'get_unit_from_dtype': None, # (!) real value is '<capsule object "NPY_DATETIMEUNIT (PyArray_Descr *)" at 0x0000020CFFD0CE70>'
    'pydate_to_dt64': None, # (!) real value is '<capsule object "__pyx_t_5numpy_int64_t (PyDateTime_Date *, npy_datetimestruct *)" at 0x0000020CFFD0CD50>'
    'pydate_to_dtstruct': None, # (!) real value is '<capsule object "void (PyDateTime_Date *, npy_datetimestruct *)" at 0x0000020CFFD0CD80>'
    'pydatetime_to_dt64': None, # (!) real value is '<capsule object "__pyx_t_5numpy_int64_t (PyDateTime_DateTime *, npy_datetimestruct *)" at 0x0000020CFFD0CCF0>'
    'pydatetime_to_dtstruct': None, # (!) real value is '<capsule object "void (PyDateTime_DateTime *, npy_datetimestruct *)" at 0x0000020CFFD0CD20>'
    'string_to_dts': None, # (!) real value is '<capsule object "int (PyObject *, npy_datetimestruct *, NPY_DATETIMEUNIT *, int *, int *, int)" at 0x0000020CFFD0CE40>'
}

__spec__ = None # (!) real value is "ModuleSpec(name='pandas._libs.tslibs.np_datetime', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x0000020CFFD0CB50>, origin='C:\\\\Users\\\\akharin\\\\PycharmProjects\\\\pythonProject\\\\venv\\\\lib\\\\site-packages\\\\pandas\\\\_libs\\\\tslibs\\\\np_datetime.cp39-win_amd64.pyd')"

__test__ = {
    'compare_mismatched_resolutions (line 392)': '\n    Overflow-safe comparison of timedelta64/datetime64 with mismatched resolutions.\n\n    >>> left = np.array([500], dtype="M8[Y]")\n    >>> right = np.array([0], dtype="M8[ns]")\n    >>> left < right  # <- wrong!\n    array([ True])\n    ',
}

