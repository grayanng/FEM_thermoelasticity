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


from ._RandomOptions import _RandomOptions

class RandomOptions(_RandomOptions):
    """
    Options for random generation.
    
        Parameters
        ----------
        initializer : int or str
            How to initialize the underlying random generator.
            If an integer is given, it is used as a seed.
            If "system" is given, the random generator is initialized with
            a system-specific source of (hopefully true) randomness.
            Other values are invalid.
    """
    def __init__(self, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ RandomOptions.__init__(self, *, initializer=u'system') """
        pass

    __dict__ = None # (!) real value is 'mappingproxy({\'__module__\': \'pyarrow._compute\', \'__doc__\': \'\\n    Options for random generation.\\n\\n    Parameters\\n    ----------\\n    initializer : int or str\\n        How to initialize the underlying random generator.\\n        If an integer is given, it is used as a seed.\\n        If "system" is given, the random generator is initialized with\\n        a system-specific source of (hopefully true) randomness.\\n        Other values are invalid.\\n    \', \'__init__\': <cyfunction RandomOptions.__init__ at 0x000001FC28B91AD0>, \'__dict__\': <attribute \'__dict__\' of \'RandomOptions\' objects>})'


