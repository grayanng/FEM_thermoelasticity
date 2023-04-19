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


from ._Utf8NormalizeOptions import _Utf8NormalizeOptions

class Utf8NormalizeOptions(_Utf8NormalizeOptions):
    """
    Options for the `utf8_normalize` function.
    
        Parameters
        ----------
        form : str
            Unicode normalization form.
            Accepted values are "NFC", "NFKC", "NFD", NFKD".
    """
    def __init__(self, form): # real signature unknown; restored from __doc__
        """ Utf8NormalizeOptions.__init__(self, form) """
        pass

    __dict__ = None # (!) real value is 'mappingproxy({\'__module__\': \'pyarrow._compute\', \'__doc__\': \'\\n    Options for the `utf8_normalize` function.\\n\\n    Parameters\\n    ----------\\n    form : str\\n        Unicode normalization form.\\n        Accepted values are "NFC", "NFKC", "NFD", NFKD".\\n    \', \'__init__\': <cyfunction Utf8NormalizeOptions.__init__ at 0x000001FC28B91A00>, \'__dict__\': <attribute \'__dict__\' of \'Utf8NormalizeOptions\' objects>})'


