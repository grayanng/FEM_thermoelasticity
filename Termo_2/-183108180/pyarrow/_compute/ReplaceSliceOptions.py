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


from ._ReplaceSliceOptions import _ReplaceSliceOptions

class ReplaceSliceOptions(_ReplaceSliceOptions):
    """
    Options for replacing slices.
    
        Parameters
        ----------
        start : int
            Index to start slicing at (inclusive).
        stop : int
            Index to stop slicing at (exclusive).
        replacement : str
            What to replace the slice with.
    """
    def __init__(self, start, stop, replacement): # real signature unknown; restored from __doc__
        """ ReplaceSliceOptions.__init__(self, start, stop, replacement) """
        pass

    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'pyarrow._compute', '__doc__': '\\n    Options for replacing slices.\\n\\n    Parameters\\n    ----------\\n    start : int\\n        Index to start slicing at (inclusive).\\n    stop : int\\n        Index to stop slicing at (exclusive).\\n    replacement : str\\n        What to replace the slice with.\\n    ', '__init__': <cyfunction ReplaceSliceOptions.__init__ at 0x000001FC28B882B0>, '__dict__': <attribute '__dict__' of 'ReplaceSliceOptions' objects>})"


