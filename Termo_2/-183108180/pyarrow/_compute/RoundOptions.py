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


from ._RoundOptions import _RoundOptions

class RoundOptions(_RoundOptions):
    """
    Options for rounding numbers.
    
        Parameters
        ----------
        ndigits : int, default 0
            Number of fractional digits to round to.
        round_mode : str, default "half_to_even"
            Rounding and tie-breaking mode.
            Accepted values are "down", "up", "towards_zero", "towards_infinity",
            "half_down", "half_up", "half_towards_zero", "half_towards_infinity",
            "half_to_even", "half_to_odd".
    """
    def __init__(self, ndigits=0, round_mode=None): # real signature unknown; restored from __doc__
        """ RoundOptions.__init__(self, ndigits=0, round_mode=u'half_to_even') """
        pass

    __dict__ = None # (!) real value is 'mappingproxy({\'__module__\': \'pyarrow._compute\', \'__doc__\': \'\\n    Options for rounding numbers.\\n\\n    Parameters\\n    ----------\\n    ndigits : int, default 0\\n        Number of fractional digits to round to.\\n    round_mode : str, default "half_to_even"\\n        Rounding and tie-breaking mode.\\n        Accepted values are "down", "up", "towards_zero", "towards_infinity",\\n        "half_down", "half_up", "half_towards_zero", "half_towards_infinity",\\n        "half_to_even", "half_to_odd".\\n    \', \'__init__\': <cyfunction RoundOptions.__init__ at 0x000001FC28B1A930>, \'__dict__\': <attribute \'__dict__\' of \'RoundOptions\' objects>})'


