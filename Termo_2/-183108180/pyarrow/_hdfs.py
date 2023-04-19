# encoding: utf-8
# module pyarrow._hdfs
# from C:\Users\akharin\PycharmProjects\pythonProject\venv\lib\site-packages\pyarrow\_hdfs.cp39-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
from pyarrow.lib import frombytes, tobytes

import pyarrow._fs as __pyarrow__fs


# functions

def _stringify_path(path): # reliably restored by inspect
    """ Convert *path* to a string or unicode path if possible. """
    pass

# classes

class HadoopFileSystem(__pyarrow__fs.FileSystem):
    """
    HadoopFileSystem(unicode host, int port=8020, unicode user=None, *, int replication=3, int buffer_size=0, default_block_size=None, kerb_ticket=None, extra_conf=None)
    
        HDFS backed FileSystem implementation
    
        Parameters
        ----------
        host : str
            HDFS host to connect to. Set to "default" for fs.defaultFS from
            core-site.xml.
        port : int, default 8020
            HDFS port to connect to. Set to 0 for default or logical (HA) nodes.
        user : str, default None
            Username when connecting to HDFS; None implies login user.
        replication : int, default 3
            Number of copies each block will have.
        buffer_size : int, default 0
            If 0, no buffering will happen otherwise the size of the temporary read
            and write buffer.
        default_block_size : int, default None
            None means the default configuration for HDFS, a typical block size is
            128 MB.
        kerb_ticket : string or path, default None
            If not None, the path to the Kerberos ticket cache.
        extra_conf : dict, default None
            Extra key/value pairs for configuration; will override any
            hdfs-site.xml properties.
    
        Examples
        --------
        >>> from pyarrow import fs
        >>> hdfs = fs.HadoopFileSystem(host, port, user=user, kerb_ticket=ticket_cache_path) # doctest: +SKIP
    
        For usage of the methods see examples for :func:`~pyarrow.fs.LocalFileSystem`.
    """
    def from_uri(self, uri): # real signature unknown; restored from __doc__
        """
        HadoopFileSystem.from_uri(uri)
        
                Instantiate HadoopFileSystem object from an URI string.
        
                The following two calls are equivalent
        
                * ``HadoopFileSystem.from_uri('hdfs://localhost:8020/?user=test&replication=1')``
                * ``HadoopFileSystem('localhost', port=8020, user='test', replication=1)``
        
                Parameters
                ----------
                uri : str
                    A string URI describing the connection to HDFS.
                    In order to change the user, replication, buffer_size or
                    default_block_size pass the values as query parts.
        
                Returns
                -------
                HadoopFileSystem
        """
        pass

    @classmethod
    def _reconstruct(cls, type_cls, kwargs): # real signature unknown; restored from __doc__
        """ HadoopFileSystem._reconstruct(type cls, kwargs) """
        pass

    def __init__(self, unicode_host, int_port=8020, unicode_user=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self): # real signature unknown; restored from __doc__
        """ HadoopFileSystem.__reduce__(self) """
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001B42E4AF2D0>'


# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x000001B42E4BA910>'

__spec__ = None # (!) real value is "ModuleSpec(name='pyarrow._hdfs', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x000001B42E4BA910>, origin='C:\\\\Users\\\\akharin\\\\PycharmProjects\\\\pythonProject\\\\venv\\\\lib\\\\site-packages\\\\pyarrow\\\\_hdfs.cp39-win_amd64.pyd')"

__test__ = {}

