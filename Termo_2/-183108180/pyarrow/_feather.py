# encoding: utf-8
# module pyarrow._feather
# from C:\Users\akharin\PycharmProjects\pythonProject\venv\lib\site-packages\pyarrow\_feather.cp39-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
from pyarrow.lib import tobytes

import pyarrow.lib as __pyarrow_lib


# functions

def write_feather(Table_table, dest, compression=None, compression_level=None, chunksize=None, version=2): # real signature unknown; restored from __doc__
    """ write_feather(Table table, dest, compression=None, compression_level=None, chunksize=None, version=2) """
    pass

# classes

class FeatherError(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class FeatherReader(__pyarrow_lib._Weakrefable):
    # no doc
    def read(self): # real signature unknown; restored from __doc__
        """ FeatherReader.read(self) """
        pass

    def read_indices(self, indices): # real signature unknown; restored from __doc__
        """ FeatherReader.read_indices(self, indices) """
        pass

    def read_names(self, names): # real signature unknown; restored from __doc__
        """ FeatherReader.read_names(self, names) """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ FeatherReader.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ FeatherReader.__setstate_cython__(self, __pyx_state) """
        pass

    version = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x000002707FD9A910>'

__spec__ = None # (!) real value is "ModuleSpec(name='pyarrow._feather', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x000002707FD9A910>, origin='C:\\\\Users\\\\akharin\\\\PycharmProjects\\\\pythonProject\\\\venv\\\\lib\\\\site-packages\\\\pyarrow\\\\_feather.cp39-win_amd64.pyd')"

__test__ = {}

