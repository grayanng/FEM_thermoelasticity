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


from ._DayOfWeekOptions import _DayOfWeekOptions

class DayOfWeekOptions(_DayOfWeekOptions):
    """
    Options for the `day_of_week` function.
    
        Parameters
        ----------
        count_from_zero : bool, default True
            If True, number days from 0, otherwise from 1.
        week_start : int, default 1
            Which day does the week start with (Monday=1, Sunday=7).
            How this value is numbered is unaffected by `count_from_zero`.
    """
    def __init__(self, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ DayOfWeekOptions.__init__(self, *, count_from_zero=True, week_start=1) """
        pass

    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'pyarrow._compute', '__doc__': '\\n    Options for the `day_of_week` function.\\n\\n    Parameters\\n    ----------\\n    count_from_zero : bool, default True\\n        If True, number days from 0, otherwise from 1.\\n    week_start : int, default 1\\n        Which day does the week start with (Monday=1, Sunday=7).\\n        How this value is numbered is unaffected by `count_from_zero`.\\n    ', '__init__': <cyfunction DayOfWeekOptions.__init__ at 0x000001FC28B88E10>, '__dict__': <attribute '__dict__' of 'DayOfWeekOptions' objects>})"


