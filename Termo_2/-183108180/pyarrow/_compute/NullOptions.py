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


from ._NullOptions import _NullOptions

class NullOptions(_NullOptions):
    """
    Options for the `is_null` function.
    
        Parameters
        ----------
        nan_is_null : bool, default False
            Whether floating-point NaN values are considered null.
    """
    def __init__(self, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ NullOptions.__init__(self, *, nan_is_null=False) """
        pass

    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'pyarrow._compute', '__doc__': '\\n    Options for the `is_null` function.\\n\\n    Parameters\\n    ----------\\n    nan_is_null : bool, default False\\n        Whether floating-point NaN values are considered null.\\n    ', '__init__': <cyfunction NullOptions.__init__ at 0x000001FC28B91110>, '__dict__': <attribute '__dict__' of 'NullOptions' objects>})"


