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


from ._StrptimeOptions import _StrptimeOptions

class StrptimeOptions(_StrptimeOptions):
    """
    Options for the `strptime` function.
    
        Parameters
        ----------
        format : str
            Pattern for parsing input strings as timestamps, such as "%Y/%m/%d".
        unit : str
            Timestamp unit of the output.
            Accepted values are "s", "ms", "us", "ns".
        error_is_null : boolean, default False
            Return null on parsing errors if true or raise if false.
    """
    def __init__(self, format, unit, error_is_null=False): # real signature unknown; restored from __doc__
        """ StrptimeOptions.__init__(self, format, unit, error_is_null=False) """
        pass

    __dict__ = None # (!) real value is 'mappingproxy({\'__module__\': \'pyarrow._compute\', \'__doc__\': \'\\n    Options for the `strptime` function.\\n\\n    Parameters\\n    ----------\\n    format : str\\n        Pattern for parsing input strings as timestamps, such as "%Y/%m/%d".\\n    unit : str\\n        Timestamp unit of the output.\\n        Accepted values are "s", "ms", "us", "ns".\\n    error_is_null : boolean, default False\\n        Return null on parsing errors if true or raise if false.\\n    \', \'__init__\': <cyfunction StrptimeOptions.__init__ at 0x000001FC28B88C70>, \'__dict__\': <attribute \'__dict__\' of \'StrptimeOptions\' objects>})'


