# encoding: utf-8
# module pyarrow._compute
# from C:\Users\akharin\PycharmProjects\pythonProject\venv\lib\site-packages\pyarrow\_compute.cp39-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import sys as sys # <module 'sys' (built-in)>
import pyarrow.lib as lib # C:\Users\akharin\PycharmProjects\pythonProject\venv\lib\site-packages\pyarrow\lib.cp39-win_amd64.pyd
import inspect as inspect # C:\Users\akharin\AppData\Local\Programs\Python\Python39\lib\inspect.py
import numpy as np # C:\Users\akharin\PycharmProjects\pythonProject\venv\lib\site-packages\numpy\__init__.py
from pyarrow.lib import ArrowInvalid, frombytes, tobytes

import pyarrow.lib as __pyarrow_lib


class Function(__pyarrow_lib._Weakrefable):
    """
    Function()
    
        A compute function.
    
        A function implements a certain logical computation over a range of
        possible input signatures.  Each signature accepts a range of input
        types and is implemented by a given Kernel.
    
        Functions can be of different kinds:
    
        * "scalar" functions apply an item-wise computation over all items
          of their inputs.  Each item in the output only depends on the values
          of the inputs at the same position.  Examples: addition, comparisons,
          string predicates...
    
        * "vector" functions apply a collection-wise computation, such that
          each item in the output may depend on the values of several items
          in each input.  Examples: dictionary encoding, sorting, extracting
          unique values...
    
        * "scalar_aggregate" functions reduce the dimensionality of the inputs by
          applying a reduction function.  Examples: sum, min_max, mode...
    
        * "hash_aggregate" functions apply a reduction function to an input
          subdivided by grouping criteria.  They may not be directly called.
          Examples: hash_sum, hash_min_max...
    
        * "meta" functions dispatch to other functions.
    """
    def call(self, args, FunctionOptions_options=None, MemoryPool_memory_pool=None, length=None): # real signature unknown; restored from __doc__
        """
        Function.call(self, args, FunctionOptions options=None, MemoryPool memory_pool=None, length=None)
        
                Call the function on the given arguments.
        
                Parameters
                ----------
                args : iterable
                    The arguments to pass to the function.  Accepted types depend
                    on the specific function.
                options : FunctionOptions, optional
                    Options instance for executing this function.  This should have
                    the right concrete options type.
                memory_pool : pyarrow.MemoryPool, optional
                    If not passed, will allocate memory from the default memory pool.
                length : int, optional
                    Batch size for execution, for nullary (no argument) functions. If
                    not passed, will be inferred from passed data.
        """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self): # real signature unknown; restored from __doc__
        """ Function.__reduce__(self) """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    arity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        The function arity.

        If Ellipsis (i.e. `...`) is returned, the function takes a variable
        number of arguments.
        """

    kind = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        The function kind.
        """

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        The function name.
        """

    num_kernels = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        The number of kernels implementing this function.
        """

    _doc = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        The C++-like function documentation (for internal use).
        """


    _kind_map = {
        0: 'scalar',
        1: 'vector',
        2: 'scalar_aggregate',
        3: 'hash_aggregate',
        4: 'meta',
    }
    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001FC28B435A0>'


