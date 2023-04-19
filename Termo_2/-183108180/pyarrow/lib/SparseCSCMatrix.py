# encoding: utf-8
# module pyarrow.lib
# from C:\Users\akharin\PycharmProjects\pythonProject\venv\lib\site-packages\pyarrow\lib.cp39-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import datetime as datetime # C:\Users\akharin\AppData\Local\Programs\Python\Python39\lib\datetime.py
import decimal as _pydecimal # C:\Users\akharin\AppData\Local\Programs\Python\Python39\lib\decimal.py
import numpy as np # C:\Users\akharin\PycharmProjects\pythonProject\venv\lib\site-packages\numpy\__init__.py
import os as os # C:\Users\akharin\AppData\Local\Programs\Python\Python39\lib\os.py
import sys as sys # <module 'sys' (built-in)>
import pickle as builtin_pickle # C:\Users\akharin\AppData\Local\Programs\Python\Python39\lib\pickle.py
import pickle as pickle # C:\Users\akharin\AppData\Local\Programs\Python\Python39\lib\pickle.py
import signal as signal # C:\Users\akharin\AppData\Local\Programs\Python\Python39\lib\signal.py
import threading as threading # C:\Users\akharin\AppData\Local\Programs\Python\Python39\lib\threading.py
import warnings as warnings # C:\Users\akharin\AppData\Local\Programs\Python\Python39\lib\warnings.py
import atexit as atexit # <module 'atexit' (built-in)>
import re as re # C:\Users\akharin\AppData\Local\Programs\Python\Python39\lib\re.py
import collections as collections # C:\Users\akharin\AppData\Local\Programs\Python\Python39\lib\collections\__init__.py
import codecs as codecs # C:\Users\akharin\AppData\Local\Programs\Python\Python39\lib\codecs.py
import time as time # <module 'time' (built-in)>
from _queue import QueueEmpty

import collections.abc as __collections_abc
import enum as __enum
import importlib._bootstrap as __importlib__bootstrap
import io as __io
import _io as ___io


from ._Weakrefable import _Weakrefable

class SparseCSCMatrix(_Weakrefable):
    """
    SparseCSCMatrix()
    
        A sparse CSC matrix.
    """
    def dim_name(self, i): # real signature unknown; restored from __doc__
        """ SparseCSCMatrix.dim_name(self, i) """
        pass

    def equals(self, SparseCSCMatrix_other): # real signature unknown; restored from __doc__
        """
        SparseCSCMatrix.equals(self, SparseCSCMatrix other)
        
                Return true if sparse tensors contains exactly equal data
        
                Parameters
                ----------
                other : SparseCSCMatrix
                    The other tensor to compare for equality.
        """
        pass

    @classmethod
    def from_dense_numpy(cls, type_cls, obj, dim_names=None): # real signature unknown; restored from __doc__
        """
        SparseCSCMatrix.from_dense_numpy(type cls, obj, dim_names=None)
        
                Convert numpy.ndarray to arrow::SparseCSCMatrix
        """
        pass

    def from_numpy(self, data, indptr, indices, shape, dim_names=None): # real signature unknown; restored from __doc__
        """
        SparseCSCMatrix.from_numpy(data, indptr, indices, shape, dim_names=None)
        
                Create arrow::SparseCSCMatrix from numpy.ndarrays
        
                Parameters
                ----------
                data : numpy.ndarray
                    Data used to populate the sparse matrix.
                indptr : numpy.ndarray
                    Range of the rows,
                    The i-th row spans from `indptr[i]` to `indptr[i+1]` in the data.
                indices : numpy.ndarray
                    Column indices of the corresponding non-zero values.
                shape : tuple
                    Shape of the matrix.
                dim_names : list, optional
                    Names of the dimensions.
        """
        pass

    def from_scipy(self, obj, dim_names=None): # real signature unknown; restored from __doc__
        """
        SparseCSCMatrix.from_scipy(obj, dim_names=None)
        
                Convert scipy.sparse.csc_matrix to arrow::SparseCSCMatrix
        
                Parameters
                ----------
                obj : scipy.sparse.csc_matrix
                    The scipy matrix that should be converted.
                dim_names : list, optional
                    Names of the dimensions.
        """
        pass

    def from_tensor(self, obj): # real signature unknown; restored from __doc__
        """
        SparseCSCMatrix.from_tensor(obj)
        
                Convert arrow::Tensor to arrow::SparseCSCMatrix
        
                Parameters
                ----------
                obj : Tensor
                    The dense tensor that should be converted.
        """
        pass

    def to_numpy(self): # real signature unknown; restored from __doc__
        """
        SparseCSCMatrix.to_numpy(self)
        
                Convert arrow::SparseCSCMatrix to numpy.ndarrays with zero copy
        """
        pass

    def to_scipy(self): # real signature unknown; restored from __doc__
        """
        SparseCSCMatrix.to_scipy(self)
        
                Convert arrow::SparseCSCMatrix to scipy.sparse.csc_matrix
        """
        pass

    def to_tensor(self): # real signature unknown; restored from __doc__
        """
        SparseCSCMatrix.to_tensor(self)
        
                Convert arrow::SparseCSCMatrix to arrow::Tensor
        """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ SparseCSCMatrix.__reduce_cython__(self) """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ SparseCSCMatrix.__setstate_cython__(self, __pyx_state) """
        pass

    dim_names = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_mutable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ndim = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    non_zero_length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    shape = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __hash__ = None
    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001970BC82DE0>'


