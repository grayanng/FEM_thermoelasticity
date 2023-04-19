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


from ._MatchSubstringOptions import _MatchSubstringOptions

class MatchSubstringOptions(_MatchSubstringOptions):
    """
    Options for looking for a substring.
    
        Parameters
        ----------
        pattern : str
            Substring pattern to look for inside input values.
        ignore_case : bool, default False
            Whether to perform a case-insensitive match.
    """
    def __init__(self, pattern, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ MatchSubstringOptions.__init__(self, pattern, *, ignore_case=False) """
        pass

    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'pyarrow._compute', '__doc__': '\\n    Options for looking for a substring.\\n\\n    Parameters\\n    ----------\\n    pattern : str\\n        Substring pattern to look for inside input values.\\n    ignore_case : bool, default False\\n        Whether to perform a case-insensitive match.\\n    ', '__init__': <cyfunction MatchSubstringOptions.__init__ at 0x000001FC28B1AC70>, '__dict__': <attribute '__dict__' of 'MatchSubstringOptions' objects>})"


