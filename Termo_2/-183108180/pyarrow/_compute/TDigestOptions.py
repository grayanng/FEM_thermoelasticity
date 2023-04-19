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


from ._TDigestOptions import _TDigestOptions

class TDigestOptions(_TDigestOptions):
    """
    Options for the `tdigest` function.
    
        Parameters
        ----------
        q : double or sequence of double, default 0.5
            Quantiles to approximate. All values must be in [0, 1].
        delta : int, default 100
            Compression parameter for the T-digest algorithm.
        buffer_size : int, default 500
            Buffer size for the T-digest algorithm.
        skip_nulls : bool, default True
            Whether to skip (ignore) nulls in the input.
            If False, any null in the input forces the output to null.
    
        min_count : int, default 0
            Minimum number of non-null values in the input.  If the number
            of non-null values is below `min_count`, the output is null.
    """
    def __init__(self, q=0.5, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ TDigestOptions.__init__(self, q=0.5, *, delta=100, buffer_size=500, skip_nulls=True, min_count=0) """
        pass

    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'pyarrow._compute', '__doc__': '\\n    Options for the `tdigest` function.\\n\\n    Parameters\\n    ----------\\n    q : double or sequence of double, default 0.5\\n        Quantiles to approximate. All values must be in [0, 1].\\n    delta : int, default 100\\n        Compression parameter for the T-digest algorithm.\\n    buffer_size : int, default 500\\n        Buffer size for the T-digest algorithm.\\n    skip_nulls : bool, default True\\n        Whether to skip (ignore) nulls in the input.\\n        If False, any null in the input forces the output to null.\\n\\n    min_count : int, default 0\\n        Minimum number of non-null values in the input.  If the number\\n        of non-null values is below `min_count`, the output is null.\\n\\n    ', '__init__': <cyfunction TDigestOptions.__init__ at 0x000001FC28B91930>, '__dict__': <attribute '__dict__' of 'TDigestOptions' objects>})"


