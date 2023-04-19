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


from ._AssumeTimezoneOptions import _AssumeTimezoneOptions

class AssumeTimezoneOptions(_AssumeTimezoneOptions):
    """
    Options for the `assume_timezone` function.
    
        Parameters
        ----------
        timezone : str
            Timezone to assume for the input.
        ambiguous : str, default "raise"
            How to handle timestamps that are ambiguous in the assumed timezone.
            Accepted values are "raise", "earliest", "latest".
        nonexistent : str, default "raise"
            How to handle timestamps that don't exist in the assumed timezone.
            Accepted values are "raise", "earliest", "latest".
    """
    def __init__(self, timezone, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ AssumeTimezoneOptions.__init__(self, timezone, *, ambiguous=u'raise', nonexistent=u'raise') """
        pass

    __dict__ = None # (!) real value is 'mappingproxy({\'__module__\': \'pyarrow._compute\', \'__doc__\': \'\\n    Options for the `assume_timezone` function.\\n\\n    Parameters\\n    ----------\\n    timezone : str\\n        Timezone to assume for the input.\\n    ambiguous : str, default "raise"\\n        How to handle timestamps that are ambiguous in the assumed timezone.\\n        Accepted values are "raise", "earliest", "latest".\\n    nonexistent : str, default "raise"\\n        How to handle timestamps that don\\\'t exist in the assumed timezone.\\n        Accepted values are "raise", "earliest", "latest".\\n    \', \'__init__\': <cyfunction AssumeTimezoneOptions.__init__ at 0x000001FC28B91040>, \'__dict__\': <attribute \'__dict__\' of \'AssumeTimezoneOptions\' objects>})'


