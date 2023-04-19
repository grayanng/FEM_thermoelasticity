# encoding: utf-8
# module pandas._libs.hashtable
# from C:\Users\akharin\PycharmProjects\pythonProject\venv\lib\site-packages\pandas\_libs\hashtable.cp39-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import numpy as np # C:\Users\akharin\PycharmProjects\pythonProject\venv\lib\site-packages\numpy\__init__.py

# Variables with simple values

SIZE_HINT_LIMIT = 1048583

# functions

def duplicated(*args, **kwargs): # real signature unknown
    pass

def get_hashtable_trace_domain(*args, **kwargs): # real signature unknown
    pass

def ismember(*args, **kwargs): # real signature unknown
    pass

def mode(*args, **kwargs): # real signature unknown
    pass

def objects_are_equal(*args, **kwargs): # real signature unknown
    pass

def object_hash(*args, **kwargs): # real signature unknown
    pass

def unique_label_indices(*args, **kwargs): # real signature unknown
    """
    Indices of the first occurrences of the unique labels
        *excluding* -1. equivalent to:
            np.unique(labels, return_index=True)[1]
    """
    pass

def value_count(*args, **kwargs): # real signature unknown
    pass

def _unique_label_indices_int32(*args, **kwargs): # real signature unknown
    """
    Indices of the first occurrences of the unique labels
        *excluding* -1. equivalent to:
            np.unique(labels, return_index=True)[1]
    """
    pass

def _unique_label_indices_int64(*args, **kwargs): # real signature unknown
    """
    Indices of the first occurrences of the unique labels
        *excluding* -1. equivalent to:
            np.unique(labels, return_index=True)[1]
    """
    pass

def __pyx_unpickle_Enum(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_HashTable(*args, **kwargs): # real signature unknown
    pass

# classes

from .HashTable import HashTable
from .Complex128HashTable import Complex128HashTable
from .Vector import Vector
from .Complex128Vector import Complex128Vector
from .Complex64HashTable import Complex64HashTable
from .Complex64Vector import Complex64Vector
from .Factorizer import Factorizer
from .Float32HashTable import Float32HashTable
from .Float32Vector import Float32Vector
from .Float64HashTable import Float64HashTable
from .Float64Vector import Float64Vector
from .Int16HashTable import Int16HashTable
from .Int16Vector import Int16Vector
from .Int32HashTable import Int32HashTable
from .Int32Vector import Int32Vector
from .Int64Factorizer import Int64Factorizer
from .IntpHashTable import IntpHashTable
from .Int64HashTable import Int64HashTable
from .Int64Vector import Int64Vector
from .Int8HashTable import Int8HashTable
from .Int8Vector import Int8Vector
from .ObjectFactorizer import ObjectFactorizer
from .ObjectVector import ObjectVector
from .PyObjectHashTable import PyObjectHashTable
from .StringHashTable import StringHashTable
from .StringVector import StringVector
from .UInt16HashTable import UInt16HashTable
from .UInt16Vector import UInt16Vector
from .UInt32HashTable import UInt32HashTable
from .UInt32Vector import UInt32Vector
from .UInt64HashTable import UInt64HashTable
from .UInt64Vector import UInt64Vector
from .UInt8HashTable import UInt8HashTable
from .UInt8Vector import UInt8Vector
# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x000001FEFEDDCA00>'

__spec__ = None # (!) real value is "ModuleSpec(name='pandas._libs.hashtable', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x000001FEFEDDCA00>, origin='C:\\\\Users\\\\akharin\\\\PycharmProjects\\\\pythonProject\\\\venv\\\\lib\\\\site-packages\\\\pandas\\\\_libs\\\\hashtable.cp39-win_amd64.pyd')"

__test__ = {
    'Int64Factorizer.factorize (line 148)': '\n        Returns\n        -------\n        ndarray[intp_t]\n\n        Examples\n        --------\n        Factorize values with nans replaced by na_sentinel\n\n        >>> fac = Int64Factorizer(3)\n        >>> fac.factorize(np.array([1,2,3]), na_sentinel=20)\n        array([0, 1, 2])\n        ',
    'ObjectFactorizer.factorize (line 101)': "\n\n        Returns\n        -------\n        np.ndarray[np.intp]\n\n        Examples\n        --------\n        Factorize values with nans replaced by na_sentinel\n\n        >>> fac = ObjectFactorizer(3)\n        >>> fac.factorize(np.array([1,2,np.nan], dtype='O'), na_sentinel=20)\n        array([ 0,  1, 20])\n        ",
}

