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


from ._WeekOptions import _WeekOptions

class WeekOptions(_WeekOptions):
    """
    Options for the `week` function.
    
        Parameters
        ----------
        week_starts_monday : bool, default True
            If True, weeks start on Monday; if False, on Sunday.
        count_from_zero : bool, default False
            If True, dates at the start of a year that fall into the last week
            of the previous year emit 0.
            If False, they emit 52 or 53 (the week number of the last week
            of the previous year).
        first_week_is_fully_in_year : bool, default False
            If True, week number 0 is fully in January.
            If False, a week that begins on December 29, 30 or 31 is considered
            to be week number 0 of the following year.
    """
    def __init__(self, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ WeekOptions.__init__(self, *, week_starts_monday=True, count_from_zero=False, first_week_is_fully_in_year=False) """
        pass

    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'pyarrow._compute', '__doc__': '\\n    Options for the `week` function.\\n\\n    Parameters\\n    ----------\\n    week_starts_monday : bool, default True\\n        If True, weeks start on Monday; if False, on Sunday.\\n    count_from_zero : bool, default False\\n        If True, dates at the start of a year that fall into the last week\\n        of the previous year emit 0.\\n        If False, they emit 52 or 53 (the week number of the last week\\n        of the previous year).\\n    first_week_is_fully_in_year : bool, default False\\n        If True, week number 0 is fully in January.\\n        If False, a week that begins on December 29, 30 or 31 is considered\\n        to be week number 0 of the following year.\\n    ', '__init__': <cyfunction WeekOptions.__init__ at 0x000001FC28B88EE0>, '__dict__': <attribute '__dict__' of 'WeekOptions' objects>})"


