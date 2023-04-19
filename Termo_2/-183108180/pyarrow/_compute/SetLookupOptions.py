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


from ._SetLookupOptions import _SetLookupOptions

class SetLookupOptions(_SetLookupOptions):
    """
    Options for the `is_in` and `index_in` functions.
    
        Parameters
        ----------
        value_set : Array
            Set of values to look for in the input.
        skip_nulls : bool, default False
            If False, nulls in the input are matched in the value_set just
            like regular values.
            If True, nulls in the input always fail matching.
    """
    def __init__(self, value_set, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ SetLookupOptions.__init__(self, value_set, *, skip_nulls=False) """
        pass

    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'pyarrow._compute', '__doc__': '\\n    Options for the `is_in` and `index_in` functions.\\n\\n    Parameters\\n    ----------\\n    value_set : Array\\n        Set of values to look for in the input.\\n    skip_nulls : bool, default False\\n        If False, nulls in the input are matched in the value_set just\\n        like regular values.\\n        If True, nulls in the input always fail matching.\\n    ', '__init__': <cyfunction SetLookupOptions.__init__ at 0x000001FC28B88BA0>, '__dict__': <attribute '__dict__' of 'SetLookupOptions' objects>})"


