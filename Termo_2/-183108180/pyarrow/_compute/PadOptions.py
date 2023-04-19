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


from ._PadOptions import _PadOptions

class PadOptions(_PadOptions):
    """
    Options for padding strings.
    
        Parameters
        ----------
        width : int
            Desired string length.
        padding : str, default " "
            What to pad the string with. Should be one byte or codepoint.
    """
    def __init__(self, width, padding=None): # real signature unknown; restored from __doc__
        """ PadOptions.__init__(self, width, padding=u' ') """
        pass

    __dict__ = None # (!) real value is 'mappingproxy({\'__module__\': \'pyarrow._compute\', \'__doc__\': \'\\n    Options for padding strings.\\n\\n    Parameters\\n    ----------\\n    width : int\\n        Desired string length.\\n    padding : str, default " "\\n        What to pad the string with. Should be one byte or codepoint.\\n    \', \'__init__\': <cyfunction PadOptions.__init__ at 0x000001FC28B1AD40>, \'__dict__\': <attribute \'__dict__\' of \'PadOptions\' objects>})'


