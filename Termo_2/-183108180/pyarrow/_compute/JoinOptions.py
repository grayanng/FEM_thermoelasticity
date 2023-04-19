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


from ._JoinOptions import _JoinOptions

class JoinOptions(_JoinOptions):
    """
    Options for the `binary_join_element_wise` function.
    
        Parameters
        ----------
        null_handling : str, default "emit_null"
            How to handle null values in the inputs.
            Accepted values are "emit_null", "skip", "replace".
        null_replacement : str, default ""
            Replacement string to emit for null inputs if `null_handling`
            is "replace".
    """
    def __init__(self, null_handling=None, null_replacement=None): # real signature unknown; restored from __doc__
        """ JoinOptions.__init__(self, null_handling=u'emit_null', null_replacement=u'') """
        pass

    __dict__ = None # (!) real value is 'mappingproxy({\'__module__\': \'pyarrow._compute\', \'__doc__\': \'\\n    Options for the `binary_join_element_wise` function.\\n\\n    Parameters\\n    ----------\\n    null_handling : str, default "emit_null"\\n        How to handle null values in the inputs.\\n        Accepted values are "emit_null", "skip", "replace".\\n    null_replacement : str, default ""\\n        Replacement string to emit for null inputs if `null_handling`\\n        is "replace".\\n    \', \'__init__\': <cyfunction JoinOptions.__init__ at 0x000001FC28B1ABA0>, \'__dict__\': <attribute \'__dict__\' of \'JoinOptions\' objects>})'


