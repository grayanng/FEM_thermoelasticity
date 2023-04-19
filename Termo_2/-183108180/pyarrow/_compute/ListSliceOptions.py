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


from ._ListSliceOptions import _ListSliceOptions

class ListSliceOptions(_ListSliceOptions):
    """
    Options for list array slicing.
    
        Parameters
        ----------
        start : int
            Index to start slicing inner list elements (inclusive).
        stop : Optional[int], default None
            If given, index to stop slicing at (exclusive).
            If not given, slicing will stop at the end. (NotImplemented)
        step : int, default 1
            Slice step.
        return_fixed_size_list : Optional[bool], default None
            Whether to return a FixedSizeListArray. If true _and_ stop is after
            a list element's length, nulls will be appended to create the
            requested slice size. The default of `None` will return the same
            type which was passed in.
    """
    def __init__(self, start, stop=None, step=1, return_fixed_size_list=None): # real signature unknown; restored from __doc__
        """ ListSliceOptions.__init__(self, start, stop=None, step=1, return_fixed_size_list=None) """
        pass

    __dict__ = None # (!) real value is 'mappingproxy({\'__module__\': \'pyarrow._compute\', \'__doc__\': "\\n    Options for list array slicing.\\n\\n    Parameters\\n    ----------\\n    start : int\\n        Index to start slicing inner list elements (inclusive).\\n    stop : Optional[int], default None\\n        If given, index to stop slicing at (exclusive).\\n        If not given, slicing will stop at the end. (NotImplemented)\\n    step : int, default 1\\n        Slice step.\\n    return_fixed_size_list : Optional[bool], default None\\n        Whether to return a FixedSizeListArray. If true _and_ stop is after\\n        a list element\'s length, nulls will be appended to create the\\n        requested slice size. The default of `None` will return the same\\n        type which was passed in.\\n    ", \'__init__\': <cyfunction ListSliceOptions.__init__ at 0x000001FC28B881E0>, \'__dict__\': <attribute \'__dict__\' of \'ListSliceOptions\' objects>})'


