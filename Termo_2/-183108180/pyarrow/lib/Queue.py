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

class Queue(object):
    """
    Create a queue object with a given maximum size.
    
        If maxsize is <= 0, the queue size is infinite.
    """
    def empty(self): # reliably restored by inspect
        """
        Return True if the queue is empty, False otherwise (not reliable!).
        
                This method is likely to be removed at some point.  Use qsize() == 0
                as a direct substitute, but be aware that either approach risks a race
                condition where a queue can grow before the result of empty() or
                qsize() can be used.
        
                To create code that needs to wait for all queued tasks to be
                completed, the preferred technique is to use the join() method.
        """
        pass

    def full(self): # reliably restored by inspect
        """
        Return True if the queue is full, False otherwise (not reliable!).
        
                This method is likely to be removed at some point.  Use qsize() >= n
                as a direct substitute, but be aware that either approach risks a race
                condition where a queue can shrink before the result of full() or
                qsize() can be used.
        """
        pass

    def get(self, block=True, timeout=None): # reliably restored by inspect
        """
        Remove and return an item from the queue.
        
                If optional args 'block' is true and 'timeout' is None (the default),
                block if necessary until an item is available. If 'timeout' is
                a non-negative number, it blocks at most 'timeout' seconds and raises
                the Empty exception if no item was available within that time.
                Otherwise ('block' is false), return an item if one is immediately
                available, else raise the Empty exception ('timeout' is ignored
                in that case).
        """
        pass

    def get_nowait(self): # reliably restored by inspect
        """
        Remove and return an item from the queue without blocking.
        
                Only get an item if one is immediately available. Otherwise
                raise the Empty exception.
        """
        pass

    def join(self): # reliably restored by inspect
        """
        Blocks until all items in the Queue have been gotten and processed.
        
                The count of unfinished tasks goes up whenever an item is added to the
                queue. The count goes down whenever a consumer thread calls task_done()
                to indicate the item was retrieved and all work on it is complete.
        
                When the count of unfinished tasks drops to zero, join() unblocks.
        """
        pass

    def put(self, item, block=True, timeout=None): # reliably restored by inspect
        """
        Put an item into the queue.
        
                If optional args 'block' is true and 'timeout' is None (the default),
                block if necessary until a free slot is available. If 'timeout' is
                a non-negative number, it blocks at most 'timeout' seconds and raises
                the Full exception if no free slot was available within that time.
                Otherwise ('block' is false), put an item on the queue if a free slot
                is immediately available, else raise the Full exception ('timeout'
                is ignored in that case).
        """
        pass

    def put_nowait(self, item): # reliably restored by inspect
        """
        Put an item into the queue without blocking.
        
                Only enqueue the item if a free slot is immediately available.
                Otherwise raise the Full exception.
        """
        pass

    def qsize(self): # reliably restored by inspect
        """ Return the approximate size of the queue (not reliable!). """
        pass

    def task_done(self): # reliably restored by inspect
        """
        Indicate that a formerly enqueued task is complete.
        
                Used by Queue consumer threads.  For each get() used to fetch a task,
                a subsequent call to task_done() tells the queue that the processing
                on the task is complete.
        
                If a join() is currently blocking, it will resume when all items
                have been processed (meaning that a task_done() call was received
                for every item that had been put() into the queue).
        
                Raises a ValueError if called more times than there were items
                placed in the queue.
        """
        pass

    def _get(self): # reliably restored by inspect
        # no doc
        pass

    def _init(self, maxsize): # reliably restored by inspect
        # no doc
        pass

    def _put(self, item): # reliably restored by inspect
        # no doc
        pass

    def _qsize(self): # reliably restored by inspect
        # no doc
        pass

    @classmethod
    def __class_getitem__(cls, *args, **kwargs): # real signature unknown
        """
        Represent a PEP 585 generic type
        
        E.g. for t = list[int], t.__origin__ is list and t.__args__ is (int,).
        """
        pass

    def __init__(self, maxsize=0): # reliably restored by inspect
        # no doc
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'queue', '__doc__': 'Create a queue object with a given maximum size.\\n\\n    If maxsize is <= 0, the queue size is infinite.\\n    ', '__init__': <function Queue.__init__ at 0x000001971BF99C10>, 'task_done': <function Queue.task_done at 0x000001971BF99CA0>, 'join': <function Queue.join at 0x000001971BF99D30>, 'qsize': <function Queue.qsize at 0x000001971BF99DC0>, 'empty': <function Queue.empty at 0x000001971BF99E50>, 'full': <function Queue.full at 0x000001971BF99EE0>, 'put': <function Queue.put at 0x000001971BF99F70>, 'get': <function Queue.get at 0x000001971BFAB040>, 'put_nowait': <function Queue.put_nowait at 0x000001971BFAB0D0>, 'get_nowait': <function Queue.get_nowait at 0x000001971BFAB160>, '_init': <function Queue._init at 0x000001971BFAB1F0>, '_qsize': <function Queue._qsize at 0x000001971BFAB280>, '_put': <function Queue._put at 0x000001971BFAB310>, '_get': <function Queue._get at 0x000001971BFAB3A0>, '__class_getitem__': <classmethod object at 0x000001971BFA3FD0>, '__dict__': <attribute '__dict__' of 'Queue' objects>, '__weakref__': <attribute '__weakref__' of 'Queue' objects>})"


