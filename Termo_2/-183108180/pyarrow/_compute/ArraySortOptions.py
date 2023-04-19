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


from ._ArraySortOptions import _ArraySortOptions

class ArraySortOptions(_ArraySortOptions):
    """
    Options for the `array_sort_indices` function.
    
        Parameters
        ----------
        order : str, default "ascending"
            Which order to sort values in.
            Accepted values are "ascending", "descending".
        null_placement : str, default "at_end"
            Where nulls in the input should be sorted.
            Accepted values are "at_start", "at_end".
    """
    def __init__(self, order=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ ArraySortOptions.__init__(self, order=u'ascending', *, null_placement=u'at_end') """
        pass

    __dict__ = None # (!) real value is 'mappingproxy({\'__module__\': \'pyarrow._compute\', \'__doc__\': \'\\n    Options for the `array_sort_indices` function.\\n\\n    Parameters\\n    ----------\\n    order : str, default "ascending"\\n        Which order to sort values in.\\n        Accepted values are "ascending", "descending".\\n    null_placement : str, default "at_end"\\n        Where nulls in the input should be sorted.\\n        Accepted values are "at_start", "at_end".\\n    \', \'__init__\': <cyfunction ArraySortOptions.__init__ at 0x000001FC28B915F0>, \'__dict__\': <attribute \'__dict__\' of \'ArraySortOptions\' objects>})'


