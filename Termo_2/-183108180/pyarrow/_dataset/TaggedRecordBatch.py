# encoding: utf-8
# module pyarrow._dataset
# from C:\Users\akharin\PycharmProjects\pythonProject\venv\lib\site-packages\pyarrow\_dataset.cp39-win_amd64.pyd
# by generator 1.147
""" Dataset is currently unstable. APIs subject to change without notice. """

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import codecs as codecs # C:\Users\akharin\AppData\Local\Programs\Python\Python39\lib\codecs.py
import collections as collections # C:\Users\akharin\AppData\Local\Programs\Python\Python39\lib\collections\__init__.py
import os as os # C:\Users\akharin\AppData\Local\Programs\Python\Python39\lib\os.py
import warnings as warnings # C:\Users\akharin\AppData\Local\Programs\Python\Python39\lib\warnings.py
import pyarrow as pa # C:\Users\akharin\PycharmProjects\pythonProject\venv\lib\site-packages\pyarrow\__init__.py
from pyarrow.lib import ArrowTypeError, _pc, frombytes, tobytes

import importlib._bootstrap as __importlib__bootstrap
import pyarrow.lib as __pyarrow_lib


class TaggedRecordBatch(__importlib__bootstrap.TaggedRecordBatch):
    """
    A combination of a record batch and the fragment it came from.
    
        Parameters
        ----------
        record_batch : RecordBatch
            The record batch.
        fragment : Fragment
            Fragment of the record batch.
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'pyarrow._dataset', '__doc__': '\\n    A combination of a record batch and the fragment it came from.\\n\\n    Parameters\\n    ----------\\n    record_batch : RecordBatch\\n        The record batch.\\n    fragment : Fragment\\n        Fragment of the record batch.\\n    ', '__dict__': <attribute '__dict__' of 'TaggedRecordBatch' objects>})"


