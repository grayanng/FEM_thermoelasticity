# encoding: utf-8
# module pandas._libs.index
# from C:\Users\akharin\PycharmProjects\pythonProject\venv\lib\site-packages\pandas\_libs\index.cp39-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import numpy as np # C:\Users\akharin\PycharmProjects\pythonProject\venv\lib\site-packages\numpy\__init__.py
import pandas._libs.algos as algos # C:\Users\akharin\PycharmProjects\pythonProject\venv\lib\site-packages\pandas\_libs\algos.cp39-win_amd64.pyd
import pandas._libs.hashtable as _hash # C:\Users\akharin\PycharmProjects\pythonProject\venv\lib\site-packages\pandas\_libs\hashtable.cp39-win_amd64.pyd

# Variables with simple values

_SIZE_CUTOFF = 1000000

# functions

def __pyx_unpickle_BaseMultiIndexCodesEngine(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_BoolEngine(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_Complex128Engine(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_Complex64Engine(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_DatetimeEngine(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_Enum(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_ExtensionEngine(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_Float32Engine(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_Float64Engine(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_IndexEngine(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_Int16Engine(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_Int32Engine(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_Int64Engine(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_Int8Engine(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_ObjectEngine(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_PeriodEngine(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_SharedEngine(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_TimedeltaEngine(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_UInt16Engine(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_UInt32Engine(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_UInt64Engine(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_UInt8Engine(*args, **kwargs): # real signature unknown
    pass

# classes

class BaseMultiIndexCodesEngine(object):
    """
    Base class for MultiIndexUIntEngine and MultiIndexPyIntEngine, which
        represent each label in a MultiIndex as an integer, by juxtaposing the bits
        encoding each level, with appropriate offsets.
    
        For instance: if 3 levels have respectively 3, 6 and 1 possible values,
        then their labels can be represented using respectively 2, 3 and 1 bits,
        as follows:
         _ _ _ _____ _ __ __ __
        |0|0|0| ... |0| 0|a1|a0| -> offset 0 (first level)
         — — — ————— — —— —— ——
        |0|0|0| ... |0|b2|b1|b0| -> offset 2 (bits required for first level)
         — — — ————— — —— —— ——
        |0|0|0| ... |0| 0| 0|c0| -> offset 5 (bits required for first two levels)
         ‾ ‾ ‾ ‾‾‾‾‾ ‾ ‾‾ ‾‾ ‾‾
        and the resulting unsigned integer representation will be:
         _ _ _ _____ _ __ __ __ __ __ __
        |0|0|0| ... |0|c0|b2|b1|b0|a1|a0|
         ‾ ‾ ‾ ‾‾‾‾‾ ‾ ‾‾ ‾‾ ‾‾ ‾‾ ‾‾ ‾‾
    
        Offsets are calculated at initialization, labels are transformed by method
        _codes_to_ints.
    
        Keys are located by first locating each component against the respective
        level, then locating (the integer representation of) codes.
    """
    def get_indexer(self, *args, **kwargs): # real signature unknown
        """
        Returns an array giving the positions of each value of `target` in
                `self.values`, where -1 represents a value in `target` which does not
                appear in `self.values`
        
                Parameters
                ----------
                target : np.ndarray
        
                Returns
                -------
                np.ndarray[intp_t, ndim=1] of the indexer of `target` into
                `self.values`
        """
        pass

    def get_indexer_non_unique(self, *args, **kwargs): # real signature unknown
        pass

    def get_indexer_with_fill(self, *args, **kwargs): # real signature unknown
        """
        Returns an array giving the positions of each value of `target` in
                `values`, where -1 represents a value in `target` which does not
                appear in `values`
        
                If `method` is "backfill" then the position for a value in `target`
                which does not appear in `values` is that of the next greater value
                in `values` (if one exists), and -1 if there is no such value.
        
                Similarly, if the method is "pad" then the position for a value in
                `target` which does not appear in `values` is that of the next smaller
                value in `values` (if one exists), and -1 if there is no such value.
        
                Parameters
                ----------
                target: ndarray[object] of tuples
                    need not be sorted, but all must have the same length, which must be
                    the same as the length of all tuples in `values`
                values : ndarray[object] of tuples
                    must be sorted and all have the same length.  Should be the set of
                    the MultiIndex's values.
                method: string
                    "backfill" or "pad"
                limit: int or None
                    if provided, limit the number of fills to this value
        
                Returns
                -------
                np.ndarray[intp_t, ndim=1] of the indexer of `target` into `values`,
                filled with the `method` (and optionally `limit`) specified
        """
        pass

    def get_loc(self, *args, **kwargs): # real signature unknown
        pass

    def _codes_to_ints(self, *args, **kwargs): # real signature unknown
        pass

    def _extract_level_codes(self, *args, **kwargs): # real signature unknown
        """
        Map the requested list of (tuple) keys to their integer representations
                for searching in the underlying integer index.
        
                Parameters
                ----------
                target : MultiIndex
        
                Returns
                ------
                int_keys : 1-dimensional array of dtype uint64 or object
                    Integers representing one combination each
        """
        pass

    def __contains__(self, *args, **kwargs): # real signature unknown
        """ Return key in self. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        """
        Parameters
                ----------
                levels : list-like of numpy arrays
                    Levels of the MultiIndex.
                labels : list-like of numpy arrays of integer dtype
                    Labels of the MultiIndex.
                offsets : numpy array of uint64 dtype
                    Pre-calculated offsets, one for each level of the index.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass


class IndexEngine(object):
    # no doc
    def clear_mapping(self, *args, **kwargs): # real signature unknown
        pass

    def get_indexer(self, *args, **kwargs): # real signature unknown
        pass

    def get_indexer_non_unique(self, *args, **kwargs): # real signature unknown
        """
        Return an indexer suitable for taking from a non unique index
                return the labels in the same order as the target
                and a missing indexer into the targets (which correspond
                to the -1 indices in the results
        
                Returns
                -------
                indexer : np.ndarray[np.intp]
                missing : np.ndarray[np.intp]
        """
        pass

    def get_loc(self, *args, **kwargs): # real signature unknown
        pass

    def sizeof(self, *args, **kwargs): # real signature unknown
        """ return the sizeof our mapping """
        pass

    def __contains__(self, *args, **kwargs): # real signature unknown
        """ Return key in self. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    def __sizeof__(self, *args, **kwargs): # real signature unknown
        pass

    is_mapping_populated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_monotonic_decreasing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_monotonic_increasing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_unique = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    mapping = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    over_size_threshold = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    values = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001CB1FD84090>'


class UInt8Engine(IndexEngine):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001CB1FD84600>'


class BoolEngine(UInt8Engine):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001CB1FD84720>'


class Complex128Engine(IndexEngine):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001CB1FD846C0>'


class Complex64Engine(IndexEngine):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001CB1FD84660>'


class Int64Engine(IndexEngine):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001CB1FD84150>'


class DatetimeEngine(Int64Engine):
    # no doc
    def get_loc(self, *args, **kwargs): # real signature unknown
        pass

    def __contains__(self, *args, **kwargs): # real signature unknown
        """ Return key in self. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001CB1FD841B0>'


class ExtensionEngine(SharedEngine):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001CB1FD847E0>'


class Float32Engine(IndexEngine):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001CB1FD84360>'


class Float64Engine(IndexEngine):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001CB1FD84300>'


class Int16Engine(IndexEngine):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001CB1FD84420>'


class Int32Engine(IndexEngine):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001CB1FD843C0>'


class Int8Engine(IndexEngine):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001CB1FD84480>'


class ObjectEngine(IndexEngine):
    """ Index Engine for use with object-dtype Index, namely the base class Index. """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001CB1FD840F0>'


class PeriodEngine(Int64Engine):
    # no doc
    def get_loc(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001CB1FD84270>'


class TimedeltaEngine(DatetimeEngine):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001CB1FD84210>'


class UInt16Engine(IndexEngine):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001CB1FD845A0>'


class UInt32Engine(IndexEngine):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001CB1FD84540>'


class UInt64Engine(IndexEngine):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001CB1FD844E0>'


# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x000001CB1FD7BC40>'

__spec__ = None # (!) real value is "ModuleSpec(name='pandas._libs.index', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x000001CB1FD7BC40>, origin='C:\\\\Users\\\\akharin\\\\PycharmProjects\\\\pythonProject\\\\venv\\\\lib\\\\site-packages\\\\pandas\\\\_libs\\\\index.cp39-win_amd64.pyd')"

__test__ = {}

