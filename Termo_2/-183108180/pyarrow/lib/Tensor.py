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

class Tensor(_Weakrefable):
    """
    Tensor()
    
        A n-dimensional array a.k.a Tensor.
    
        Examples
        --------
        >>> import pyarrow as pa
        >>> import numpy as np
        >>> x = np.array([[2, 2, 4], [4, 5, 100]], np.int32)
        >>> pa.Tensor.from_numpy(x, dim_names=["dim1","dim2"])
        <pyarrow.Tensor>
        type: int32
        shape: (2, 3)
        strides: (12, 4)
    """
    def dim_name(self, i): # real signature unknown; restored from __doc__
        """
        Tensor.dim_name(self, i)
        
                Returns the name of the i-th tensor dimension.
        
                Parameters
                ----------
                i : int
                    The physical index of the tensor dimension.
        
                Examples
                --------
                >>> import pyarrow as pa
                >>> import numpy as np
                >>> x = np.array([[2, 2, 4], [4, 5, 100]], np.int32)
                >>> tensor = pa.Tensor.from_numpy(x, dim_names=["dim1","dim2"])
                >>> tensor.dim_name(0)
                'dim1'
                >>> tensor.dim_name(1)
                'dim2'
        """
        pass

    def equals(self, Tensor_other): # real signature unknown; restored from __doc__
        """
        Tensor.equals(self, Tensor other)
        
                Return true if the tensors contains exactly equal data.
        
                Parameters
                ----------
                other : Tensor
                    The other tensor to compare for equality.
        
                Examples
                --------
                >>> import pyarrow as pa
                >>> import numpy as np
                >>> x = np.array([[2, 2, 4], [4, 5, 100]], np.int32)
                >>> tensor = pa.Tensor.from_numpy(x, dim_names=["dim1","dim2"])
                >>> y = np.array([[2, 2, 4], [4, 5, 10]], np.int32)
                >>> tensor2 = pa.Tensor.from_numpy(y, dim_names=["a","b"])
                >>> tensor.equals(tensor)
                True
                >>> tensor.equals(tensor2)
                False
        """
        pass

    def from_numpy(self, obj, dim_names=None): # real signature unknown; restored from __doc__
        """
        Tensor.from_numpy(obj, dim_names=None)
        
                Create a Tensor from a numpy array.
        
                Parameters
                ----------
                obj : numpy.ndarray
                    The source numpy array
                dim_names : list, optional
                    Names of each dimension of the Tensor.
        
                Examples
                --------
                >>> import pyarrow as pa
                >>> import numpy as np
                >>> x = np.array([[2, 2, 4], [4, 5, 100]], np.int32)
                >>> pa.Tensor.from_numpy(x, dim_names=["dim1","dim2"])
                <pyarrow.Tensor>
                type: int32
                shape: (2, 3)
                strides: (12, 4)
        """
        pass

    def to_numpy(self): # real signature unknown; restored from __doc__
        """
        Tensor.to_numpy(self)
        
                Convert arrow::Tensor to numpy.ndarray with zero copy
        
                Examples
                --------
                >>> import pyarrow as pa
                >>> import numpy as np
                >>> x = np.array([[2, 2, 4], [4, 5, 100]], np.int32)
                >>> tensor = pa.Tensor.from_numpy(x, dim_names=["dim1","dim2"])
                >>> tensor.to_numpy()
                array([[  2,   2,   4],
                       [  4,   5, 100]], dtype=int32)
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
        """ Tensor.__reduce_cython__(self) """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ Tensor.__setstate_cython__(self, __pyx_state) """
        pass

    dim_names = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Names of this tensor dimensions.

        Examples
        --------
        >>> import pyarrow as pa
        >>> import numpy as np
        >>> x = np.array([[2, 2, 4], [4, 5, 100]], np.int32)
        >>> tensor = pa.Tensor.from_numpy(x, dim_names=["dim1","dim2"])
        >>> tensor.dim_names
        ['dim1', 'dim2']
        """

    is_contiguous = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Is this tensor contiguous in memory.

        Examples
        --------
        >>> import pyarrow as pa
        >>> import numpy as np
        >>> x = np.array([[2, 2, 4], [4, 5, 100]], np.int32)
        >>> tensor = pa.Tensor.from_numpy(x, dim_names=["dim1","dim2"])
        >>> tensor.is_contiguous
        True
        """

    is_mutable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Is this tensor mutable or immutable.

        Examples
        --------
        >>> import pyarrow as pa
        >>> import numpy as np
        >>> x = np.array([[2, 2, 4], [4, 5, 100]], np.int32)
        >>> tensor = pa.Tensor.from_numpy(x, dim_names=["dim1","dim2"])
        >>> tensor.is_mutable
        True
        """

    ndim = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        The dimension (n) of this tensor.

        Examples
        --------
        >>> import pyarrow as pa
        >>> import numpy as np
        >>> x = np.array([[2, 2, 4], [4, 5, 100]], np.int32)
        >>> tensor = pa.Tensor.from_numpy(x, dim_names=["dim1","dim2"])
        >>> tensor.ndim
        2
        """

    shape = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        The shape of this tensor.

        Examples
        --------
        >>> import pyarrow as pa
        >>> import numpy as np
        >>> x = np.array([[2, 2, 4], [4, 5, 100]], np.int32)
        >>> tensor = pa.Tensor.from_numpy(x, dim_names=["dim1","dim2"])
        >>> tensor.shape
        (2, 3)
        """

    size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        The size of this tensor.

        Examples
        --------
        >>> import pyarrow as pa
        >>> import numpy as np
        >>> x = np.array([[2, 2, 4], [4, 5, 100]], np.int32)
        >>> tensor = pa.Tensor.from_numpy(x, dim_names=["dim1","dim2"])
        >>> tensor.size
        6
        """

    strides = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Strides of this tensor.

        Examples
        --------
        >>> import pyarrow as pa
        >>> import numpy as np
        >>> x = np.array([[2, 2, 4], [4, 5, 100]], np.int32)
        >>> tensor = pa.Tensor.from_numpy(x, dim_names=["dim1","dim2"])
        >>> tensor.strides
        (12, 4)
        """

    type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __hash__ = None
    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001970BC82EA0>'


