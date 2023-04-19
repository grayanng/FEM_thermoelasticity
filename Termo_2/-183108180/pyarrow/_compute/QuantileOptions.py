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


from ._QuantileOptions import _QuantileOptions

class QuantileOptions(_QuantileOptions):
    """
    Options for the `quantile` function.
    
        Parameters
        ----------
        q : double or sequence of double, default 0.5
            Quantiles to compute. All values must be in [0, 1].
        interpolation : str, default "linear"
            How to break ties between competing data points for a given quantile.
            Accepted values are:
    
            - "linear": compute an interpolation
            - "lower": always use the smallest of the two data points
            - "higher": always use the largest of the two data points
            - "nearest": select the data point that is closest to the quantile
            - "midpoint": compute the (unweighted) mean of the two data points
        skip_nulls : bool, default True
            Whether to skip (ignore) nulls in the input.
            If False, any null in the input forces the output to null.
    
        min_count : int, default 0
            Minimum number of non-null values in the input.  If the number
            of non-null values is below `min_count`, the output is null.
    """
    def __init__(self, q=0.5, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QuantileOptions.__init__(self, q=0.5, *, interpolation=u'linear', skip_nulls=True, min_count=0) """
        pass

    __dict__ = None # (!) real value is 'mappingproxy({\'__module__\': \'pyarrow._compute\', \'__doc__\': \'\\n    Options for the `quantile` function.\\n\\n    Parameters\\n    ----------\\n    q : double or sequence of double, default 0.5\\n        Quantiles to compute. All values must be in [0, 1].\\n    interpolation : str, default "linear"\\n        How to break ties between competing data points for a given quantile.\\n        Accepted values are:\\n\\n        - "linear": compute an interpolation\\n        - "lower": always use the smallest of the two data points\\n        - "higher": always use the largest of the two data points\\n        - "nearest": select the data point that is closest to the quantile\\n        - "midpoint": compute the (unweighted) mean of the two data points\\n    skip_nulls : bool, default True\\n        Whether to skip (ignore) nulls in the input.\\n        If False, any null in the input forces the output to null.\\n\\n    min_count : int, default 0\\n        Minimum number of non-null values in the input.  If the number\\n        of non-null values is below `min_count`, the output is null.\\n\\n    \', \'__init__\': <cyfunction QuantileOptions.__init__ at 0x000001FC28B91860>, \'__dict__\': <attribute \'__dict__\' of \'QuantileOptions\' objects>})'


