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


from ._ModeOptions import _ModeOptions

class ModeOptions(_ModeOptions):
    """
    Options for the `mode` function.
    
        Parameters
        ----------
        n : int, default 1
            Number of distinct most-common values to return.
        skip_nulls : bool, default True
            Whether to skip (ignore) nulls in the input.
            If False, any null in the input forces the output to null.
    
        min_count : int, default 0
            Minimum number of non-null values in the input.  If the number
            of non-null values is below `min_count`, the output is null.
    """
    def __init__(self, n=1, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ ModeOptions.__init__(self, n=1, *, skip_nulls=True, min_count=0) """
        pass

    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'pyarrow._compute', '__doc__': '\\n    Options for the `mode` function.\\n\\n    Parameters\\n    ----------\\n    n : int, default 1\\n        Number of distinct most-common values to return.\\n    skip_nulls : bool, default True\\n        Whether to skip (ignore) nulls in the input.\\n        If False, any null in the input forces the output to null.\\n\\n    min_count : int, default 0\\n        Minimum number of non-null values in the input.  If the number\\n        of non-null values is below `min_count`, the output is null.\\n\\n    ', '__init__': <cyfunction ModeOptions.__init__ at 0x000001FC28B88AD0>, '__dict__': <attribute '__dict__' of 'ModeOptions' objects>})"


