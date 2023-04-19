# encoding: utf-8
# module pyarrow._hdfsio
# from C:\Users\akharin\PycharmProjects\pythonProject\venv\lib\site-packages\pyarrow\_hdfsio.cp39-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import re as re # C:\Users\akharin\AppData\Local\Programs\Python\Python39\lib\re.py
from pyarrow.lib import frombytes, tobytes

from _queue import QueueEmpty

import pyarrow.lib as __pyarrow_lib


# functions

def have_libhdfs(): # real signature unknown; restored from __doc__
    """ have_libhdfs() """
    pass

def strip_hdfs_abspath(path): # real signature unknown; restored from __doc__
    """ strip_hdfs_abspath(path) """
    pass

# classes

class ArrowIOError(Exception):
    """ Base class for I/O related errors. """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    characters_written = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    errno = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """POSIX exception code"""

    filename = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """exception filename"""

    filename2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """second exception filename"""

    strerror = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """exception strerror"""

    winerror = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Win32 exception code"""



class HadoopFileSystem(__pyarrow_lib._Weakrefable):
    # no doc
    def chmod(self, path, mode): # real signature unknown; restored from __doc__
        """
        HadoopFileSystem.chmod(self, path, mode)
        
                Change file permissions
        
                Parameters
                ----------
                path : string
                    absolute path to file or directory
                mode : int
                    POSIX-like bitmask
        """
        pass

    def chown(self, path, owner=None, group=None): # real signature unknown; restored from __doc__
        """
        HadoopFileSystem.chown(self, path, owner=None, group=None)
        
                Change file permissions
        
                Parameters
                ----------
                path : string
                    absolute path to file or directory
                owner : string, default None
                    New owner, None for no change
                group : string, default None
                    New group, None for no change
        """
        pass

    def close(self): # real signature unknown; restored from __doc__
        """
        HadoopFileSystem.close(self)
        
                Disconnect from the HDFS cluster
        """
        pass

    @classmethod
    def connect(cls, type_cls, *args, **kwargs): # real signature unknown; restored from __doc__
        """ HadoopFileSystem.connect(type cls, *args, **kwargs) """
        pass

    def delete(self, path, bool_recursive=False): # real signature unknown; restored from __doc__
        """
        HadoopFileSystem.delete(self, path, bool recursive=False)
        
                Delete the indicated file or directory
        
                Parameters
                ----------
                path : string
                recursive : boolean, default False
                    If True, also delete child paths for directories
        """
        pass

    def df(self): # real signature unknown; restored from __doc__
        """
        HadoopFileSystem.df(self)
        
                Return free space on disk, like the UNIX df command
        
                Returns
                -------
                space : int
        """
        pass

    def download(self, path, stream, buffer_size=None): # real signature unknown; restored from __doc__
        """ HadoopFileSystem.download(self, path, stream, buffer_size=None) """
        pass

    def exists(self, path): # real signature unknown; restored from __doc__
        """
        HadoopFileSystem.exists(self, path)
        
                Returns True if the path is known to the cluster, False if it does not
                (or there is an RPC error)
        """
        pass

    def get_capacity(self): # real signature unknown; restored from __doc__
        """
        HadoopFileSystem.get_capacity(self)
        
                Get reported total capacity of file system
        
                Returns
                -------
                capacity : int
        """
        pass

    def get_space_used(self): # real signature unknown; restored from __doc__
        """
        HadoopFileSystem.get_space_used(self)
        
                Get space used on file system
        
                Returns
                -------
                space_used : int
        """
        pass

    def info(self, path): # real signature unknown; restored from __doc__
        """
        HadoopFileSystem.info(self, path)
        
                Return detailed HDFS information for path
        
                Parameters
                ----------
                path : string
                    Path to file or directory
        
                Returns
                -------
                path_info : dict
        """
        pass

    def isdir(self, path): # real signature unknown; restored from __doc__
        """ HadoopFileSystem.isdir(self, path) """
        pass

    def isfile(self, path): # real signature unknown; restored from __doc__
        """ HadoopFileSystem.isfile(self, path) """
        pass

    def ls(self, path, bool_full_info): # real signature unknown; restored from __doc__
        """ HadoopFileSystem.ls(self, path, bool full_info) """
        pass

    def mkdir(self, path): # real signature unknown; restored from __doc__
        """
        HadoopFileSystem.mkdir(self, path)
        
                Create indicated directory and any necessary parent directories
        """
        pass

    def open(self, path, mode=None, buffer_size=None, replication=None, default_block_size=None): # real signature unknown; restored from __doc__
        """
        HadoopFileSystem.open(self, path, mode=u'rb', buffer_size=None, replication=None, default_block_size=None)
        
                Open HDFS file for reading or writing
        
                Parameters
                ----------
                mode : string
                    Must be one of 'rb', 'wb', 'ab'
        
                Returns
                -------
                handle : HdfsFile
        """
        pass

    def rename(self, path, new_path): # real signature unknown; restored from __doc__
        """ HadoopFileSystem.rename(self, path, new_path) """
        pass

    def stat(self, path): # real signature unknown; restored from __doc__
        """
        HadoopFileSystem.stat(self, path)
        
                Return basic file system statistics about path
        
                Parameters
                ----------
                path : string
                    Path to file or directory
        
                Returns
                -------
                stat : dict
        """
        pass

    def upload(self, path, stream, buffer_size=None): # real signature unknown; restored from __doc__
        """
        HadoopFileSystem.upload(self, path, stream, buffer_size=None)
        
                Upload file-like object to HDFS path
        """
        pass

    def _connect(self, host, port, user, kerb_ticket, extra_conf): # real signature unknown; restored from __doc__
        """ HadoopFileSystem._connect(self, host, port, user, kerb_ticket, extra_conf) """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ HadoopFileSystem.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ HadoopFileSystem.__setstate_cython__(self, __pyx_state) """
        pass

    extra_conf = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    host = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_open = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    kerb_ticket = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    port = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    user = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001D3DC37F270>'


class HdfsFile(__pyarrow_lib.NativeFile):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ HdfsFile.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ HdfsFile.__setstate_cython__(self, __pyx_state) """
        pass

    buffer_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    mode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001D3DC37F1E0>'


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


    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'queue', '__doc__': 'Create a queue object with a given maximum size.\\n\\n    If maxsize is <= 0, the queue size is infinite.\\n    ', '__init__': <function Queue.__init__ at 0x000001D3EA959CA0>, 'task_done': <function Queue.task_done at 0x000001D3EA959D30>, 'join': <function Queue.join at 0x000001D3EA959DC0>, 'qsize': <function Queue.qsize at 0x000001D3EA959E50>, 'empty': <function Queue.empty at 0x000001D3EA959EE0>, 'full': <function Queue.full at 0x000001D3EA959F70>, 'put': <function Queue.put at 0x000001D3EA96B040>, 'get': <function Queue.get at 0x000001D3EA96B0D0>, 'put_nowait': <function Queue.put_nowait at 0x000001D3EA96B160>, 'get_nowait': <function Queue.get_nowait at 0x000001D3EA96B1F0>, '_init': <function Queue._init at 0x000001D3EA96B280>, '_qsize': <function Queue._qsize at 0x000001D3EA96B310>, '_put': <function Queue._put at 0x000001D3EA96B3A0>, '_get': <function Queue._get at 0x000001D3EA96B430>, '__class_getitem__': <classmethod object at 0x000001D3EA9690D0>, '__dict__': <attribute '__dict__' of 'Queue' objects>, '__weakref__': <attribute '__weakref__' of 'Queue' objects>})"


class QueueFull(Exception):
    """ Exception raised by Queue.put(block=0)/put_nowait(). """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class _HdfsFileNanny(__pyarrow_lib._Weakrefable):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ _HdfsFileNanny.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ _HdfsFileNanny.__setstate_cython__(self, __pyx_state) """
        pass


# variables with complex values

_HDFS_PATH_RE = None # (!) real value is "re.compile('hdfs://(.*):(\\\\d+)(.*)')"

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x000001D3DC37F550>'

__spec__ = None # (!) real value is "ModuleSpec(name='pyarrow._hdfsio', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x000001D3DC37F550>, origin='C:\\\\Users\\\\akharin\\\\PycharmProjects\\\\pythonProject\\\\venv\\\\lib\\\\site-packages\\\\pyarrow\\\\_hdfsio.cp39-win_amd64.pyd')"

__test__ = {}

