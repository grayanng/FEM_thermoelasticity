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


class Expression(__pyarrow_lib._Weakrefable):
    """
    Expression()
    
        A logical expression to be evaluated against some input.
    
        To create an expression:
    
        - Use the factory function ``pyarrow.compute.scalar()`` to create a
          scalar (not necessary when combined, see example below).
        - Use the factory function ``pyarrow.compute.field()`` to reference
          a field (column in table).
        - Compare fields and scalars with ``<``, ``<=``, ``==``, ``>=``, ``>``.
        - Combine expressions using python operators ``&`` (logical and),
          ``|`` (logical or) and ``~`` (logical not).
          Note: python keywords ``and``, ``or`` and ``not`` cannot be used
          to combine expressions.
        - Create expression predicates using Expression methods such as
          ``pyarrow.compute.Expression.isin()``.
    
        Examples
        --------
    
        >>> import pyarrow.compute as pc
        >>> (pc.field("a") < pc.scalar(3)) | (pc.field("b") > 7)
        <pyarrow.compute.Expression ((a < 3) or (b > 7))>
        >>> pc.field('a') != 3
        <pyarrow.compute.Expression (a != 3)>
        >>> pc.field('a').isin([1, 2, 3])
        <pyarrow.compute.Expression is_in(a, {value_set=int64:[
          1,
          2,
          3
        ], skip_nulls=false})>
    """
    def cast(self, type=None, safe=None, options=None): # real signature unknown; restored from __doc__
        """
        Expression.cast(self, type=None, safe=None, options=None)
        
                Explicitly set or change the expression's data type.
        
                This creates a new expression equivalent to calling the
                `cast` compute function on this expression.
        
                Parameters
                ----------
                type : DataType, default None
                    Type to cast array to.
                safe : boolean, default True
                    Whether to check for conversion errors such as overflow.
                options : CastOptions, default None
                    Additional checks pass by CastOptions
        
                Returns
                -------
                cast : Expression
        """
        pass

    def equals(self, Expression_other): # real signature unknown; restored from __doc__
        """ Expression.equals(self, Expression other) """
        pass

    def isin(self, values): # real signature unknown; restored from __doc__
        """
        Expression.isin(self, values)
        
                Check whether the expression is contained in values.
        
                This creates a new expression equivalent to calling the
                `is_in` compute function on this expression.
        
                Parameters
                ----------
                values : Array or iterable
                    The values to check for.
        
                Returns
                -------
                isin : Expression
                    A new expression that, when evaluated, checks whether
                    this expression's value is contained in `values`.
        """
        pass

    def is_null(self, bool_nan_is_null=False): # real signature unknown; restored from __doc__
        """
        Expression.is_null(self, bool nan_is_null=False)
        
                Check whether the expression is null.
        
                This creates a new expression equivalent to calling the
                `is_null` compute function on this expression.
        
                Parameters
                ----------
                nan_is_null : boolean, default False
                    Whether floating-point NaNs are considered null.
        
                Returns
                -------
                is_null : Expression
        """
        pass

    def is_valid(self): # real signature unknown; restored from __doc__
        """
        Expression.is_valid(self)
        
                Check whether the expression is not-null (valid).
        
                This creates a new expression equivalent to calling the
                `is_valid` compute function on this expression.
        
                Returns
                -------
                is_valid : Expression
        """
        pass

    def _call(self, unicode_function_name, list_arguments, FunctionOptions_options=None): # real signature unknown; restored from __doc__
        """ Expression._call(unicode function_name, list arguments, FunctionOptions options=None) """
        pass

    def _deserialize(self, Buffer_buffer): # real signature unknown; restored from __doc__
        """ Expression._deserialize(Buffer buffer) """
        pass

    def _field(self, name_or_idx): # real signature unknown; restored from __doc__
        """ Expression._field(name_or_idx) """
        pass

    def _nested_field(self, tuple_names): # real signature unknown; restored from __doc__
        """ Expression._nested_field(tuple names) """
        pass

    def _scalar(self, value): # real signature unknown; restored from __doc__
        """ Expression._scalar(value) """
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        """ Return self+value. """
        pass

    def __and__(self, *args, **kwargs): # real signature unknown
        """ Return self&value. """
        pass

    def __bool__(self, *args, **kwargs): # real signature unknown
        """ True if self else False """
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

    def __invert__(self, *args, **kwargs): # real signature unknown
        """ ~self """
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

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __or__(self, *args, **kwargs): # real signature unknown
        """ Return self|value. """
        pass

    def __radd__(self, *args, **kwargs): # real signature unknown
        """ Return value+self. """
        pass

    def __rand__(self, *args, **kwargs): # real signature unknown
        """ Return value&self. """
        pass

    def __reduce__(self): # real signature unknown; restored from __doc__
        """ Expression.__reduce__(self) """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        """ Return value*self. """
        pass

    def __ror__(self, *args, **kwargs): # real signature unknown
        """ Return value|self. """
        pass

    def __rsub__(self, *args, **kwargs): # real signature unknown
        """ Return value-self. """
        pass

    def __rtruediv__(self, *args, **kwargs): # real signature unknown
        """ Return value/self. """
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

    __hash__ = None
    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001FC28B43390>'


