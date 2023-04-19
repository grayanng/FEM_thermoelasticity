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


from ._ReplaceSubstringOptions import _ReplaceSubstringOptions

class ReplaceSubstringOptions(_ReplaceSubstringOptions):
    """
    Options for replacing matched substrings.
    
        Parameters
        ----------
        pattern : str
            Substring pattern to look for inside input values.
        replacement : str
            What to replace the pattern with.
        max_replacements : int or None, default None
            The maximum number of strings to replace in each
            input value (unlimited if None).
    """
    def __init__(self, pattern, replacement, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ ReplaceSubstringOptions.__init__(self, pattern, replacement, *, max_replacements=None) """
        pass

    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'pyarrow._compute', '__doc__': '\\n    Options for replacing matched substrings.\\n\\n    Parameters\\n    ----------\\n    pattern : str\\n        Substring pattern to look for inside input values.\\n    replacement : str\\n        What to replace the pattern with.\\n    max_replacements : int or None, default None\\n        The maximum number of strings to replace in each\\n        input value (unlimited if None).\\n    ', '__init__': <cyfunction ReplaceSubstringOptions.__init__ at 0x000001FC28B1AEE0>, '__dict__': <attribute '__dict__' of 'ReplaceSubstringOptions' objects>})"


