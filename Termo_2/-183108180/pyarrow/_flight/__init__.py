# encoding: utf-8
# module pyarrow._flight
# from C:\Users\akharin\PycharmProjects\pythonProject\venv\lib\site-packages\pyarrow\_flight.cp39-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import collections as collections # C:\Users\akharin\AppData\Local\Programs\Python\Python39\lib\collections\__init__.py
import contextlib as contextlib # C:\Users\akharin\AppData\Local\Programs\Python\Python39\lib\contextlib.py
import enum as enum # C:\Users\akharin\AppData\Local\Programs\Python\Python39\lib\enum.py
import re as re # C:\Users\akharin\AppData\Local\Programs\Python\Python39\lib\re.py
import socket as socket # C:\Users\akharin\AppData\Local\Programs\Python\Python39\lib\socket.py
import time as time # <module 'time' (built-in)>
import threading as threading # C:\Users\akharin\AppData\Local\Programs\Python\Python39\lib\threading.py
import warnings as warnings # C:\Users\akharin\AppData\Local\Programs\Python\Python39\lib\warnings.py
import weakref as weakref # C:\Users\akharin\AppData\Local\Programs\Python\Python39\lib\weakref.py
import pyarrow.lib as lib # C:\Users\akharin\PycharmProjects\pythonProject\venv\lib\site-packages\pyarrow\lib.cp39-win_amd64.pyd
from pyarrow.lib import (ArrowCancelled, ArrowException, ArrowInvalid, 
    SignalStopHandler, _ReadPandasMixin, as_buffer, frombytes, tobytes)

import enum as __enum
import importlib._bootstrap as __importlib__bootstrap
import pyarrow.lib as __pyarrow_lib


# functions

def connect(location, **kwargs): # real signature unknown; restored from __doc__
    """
    connect(location, **kwargs)
    
        Connect to a Flight server.
    
        Parameters
        ----------
        location : str, tuple, or Location
            Location to connect to. Either a URI like "grpc://localhost:port",
            a tuple of (host, port), or a Location instance.
        tls_root_certs : bytes or None
            PEM-encoded.
        cert_chain: str or None
            If provided, enables TLS mutual authentication.
        private_key: str or None
            If provided, enables TLS mutual authentication.
        override_hostname : str or None
            Override the hostname checked by TLS. Insecure, use with caution.
        middleware : list or None
            A list of ClientMiddlewareFactory instances to apply.
        write_size_limit_bytes : int or None
            A soft limit on the size of a data payload sent to the
            server. Enabled if positive. If enabled, writing a record
            batch that (when serialized) exceeds this limit will raise an
            exception; the client can retry the write with a smaller
            batch.
        disable_server_verification : boolean or None
            Disable verifying the server when using TLS.
            Insecure, use with caution.
        generic_options : list or None
            A list of generic (string, int or string) options to pass to
            the underlying transport.
    
        Returns
        -------
        client : FlightClient
    """
    pass

def _get_legacy_format_default(use_legacy_format, options): # reliably restored by inspect
    # no doc
    pass

def _munge_grpc_python_error(message): # real signature unknown; restored from __doc__
    """ _munge_grpc_python_error(message) """
    pass

def __pyx_unpickle_ClientAuthHandler(__pyx_type, long___pyx_checksum, __pyx_state): # real signature unknown; restored from __doc__
    """ __pyx_unpickle_ClientAuthHandler(__pyx_type, long __pyx_checksum, __pyx_state) """
    pass

def __pyx_unpickle_ClientMiddleware(__pyx_type, long___pyx_checksum, __pyx_state): # real signature unknown; restored from __doc__
    """ __pyx_unpickle_ClientMiddleware(__pyx_type, long __pyx_checksum, __pyx_state) """
    pass

def __pyx_unpickle_ClientMiddlewareFactory(__pyx_type, long___pyx_checksum, __pyx_state): # real signature unknown; restored from __doc__
    """ __pyx_unpickle_ClientMiddlewareFactory(__pyx_type, long __pyx_checksum, __pyx_state) """
    pass

def __pyx_unpickle_FlightCancelledError(__pyx_type, long___pyx_checksum, __pyx_state): # real signature unknown; restored from __doc__
    """ __pyx_unpickle_FlightCancelledError(__pyx_type, long __pyx_checksum, __pyx_state) """
    pass

def __pyx_unpickle_FlightDataStream(__pyx_type, long___pyx_checksum, __pyx_state): # real signature unknown; restored from __doc__
    """ __pyx_unpickle_FlightDataStream(__pyx_type, long __pyx_checksum, __pyx_state) """
    pass

def __pyx_unpickle_FlightError(__pyx_type, long___pyx_checksum, __pyx_state): # real signature unknown; restored from __doc__
    """ __pyx_unpickle_FlightError(__pyx_type, long __pyx_checksum, __pyx_state) """
    pass

def __pyx_unpickle_FlightInternalError(__pyx_type, long___pyx_checksum, __pyx_state): # real signature unknown; restored from __doc__
    """ __pyx_unpickle_FlightInternalError(__pyx_type, long __pyx_checksum, __pyx_state) """
    pass

def __pyx_unpickle_FlightServerError(__pyx_type, long___pyx_checksum, __pyx_state): # real signature unknown; restored from __doc__
    """ __pyx_unpickle_FlightServerError(__pyx_type, long __pyx_checksum, __pyx_state) """
    pass

def __pyx_unpickle_FlightTimedOutError(__pyx_type, long___pyx_checksum, __pyx_state): # real signature unknown; restored from __doc__
    """ __pyx_unpickle_FlightTimedOutError(__pyx_type, long __pyx_checksum, __pyx_state) """
    pass

def __pyx_unpickle_FlightUnauthenticatedError(__pyx_type, long___pyx_checksum, __pyx_state): # real signature unknown; restored from __doc__
    """ __pyx_unpickle_FlightUnauthenticatedError(__pyx_type, long __pyx_checksum, __pyx_state) """
    pass

def __pyx_unpickle_FlightUnauthorizedError(__pyx_type, long___pyx_checksum, __pyx_state): # real signature unknown; restored from __doc__
    """ __pyx_unpickle_FlightUnauthorizedError(__pyx_type, long __pyx_checksum, __pyx_state) """
    pass

def __pyx_unpickle_FlightUnavailableError(__pyx_type, long___pyx_checksum, __pyx_state): # real signature unknown; restored from __doc__
    """ __pyx_unpickle_FlightUnavailableError(__pyx_type, long __pyx_checksum, __pyx_state) """
    pass

def __pyx_unpickle_ServerAuthHandler(__pyx_type, long___pyx_checksum, __pyx_state): # real signature unknown; restored from __doc__
    """ __pyx_unpickle_ServerAuthHandler(__pyx_type, long __pyx_checksum, __pyx_state) """
    pass

def __pyx_unpickle_ServerMiddleware(__pyx_type, long___pyx_checksum, __pyx_state): # real signature unknown; restored from __doc__
    """ __pyx_unpickle_ServerMiddleware(__pyx_type, long __pyx_checksum, __pyx_state) """
    pass

def __pyx_unpickle_ServerMiddlewareFactory(__pyx_type, long___pyx_checksum, __pyx_state): # real signature unknown; restored from __doc__
    """ __pyx_unpickle_ServerMiddlewareFactory(__pyx_type, long __pyx_checksum, __pyx_state) """
    pass

def __pyx_unpickle_TracingServerMiddlewareFactory(__pyx_type, long___pyx_checksum, __pyx_state): # real signature unknown; restored from __doc__
    """ __pyx_unpickle_TracingServerMiddlewareFactory(__pyx_type, long __pyx_checksum, __pyx_state) """
    pass

def __pyx_unpickle__ServerMiddlewareFactoryWrapper(__pyx_type, long___pyx_checksum, __pyx_state): # real signature unknown; restored from __doc__
    """ __pyx_unpickle__ServerMiddlewareFactoryWrapper(__pyx_type, long __pyx_checksum, __pyx_state) """
    pass

def __pyx_unpickle__ServerMiddlewareWrapper(__pyx_type, long___pyx_checksum, __pyx_state): # real signature unknown; restored from __doc__
    """ __pyx_unpickle__ServerMiddlewareWrapper(__pyx_type, long __pyx_checksum, __pyx_state) """
    pass

# classes

from .Action import Action
from ._ActionType import _ActionType
from .ActionType import ActionType
from .BasicAuth import BasicAuth
from ._CallInfo import _CallInfo
from .CallInfo import CallInfo
from ._CertKeyPair import _CertKeyPair
from .CertKeyPair import CertKeyPair
from .ClientAuthHandler import ClientAuthHandler
from .ClientAuthReader import ClientAuthReader
from .ClientAuthSender import ClientAuthSender
from .ClientMiddleware import ClientMiddleware
from .ClientMiddlewareFactory import ClientMiddlewareFactory
from .DescriptorType import DescriptorType
from .FlightCallOptions import FlightCallOptions
from .FlightError import FlightError
from .FlightCancelledError import FlightCancelledError
from .FlightClient import FlightClient
from .FlightDataStream import FlightDataStream
from .FlightDescriptor import FlightDescriptor
from .FlightEndpoint import FlightEndpoint
from .FlightInfo import FlightInfo
from .FlightInternalError import FlightInternalError
from .FlightMetadataReader import FlightMetadataReader
from .FlightMetadataWriter import FlightMetadataWriter
from .FlightMethod import FlightMethod
from .FlightServerBase import FlightServerBase
from .FlightServerError import FlightServerError
from .FlightStreamChunk import FlightStreamChunk
from ._MetadataRecordBatchReader import _MetadataRecordBatchReader
from .MetadataRecordBatchReader import MetadataRecordBatchReader
from .FlightStreamReader import FlightStreamReader
from .MetadataRecordBatchWriter import MetadataRecordBatchWriter
from .FlightStreamWriter import FlightStreamWriter
from .FlightTimedOutError import FlightTimedOutError
from .FlightUnauthenticatedError import FlightUnauthenticatedError
from .FlightUnauthorizedError import FlightUnauthorizedError
from .FlightUnavailableError import FlightUnavailableError
from .FlightWriteSizeExceededError import FlightWriteSizeExceededError
from .GeneratorStream import GeneratorStream
from .Location import Location
from .RecordBatchStream import RecordBatchStream
from .Result import Result
from .SchemaResult import SchemaResult
from .ServerAuthHandler import ServerAuthHandler
from .ServerAuthReader import ServerAuthReader
from .ServerAuthSender import ServerAuthSender
from .ServerCallContext import ServerCallContext
from .ServerMiddleware import ServerMiddleware
from .ServerMiddlewareFactory import ServerMiddlewareFactory
from .Ticket import Ticket
from .TracingServerMiddleware import TracingServerMiddleware
from .TracingServerMiddlewareFactory import TracingServerMiddlewareFactory
from ._FlightServerFinalizer import _FlightServerFinalizer
from ._ServerMiddlewareFactoryWrapper import _ServerMiddlewareFactoryWrapper
from ._ServerMiddlewareWrapper import _ServerMiddlewareWrapper
# variables with complex values

_FLIGHT_SERVER_ERROR_REGEX = None # (!) real value is "re.compile('Flight RPC failed with message: (.*). Detail: Python exception: (.*)', re.DOTALL)"

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x0000024409B3A910>'

__spec__ = None # (!) real value is "ModuleSpec(name='pyarrow._flight', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x0000024409B3A910>, origin='C:\\\\Users\\\\akharin\\\\PycharmProjects\\\\pythonProject\\\\venv\\\\lib\\\\site-packages\\\\pyarrow\\\\_flight.cp39-win_amd64.pyd')"

__test__ = {}

