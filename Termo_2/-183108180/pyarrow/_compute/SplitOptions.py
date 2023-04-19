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


from ._SplitOptions import _SplitOptions

class SplitOptions(_SplitOptions):
    """
    Options for splitting on whitespace.
    
        Parameters
        ----------
        max_splits : int or None, default None
            Maximum number of splits for each input value (unlimited if None).
        reverse : bool, default False
            Whether to start splitting from the end of each input value.
            This only has an effect if `max_splits` is not None.
    """
    def __init__(self, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ SplitOptions.__init__(self, *, max_splits=None, reverse=False) """
        pass

    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'pyarrow._compute', '__doc__': '\\n    Options for splitting on whitespace.\\n\\n    Parameters\\n    ----------\\n    max_splits : int or None, default None\\n        Maximum number of splits for each input value (unlimited if None).\\n    reverse : bool, default False\\n        Whether to start splitting from the end of each input value.\\n        This only has an effect if `max_splits` is not None.\\n    ', '__init__': <cyfunction SplitOptions.__init__ at 0x000001FC28B912B0>, '__dict__': <attribute '__dict__' of 'SplitOptions' objects>})"


