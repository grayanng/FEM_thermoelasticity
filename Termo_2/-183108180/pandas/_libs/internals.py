# encoding: utf-8
# module pandas._libs.internals
# from C:\Users\akharin\PycharmProjects\pythonProject\venv\lib\site-packages\pandas\_libs\internals.cp39-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import weakref as weakref # C:\Users\akharin\AppData\Local\Programs\Python\Python39\lib\weakref.py
import numpy as np # C:\Users\akharin\PycharmProjects\pythonProject\venv\lib\site-packages\numpy\__init__.py
from pandas._libs.algos import ensure_int64


# functions

def get_blkno_indexers(*args, **kwargs): # real signature unknown
    """
    Enumerate contiguous runs of integers in ndarray.
    
        Iterate over elements of `blknos` yielding ``(blkno, slice(start, stop))``
        pairs for each contiguous run found.
    
        If `group` is True and there is more than one run for a certain blkno,
        ``(blkno, array)`` with an array containing positions of all elements equal
        to blkno.
    
        Returns
        -------
        list[tuple[int, slice | np.ndarray]]
    """
    pass

def get_blkno_placements(*args, **kwargs): # real signature unknown
    """
    Parameters
        ----------
        blknos : np.ndarray[int64]
        group : bool, default True
    
        Returns
        -------
        iterator
            yield (blkno, BlockPlacement)
    """
    pass

def slice_len(*args, **kwargs): # real signature unknown
    """
    Get length of a bounded slice.
    
        The slice must not have any "open" bounds that would create dependency on
        container size, i.e.:
        - if ``s.step is None or s.step > 0``, ``s.stop`` is not ``None``
        - if ``s.step < 0``, ``s.start`` is not ``None``
    
        Otherwise, the result is unreliable.
    """
    pass

def update_blklocs_and_blknos(*args, **kwargs): # real signature unknown
    """ Update blklocs and blknos when a new column is inserted at 'loc'. """
    pass

def _unpickle_block(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_Enum(*args, **kwargs): # real signature unknown
    pass

# classes

class SharedBlock(object):
    """ Defining __init__ in a cython class significantly improves performance. """
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

    ndim = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _mgr_locs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001AC6EEB1D20>'


class Block(SharedBlock):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    values = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001AC6EEB1E40>'


class BlockManager(object):
    # no doc
    def get_slice(self, *args, **kwargs): # real signature unknown
        pass

    def _post_setstate(self, *args, **kwargs): # real signature unknown
        pass

    def _rebuild_blknos_and_blklocs(self, *args, **kwargs): # real signature unknown
        """ Update mgr._blknos / mgr._blklocs. """
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

    axes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    blocks = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    refs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _blklocs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _blknos = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _is_consolidated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _known_consolidated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001AC6EEB1EA0>'


class BlockPlacement(object):
    # no doc
    def add(self, *args, **kwargs): # real signature unknown
        pass

    def append(self, *args, **kwargs): # real signature unknown
        pass

    def delete(self, *args, **kwargs): # real signature unknown
        pass

    def increment_above(self, *args, **kwargs): # real signature unknown
        """ Increment any entries of 'loc' or above by one. """
        pass

    def tile_for_unstack(self, *args, **kwargs): # real signature unknown
        """ Find the new mgr_locs for the un-stacked version of a Block. """
        pass

    def __getitem__(self, *args, **kwargs): # real signature unknown
        """ Return self[key]. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __iter__(self, *args, **kwargs): # real signature unknown
        """ Implement iter(self). """
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
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

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    as_array = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    as_slice = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    indexer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_slice_like = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001AC6EEB1CC0>'


class defaultdict(dict):
    """
    defaultdict(default_factory=None, /, [...]) --> dict with default factory
    
    The default factory is called without arguments to produce
    a new value when a key is not present, in __getitem__ only.
    A defaultdict compares equal to a dict with the same items.
    All remaining arguments are treated the same as if they were
    passed to the dict constructor, including keyword arguments.
    """
    def copy(self): # real signature unknown; restored from __doc__
        """ D.copy() -> a shallow copy of D. """
        pass

    @classmethod
    def __class_getitem__(cls, *args, **kwargs): # real signature unknown
        """ See PEP 585 """
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        """ D.copy() -> a shallow copy of D. """
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __init__(self, default_factory=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    def __missing__(self, key): # real signature unknown; restored from __doc__
        """
        __missing__(key) # Called by __getitem__ for missing key; pseudo-code:
          if self.default_factory is None: raise KeyError((key,))
          self[key] = value = self.default_factory()
          return value
        """
        pass

    def __or__(self, *args, **kwargs): # real signature unknown
        """ Return self|value. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ Return state information for pickling. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __ror__(self, *args, **kwargs): # real signature unknown
        """ Return value|self. """
        pass

    default_factory = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Factory for default value called by __missing__()."""



class NDArrayBackedBlock(SharedBlock):
    """ Block backed by NDArrayBackedExtensionArray """
    def getitem_block_index(self, *args, **kwargs): # real signature unknown
        """
        Perform __getitem__-like specialized to slicing along index.
        
                Assumes self.ndim == 2
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    values = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001AC6EEB1DE0>'


class NumpyBlock(SharedBlock):
    # no doc
    def getitem_block_index(self, *args, **kwargs): # real signature unknown
        """
        Perform __getitem__-like specialized to slicing along index.
        
                Assumes self.ndim == 2
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    values = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001AC6EEB1D80>'


# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x000001AC6EEB16A0>'

__spec__ = None # (!) real value is "ModuleSpec(name='pandas._libs.internals', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x000001AC6EEB16A0>, origin='C:\\\\Users\\\\akharin\\\\PycharmProjects\\\\pythonProject\\\\venv\\\\lib\\\\site-packages\\\\pandas\\\\_libs\\\\internals.cp39-win_amd64.pyd')"

__test__ = {}

