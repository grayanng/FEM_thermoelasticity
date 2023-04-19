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


from ._CumulativeSumOptions import _CumulativeSumOptions

class CumulativeSumOptions(_CumulativeSumOptions):
    """
    Options for `cumulative_sum` function.
    
        Parameters
        ----------
        start : Scalar, default 0.0
            Starting value for sum computation
        skip_nulls : bool, default False
            When false, the first encountered null is propagated.
    """
    def __init__(self, start=0.0, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ CumulativeSumOptions.__init__(self, start=0.0, *, skip_nulls=False) """
        pass

    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'pyarrow._compute', '__doc__': '\\n    Options for `cumulative_sum` function.\\n\\n    Parameters\\n    ----------\\n    start : Scalar, default 0.0\\n        Starting value for sum computation\\n    skip_nulls : bool, default False\\n        When false, the first encountered null is propagated.\\n    ', '__init__': <cyfunction CumulativeSumOptions.__init__ at 0x000001FC28B91520>, '__dict__': <attribute '__dict__' of 'CumulativeSumOptions' objects>})"


