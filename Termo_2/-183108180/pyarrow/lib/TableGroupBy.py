# encoding: utf-8
# module pyarrow.lib
# from C:\Users\akharin\PycharmProjects\pythonProject\venv\lib\site-packages\pyarrow\lib.cp39-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import datetime as datetime # C:\Users\akharin\AppData\Local\Programs\Python\Python39\lib\datetime.py
import decimal as _pydecimal # C:\Users\akharin\AppData\Local\Programs\Python\Python39\lib\decimal.py
import numpy as np # C:\Users\akharin\PycharmProjects\pythonProject\venv\lib\site-packages\numpy\__init__.py
import os as os # C:\Users\akharin\AppData\Local\Programs\Python\Python39\lib\os.py
import sys as sys # <module 'sys' (built-in)>
import pickle as builtin_pickle # C:\Users\akharin\AppData\Local\Programs\Python\Python39\lib\pickle.py
import pickle as pickle # C:\Users\akharin\AppData\Local\Programs\Python\Python39\lib\pickle.py
import signal as signal # C:\Users\akharin\AppData\Local\Programs\Python\Python39\lib\signal.py
import threading as threading # C:\Users\akharin\AppData\Local\Programs\Python\Python39\lib\threading.py
import warnings as warnings # C:\Users\akharin\AppData\Local\Programs\Python\Python39\lib\warnings.py
import atexit as atexit # <module 'atexit' (built-in)>
import re as re # C:\Users\akharin\AppData\Local\Programs\Python\Python39\lib\re.py
import collections as collections # C:\Users\akharin\AppData\Local\Programs\Python\Python39\lib\collections\__init__.py
import codecs as codecs # C:\Users\akharin\AppData\Local\Programs\Python\Python39\lib\codecs.py
import time as time # <module 'time' (built-in)>
from _queue import QueueEmpty

import collections.abc as __collections_abc
import enum as __enum
import importlib._bootstrap as __importlib__bootstrap
import io as __io
import _io as ___io


from .object import object

class TableGroupBy(object):
    """
    A grouping of columns in a table on which to perform aggregations.
    
        Parameters
        ----------
        table : pyarrow.Table
            Input table to execute the aggregation on.
        keys : str or list[str]
            Name of the grouped columns.
    
        Examples
        --------
        >>> import pyarrow as pa
        >>> t = pa.table([
        ...       pa.array(["a", "a", "b", "b", "c"]),
        ...       pa.array([1, 2, 3, 4, 5]),
        ... ], names=["keys", "values"])
    
        Grouping of columns:
    
        >>> pa.TableGroupBy(t,"keys")
        <pyarrow.lib.TableGroupBy object at ...>
    
        Perform aggregations:
    
        >>> pa.TableGroupBy(t,"keys").aggregate([("values", "sum")])
        pyarrow.Table
        values_sum: int64
        keys: string
        ----
        values_sum: [[3,7,5]]
        keys: [["a","b","c"]]
    """
    def aggregate(self, aggregations): # real signature unknown; restored from __doc__
        """
        TableGroupBy.aggregate(self, aggregations)
        
                Perform an aggregation over the grouped columns of the table.
        
                Parameters
                ----------
                aggregations : list[tuple(str, str)] or list[tuple(str, str, FunctionOptions)]
                    List of tuples made of aggregation column names followed
                    by function names and optionally aggregation function options.
                    Pass empty list to get a single row for each group.
        
                Returns
                -------
                Table
                    Results of the aggregation functions.
        
                Examples
                --------
                >>> import pyarrow as pa
                >>> t = pa.table([
                ...       pa.array(["a", "a", "b", "b", "c"]),
                ...       pa.array([1, 2, 3, 4, 5]),
                ... ], names=["keys", "values"])
                >>> t.group_by("keys").aggregate([("values", "sum")])
                pyarrow.Table
                values_sum: int64
                keys: string
                ----
                values_sum: [[3,7,5]]
                keys: [["a","b","c"]]
                >>> t.group_by("keys").aggregate([])
                pyarrow.Table
                keys: string
                ----
                keys: [["a","b","c"]]
        """
        pass

    def __init__(self, table, keys): # real signature unknown; restored from __doc__
        """ TableGroupBy.__init__(self, table, keys) """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is 'mappingproxy({\'__module__\': \'pyarrow.lib\', \'__doc__\': \'\\n    A grouping of columns in a table on which to perform aggregations.\\n\\n    Parameters\\n    ----------\\n    table : pyarrow.Table\\n        Input table to execute the aggregation on.\\n    keys : str or list[str]\\n        Name of the grouped columns.\\n\\n    Examples\\n    --------\\n    >>> import pyarrow as pa\\n    >>> t = pa.table([\\n    ...       pa.array(["a", "a", "b", "b", "c"]),\\n    ...       pa.array([1, 2, 3, 4, 5]),\\n    ... ], names=["keys", "values"])\\n\\n    Grouping of columns:\\n\\n    >>> pa.TableGroupBy(t,"keys")\\n    <pyarrow.lib.TableGroupBy object at ...>\\n\\n    Perform aggregations:\\n\\n    >>> pa.TableGroupBy(t,"keys").aggregate([("values", "sum")])\\n    pyarrow.Table\\n    values_sum: int64\\n    keys: string\\n    ----\\n    values_sum: [[3,7,5]]\\n    keys: [["a","b","c"]]\\n    \', \'__init__\': <cyfunction TableGroupBy.__init__ at 0x000001971BF9A110>, \'aggregate\': <cyfunction TableGroupBy.aggregate at 0x000001971BF9A2B0>, \'__dict__\': <attribute \'__dict__\' of \'TableGroupBy\' objects>, \'__weakref__\': <attribute \'__weakref__\' of \'TableGroupBy\' objects>})'


