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


# functions

def call_function(name, args, options=None, memory_pool=None, length=None): # real signature unknown; restored from __doc__
    """
    call_function(name, args, options=None, memory_pool=None, length=None)
    
        Call a named function.
    
        The function is looked up in the global registry
        (as returned by `function_registry()`).
    
        Parameters
        ----------
        name : str
            The name of the function to call.
        args : list
            The arguments to the function.
        options : optional
            options provided to the function.
        memory_pool : MemoryPool, optional
            memory pool to use for allocations during function execution.
        length : int, optional
            Batch size for execution, for nullary (no argument) functions. If not
            passed, inferred from data.
    """
    pass

def function_registry(): # real signature unknown; restored from __doc__
    """ function_registry() """
    pass

def get_function(name): # real signature unknown; restored from __doc__
    """
    get_function(name)
    
        Get a function by name.
    
        The function is looked up in the global registry
        (as returned by `function_registry()`).
    
        Parameters
        ----------
        name : str
            The name of the function to lookup
    """
    pass

def list_functions(): # real signature unknown; restored from __doc__
    """
    list_functions()
    
        Return all function names in the global registry.
    """
    pass

def namedtuple(typename, field_names, *, rename=False, defaults=None, module=None): # reliably restored by inspect
    """
    Returns a new subclass of tuple with named fields.
    
        >>> Point = namedtuple('Point', ['x', 'y'])
        >>> Point.__doc__                   # docstring for the new class
        'Point(x, y)'
        >>> p = Point(11, y=22)             # instantiate with positional args or keywords
        >>> p[0] + p[1]                     # indexable like a plain tuple
        33
        >>> x, y = p                        # unpack like a regular tuple
        >>> x, y
        (11, 22)
        >>> p.x + p.y                       # fields also accessible by name
        33
        >>> d = p._asdict()                 # convert to a dictionary
        >>> d['x']
        11
        >>> Point(**d)                      # convert from a dictionary
        Point(x=11, y=22)
        >>> p._replace(x=100)               # _replace() is like str.replace() but targets named fields
        Point(x=100, y=22)
    """
    pass

def register_scalar_function(func, function_name, function_doc, in_types, out_type): # real signature unknown; restored from __doc__
    """
    register_scalar_function(func, function_name, function_doc, in_types, out_type)
    
        Register a user-defined scalar function.
    
        A scalar function is a function that executes elementwise
        operations on arrays or scalars, i.e. a scalar function must
        be computed row-by-row with no state where each output row
        is computed only from its corresponding input row.
        In other words, all argument arrays have the same length,
        and the output array is of the same length as the arguments.
        Scalar functions are the only functions allowed in query engine
        expressions.
    
        Parameters
        ----------
        func : callable
            A callable implementing the user-defined function.
            The first argument is the context argument of type
            ScalarUdfContext.
            Then, it must take arguments equal to the number of
            in_types defined. It must return an Array or Scalar
            matching the out_type. It must return a Scalar if
            all arguments are scalar, else it must return an Array.
    
            To define a varargs function, pass a callable that takes
            varargs. The last in_type will be the type of all varargs
            arguments.
        function_name : str
            Name of the function. This name must be globally unique.
        function_doc : dict
            A dictionary object with keys "summary" (str),
            and "description" (str).
        in_types : Dict[str, DataType]
            A dictionary mapping function argument names to
            their respective DataType.
            The argument names will be used to generate
            documentation for the function. The number of
            arguments specified here determines the function
            arity.
        out_type : DataType
            Output type of the function.
    
        Examples
        --------
        >>> import pyarrow as pa
        >>> import pyarrow.compute as pc
        >>>
        >>> func_doc = {}
        >>> func_doc["summary"] = "simple udf"
        >>> func_doc["description"] = "add a constant to a scalar"
        >>>
        >>> def add_constant(ctx, array):
        ...     return pc.add(array, 1, memory_pool=ctx.memory_pool)
        >>>
        >>> func_name = "py_add_func"
        >>> in_types = {"array": pa.int64()}
        >>> out_type = pa.int64()
        >>> pc.register_scalar_function(add_constant, func_name, func_doc,
        ...                   in_types, out_type)
        >>>
        >>> func = pc.get_function(func_name)
        >>> func.name
        'py_add_func'
        >>> answer = pc.call_function(func_name, [pa.array([20])])
        >>> answer
        <pyarrow.lib.Int64Array object at ...>
        [
          21
        ]
    """
    pass

def _deserialize(Buffer_buffer): # real signature unknown; restored from __doc__
    """ Expression._deserialize(Buffer buffer) """
    pass

def _get_scalar_udf_context(memory_pool, batch_length): # real signature unknown; restored from __doc__
    """ _get_scalar_udf_context(memory_pool, batch_length) """
    pass

def _group_by(args, keys, aggregations): # real signature unknown; restored from __doc__
    """ _group_by(args, keys, aggregations) """
    pass

def _min_count_doc(*args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """ _min_count_doc(*, default) """
    pass

def _raise_invalid_function_option(value, description, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """ _raise_invalid_function_option(value, description, *, exception_class=ValueError) """
    pass

def _skip_nulls_doc(): # real signature unknown; restored from __doc__
    """ _skip_nulls_doc() """
    pass

def __pyx_unpickle_Kernel(__pyx_type, long___pyx_checksum, __pyx_state): # real signature unknown; restored from __doc__
    """ __pyx_unpickle_Kernel(__pyx_type, long __pyx_checksum, __pyx_state) """
    pass

# classes

from .FunctionOptions import FunctionOptions
from ._ArraySortOptions import _ArraySortOptions
from .ArraySortOptions import ArraySortOptions
from ._AssumeTimezoneOptions import _AssumeTimezoneOptions
from .AssumeTimezoneOptions import AssumeTimezoneOptions
from ._CastOptions import _CastOptions
from .CastOptions import CastOptions
from ._CountOptions import _CountOptions
from .CountOptions import CountOptions
from ._CumulativeSumOptions import _CumulativeSumOptions
from .CumulativeSumOptions import CumulativeSumOptions
from ._DayOfWeekOptions import _DayOfWeekOptions
from .DayOfWeekOptions import DayOfWeekOptions
from ._DictionaryEncodeOptions import _DictionaryEncodeOptions
from .DictionaryEncodeOptions import DictionaryEncodeOptions
from ._ElementWiseAggregateOptions import _ElementWiseAggregateOptions
from .ElementWiseAggregateOptions import ElementWiseAggregateOptions
from .Expression import Expression
from ._ExtractRegexOptions import _ExtractRegexOptions
from .ExtractRegexOptions import ExtractRegexOptions
from ._FilterOptions import _FilterOptions
from .FilterOptions import FilterOptions
from .Function import Function
from .FunctionDoc import FunctionDoc
from .FunctionRegistry import FunctionRegistry
from .HashAggregateFunction import HashAggregateFunction
from .Kernel import Kernel
from .HashAggregateKernel import HashAggregateKernel
from ._IndexOptions import _IndexOptions
from .IndexOptions import IndexOptions
from ._JoinOptions import _JoinOptions
from .JoinOptions import JoinOptions
from ._ListSliceOptions import _ListSliceOptions
from .ListSliceOptions import ListSliceOptions
from ._MakeStructOptions import _MakeStructOptions
from .MakeStructOptions import MakeStructOptions
from ._MapLookupOptions import _MapLookupOptions
from .MapLookupOptions import MapLookupOptions
from ._MatchSubstringOptions import _MatchSubstringOptions
from .MatchSubstringOptions import MatchSubstringOptions
from .MetaFunction import MetaFunction
from ._ModeOptions import _ModeOptions
from .ModeOptions import ModeOptions
from ._NullOptions import _NullOptions
from .NullOptions import NullOptions
from .ordered_dict import ordered_dict
from ._PadOptions import _PadOptions
from .PadOptions import PadOptions
from ._PartitionNthOptions import _PartitionNthOptions
from .PartitionNthOptions import PartitionNthOptions
from ._QuantileOptions import _QuantileOptions
from .QuantileOptions import QuantileOptions
from ._RandomOptions import _RandomOptions
from .RandomOptions import RandomOptions
from ._RankOptions import _RankOptions
from .RankOptions import RankOptions
from ._ReplaceSliceOptions import _ReplaceSliceOptions
from .ReplaceSliceOptions import ReplaceSliceOptions
from ._ReplaceSubstringOptions import _ReplaceSubstringOptions
from .ReplaceSubstringOptions import ReplaceSubstringOptions
from ._RoundOptions import _RoundOptions
from .RoundOptions import RoundOptions
from ._RoundTemporalOptions import _RoundTemporalOptions
from .RoundTemporalOptions import RoundTemporalOptions
from ._RoundToMultipleOptions import _RoundToMultipleOptions
from .RoundToMultipleOptions import RoundToMultipleOptions
from .ScalarAggregateFunction import ScalarAggregateFunction
from .ScalarAggregateKernel import ScalarAggregateKernel
from ._ScalarAggregateOptions import _ScalarAggregateOptions
from .ScalarAggregateOptions import ScalarAggregateOptions
from .ScalarFunction import ScalarFunction
from .ScalarKernel import ScalarKernel
from .ScalarUdfContext import ScalarUdfContext
from ._SelectKOptions import _SelectKOptions
from .SelectKOptions import SelectKOptions
from ._SetLookupOptions import _SetLookupOptions
from .SetLookupOptions import SetLookupOptions
from ._SliceOptions import _SliceOptions
from .SliceOptions import SliceOptions
from ._SortOptions import _SortOptions
from .SortOptions import SortOptions
from ._SplitOptions import _SplitOptions
from .SplitOptions import SplitOptions
from ._SplitPatternOptions import _SplitPatternOptions
from .SplitPatternOptions import SplitPatternOptions
from ._StrftimeOptions import _StrftimeOptions
from .StrftimeOptions import StrftimeOptions
from ._StrptimeOptions import _StrptimeOptions
from .StrptimeOptions import StrptimeOptions
from ._StructFieldOptions import _StructFieldOptions
from .StructFieldOptions import StructFieldOptions
from ._TakeOptions import _TakeOptions
from .TakeOptions import TakeOptions
from ._TDigestOptions import _TDigestOptions
from .TDigestOptions import TDigestOptions
from ._TrimOptions import _TrimOptions
from .TrimOptions import TrimOptions
from ._Utf8NormalizeOptions import _Utf8NormalizeOptions
from .Utf8NormalizeOptions import Utf8NormalizeOptions
from ._VarianceOptions import _VarianceOptions
from .VarianceOptions import VarianceOptions
from .VectorFunction import VectorFunction
from .VectorKernel import VectorKernel
from ._WeekOptions import _WeekOptions
from .WeekOptions import WeekOptions
# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x000001FC1A53F700>'

__pyx_capi__ = {
    '_bind': None, # (!) real value is '<capsule object "arrow::compute::Expression (struct __pyx_obj_7pyarrow_8_compute_Expression *, struct __pyx_obj_7pyarrow_3lib_Schema *)" at 0x000001FC28B43210>'
    '_true': None, # (!) real value is '<capsule object "arrow::compute::Expression" at 0x000001FC28B431E0>'
}

__spec__ = None # (!) real value is "ModuleSpec(name='pyarrow._compute', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x000001FC1A53F700>, origin='C:\\\\Users\\\\akharin\\\\PycharmProjects\\\\pythonProject\\\\venv\\\\lib\\\\site-packages\\\\pyarrow\\\\_compute.cp39-win_amd64.pyd')"

__test__ = {
    'register_scalar_function (line 2594)': '\n    Register a user-defined scalar function.\n\n    A scalar function is a function that executes elementwise\n    operations on arrays or scalars, i.e. a scalar function must\n    be computed row-by-row with no state where each output row\n    is computed only from its corresponding input row.\n    In other words, all argument arrays have the same length,\n    and the output array is of the same length as the arguments.\n    Scalar functions are the only functions allowed in query engine\n    expressions.\n\n    Parameters\n    ----------\n    func : callable\n        A callable implementing the user-defined function.\n        The first argument is the context argument of type\n        ScalarUdfContext.\n        Then, it must take arguments equal to the number of\n        in_types defined. It must return an Array or Scalar\n        matching the out_type. It must return a Scalar if\n        all arguments are scalar, else it must return an Array.\n\n        To define a varargs function, pass a callable that takes\n        varargs. The last in_type will be the type of all varargs\n        arguments.\n    function_name : str\n        Name of the function. This name must be globally unique.\n    function_doc : dict\n        A dictionary object with keys "summary" (str),\n        and "description" (str).\n    in_types : Dict[str, DataType]\n        A dictionary mapping function argument names to\n        their respective DataType.\n        The argument names will be used to generate\n        documentation for the function. The number of\n        arguments specified here determines the function\n        arity.\n    out_type : DataType\n        Output type of the function.\n\n    Examples\n    --------\n    >>> import pyarrow as pa\n    >>> import pyarrow.compute as pc\n    >>>\n    >>> func_doc = {}\n    >>> func_doc["summary"] = "simple udf"\n    >>> func_doc["description"] = "add a constant to a scalar"\n    >>>\n    >>> def add_constant(ctx, array):\n    ...     return pc.add(array, 1, memory_pool=ctx.memory_pool)\n    >>>\n    >>> func_name = "py_add_func"\n    >>> in_types = {"array": pa.int64()}\n    >>> out_type = pa.int64()\n    >>> pc.register_scalar_function(add_constant, func_name, func_doc,\n    ...                   in_types, out_type)\n    >>>\n    >>> func = pc.get_function(func_name)\n    >>> func.name\n    \'py_add_func\'\n    >>> answer = pc.call_function(func_name, [pa.array([20])])\n    >>> answer\n    <pyarrow.lib.Int64Array object at ...>\n    [\n      21\n    ]\n    ',
}

