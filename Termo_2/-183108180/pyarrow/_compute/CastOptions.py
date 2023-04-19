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


from ._CastOptions import _CastOptions

class CastOptions(_CastOptions):
    """
    Options for the `cast` function.
    
        Parameters
        ----------
        target_type : DataType, optional
            The PyArrow type to cast to.
        allow_int_overflow : bool, default False
            Whether integer overflow is allowed when casting.
        allow_time_truncate : bool, default False
            Whether time precision truncation is allowed when casting.
        allow_time_overflow : bool, default False
            Whether date/time range overflow is allowed when casting.
        allow_decimal_truncate : bool, default False
            Whether decimal precision truncation is allowed when casting.
        allow_float_truncate : bool, default False
            Whether floating-point precision truncation is allowed when casting.
        allow_invalid_utf8 : bool, default False
            Whether producing invalid utf8 data is allowed when casting.
    """
    def safe(self, target_type=None): # real signature unknown; restored from __doc__
        """
        CastOptions.safe(target_type=None)
        "
                Create a CastOptions for a safe cast.
        
                Parameters
                ----------
                target_type : optional
                    Target cast type for the safe cast.
        """
        pass

    def unsafe(self, target_type=None): # real signature unknown; restored from __doc__
        """
        CastOptions.unsafe(target_type=None)
        "
                Create a CastOptions for an unsafe cast.
        
                Parameters
                ----------
                target_type : optional
                    Target cast type for the unsafe cast.
        """
        pass

    def __init__(self, target_type=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ CastOptions.__init__(self, target_type=None, *, allow_int_overflow=None, allow_time_truncate=None, allow_time_overflow=None, allow_decimal_truncate=None, allow_float_truncate=None, allow_invalid_utf8=None) """
        pass

    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'pyarrow._compute', '__doc__': '\\n    Options for the `cast` function.\\n\\n    Parameters\\n    ----------\\n    target_type : DataType, optional\\n        The PyArrow type to cast to.\\n    allow_int_overflow : bool, default False\\n        Whether integer overflow is allowed when casting.\\n    allow_time_truncate : bool, default False\\n        Whether time precision truncation is allowed when casting.\\n    allow_time_overflow : bool, default False\\n        Whether date/time range overflow is allowed when casting.\\n    allow_decimal_truncate : bool, default False\\n        Whether decimal precision truncation is allowed when casting.\\n    allow_float_truncate : bool, default False\\n        Whether floating-point precision truncation is allowed when casting.\\n    allow_invalid_utf8 : bool, default False\\n        Whether producing invalid utf8 data is allowed when casting.\\n    ', '__init__': <cyfunction CastOptions.__init__ at 0x000001FC1A532860>, 'safe': <staticmethod object at 0x000001FC28B4FF70>, 'unsafe': <staticmethod object at 0x000001FC28B4FE20>, '__dict__': <attribute '__dict__' of 'CastOptions' objects>})"


