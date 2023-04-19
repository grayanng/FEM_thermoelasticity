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


from ._StrftimeOptions import _StrftimeOptions

class StrftimeOptions(_StrftimeOptions):
    """
    Options for the `strftime` function.
    
        Parameters
        ----------
        format : str, default "%Y-%m-%dT%H:%M:%S"
            Pattern for formatting input values.
        locale : str, default "C"
            Locale to use for locale-specific format specifiers.
    """
    def __init__(self, format=None, locale=None): # real signature unknown; restored from __doc__
        """ StrftimeOptions.__init__(self, format=u'%Y-%m-%dT%H:%M:%S', locale=u'C') """
        pass

    __dict__ = None # (!) real value is 'mappingproxy({\'__module__\': \'pyarrow._compute\', \'__doc__\': \'\\n    Options for the `strftime` function.\\n\\n    Parameters\\n    ----------\\n    format : str, default "%Y-%m-%dT%H:%M:%S"\\n        Pattern for formatting input values.\\n    locale : str, default "C"\\n        Locale to use for locale-specific format specifiers.\\n    \', \'__init__\': <cyfunction StrftimeOptions.__init__ at 0x000001FC28B88D40>, \'__dict__\': <attribute \'__dict__\' of \'StrftimeOptions\' objects>})'


