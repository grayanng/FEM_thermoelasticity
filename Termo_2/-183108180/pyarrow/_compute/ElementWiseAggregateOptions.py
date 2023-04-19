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


from ._ElementWiseAggregateOptions import _ElementWiseAggregateOptions

class ElementWiseAggregateOptions(_ElementWiseAggregateOptions):
    """
    Options for element-wise aggregate functions.
    
        Parameters
        ----------
        skip_nulls : bool, default True
            Whether to skip (ignore) nulls in the input.
            If False, any null in the input forces the output to null.
    """
    def __init__(self, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ ElementWiseAggregateOptions.__init__(self, *, skip_nulls=True) """
        pass

    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'pyarrow._compute', '__doc__': '\\n    Options for element-wise aggregate functions.\\n\\n    Parameters\\n    ----------\\n    skip_nulls : bool, default True\\n        Whether to skip (ignore) nulls in the input.\\n        If False, any null in the input forces the output to null.\\n\\n    ', '__init__': <cyfunction ElementWiseAggregateOptions.__init__ at 0x000001FC28B1AA00>, '__dict__': <attribute '__dict__' of 'ElementWiseAggregateOptions' objects>})"


