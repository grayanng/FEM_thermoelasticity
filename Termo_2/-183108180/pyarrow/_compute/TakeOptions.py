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


from ._TakeOptions import _TakeOptions

class TakeOptions(_TakeOptions):
    """
    Options for the `take` and `array_take` functions.
    
        Parameters
        ----------
        boundscheck : boolean, default True
            Whether to check indices are within bounds. If False and an
            index is out of boundes, behavior is undefined (the process
            may crash).
    """
    def __init__(self, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ TakeOptions.__init__(self, *, boundscheck=True) """
        pass

    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'pyarrow._compute', '__doc__': '\\n    Options for the `take` and `array_take` functions.\\n\\n    Parameters\\n    ----------\\n    boundscheck : boolean, default True\\n        Whether to check indices are within bounds. If False and an\\n        index is out of boundes, behavior is undefined (the process\\n        may crash).\\n    ', '__init__': <cyfunction TakeOptions.__init__ at 0x000001FC28B88520>, '__dict__': <attribute '__dict__' of 'TakeOptions' objects>})"


