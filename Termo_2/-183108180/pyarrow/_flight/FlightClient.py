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


class FlightClient(__pyarrow_lib._Weakrefable):
    """
    FlightClient(location, tls_root_certs=None, *, cert_chain=None, private_key=None, override_hostname=None, middleware=None, write_size_limit_bytes=None, disable_server_verification=None, generic_options=None)
    A client to a Flight service.
    
        Connect to a Flight service on the given host and port.
    
        Parameters
        ----------
        location : str, tuple or Location
            Location to connect to. Either a gRPC URI like `grpc://localhost:port`,
            a tuple of (host, port) pair, or a Location instance.
        tls_root_certs : bytes or None
            PEM-encoded
        cert_chain: bytes or None
            Client certificate if using mutual TLS
        private_key: bytes or None
            Client private key for cert_chain is using mutual TLS
        override_hostname : str or None
            Override the hostname checked by TLS. Insecure, use with caution.
        middleware : list optional, default None
            A list of ClientMiddlewareFactory instances.
        write_size_limit_bytes : int optional, default None
            A soft limit on the size of a data payload sent to the
            server. Enabled if positive. If enabled, writing a record
            batch that (when serialized) exceeds this limit will raise an
            exception; the client can retry the write with a smaller
            batch.
        disable_server_verification : boolean optional, default False
            A flag that indicates that, if the client is connecting
            with TLS, that it skips server verification. If this is
            enabled, all other TLS settings are overridden.
        generic_options : list optional, default None
            A list of generic (string, int or string) option tuples passed
            to the underlying transport. Effect is implementation
            dependent.
    """
    def authenticate(self, auth_handler, FlightCallOptions_options=None): # real signature unknown; restored from __doc__
        """
        FlightClient.authenticate(self, auth_handler, FlightCallOptions options: FlightCallOptions = None)
        Authenticate to the server.
        
                Parameters
                ----------
                auth_handler : ClientAuthHandler
                    The authentication mechanism to use.
                options : FlightCallOptions
                    Options for this call.
        """
        pass

    def authenticate_basic_token(self, username, password, FlightCallOptions_options=None): # real signature unknown; restored from __doc__
        """
        FlightClient.authenticate_basic_token(self, username, password, FlightCallOptions options: FlightCallOptions = None)
        Authenticate to the server with HTTP basic authentication.
        
                Parameters
                ----------
                username : string
                    Username to authenticate with
                password : string
                    Password to authenticate with
                options  : FlightCallOptions
                    Options for this call
        
                Returns
                -------
                tuple : Tuple[str, str]
                    A tuple representing the FlightCallOptions authorization
                    header entry of a bearer token.
        """
        pass

    def close(self): # real signature unknown; restored from __doc__
        """
        FlightClient.close(self)
        Close the client and disconnect.
        """
        pass

    @classmethod
    def connect(cls, type_cls, location, tls_root_certs=None, cert_chain=None, private_key=None, override_hostname=None, disable_server_verification=None): # real signature unknown; restored from __doc__
        """
        FlightClient.connect(type cls, location, tls_root_certs=None, cert_chain=None, private_key=None, override_hostname=None, disable_server_verification=None)
        Connect to a Flight server.
        
                .. deprecated:: 0.15.0
                    Use the ``FlightClient`` constructor or ``pyarrow.flight.connect`` function instead.
        """
        pass

    def do_action(self, action, FlightCallOptions_options=None): # real signature unknown; restored from __doc__
        """
        FlightClient.do_action(self, action, FlightCallOptions options: FlightCallOptions = None)
        
                Execute an action on a service.
        
                Parameters
                ----------
                action : str, tuple, or Action
                    Can be action type name (no body), type and body, or any Action
                    object
                options : FlightCallOptions
                    RPC options
        
                Returns
                -------
                results : iterator of Result values
        """
        pass

    def do_exchange(self, FlightDescriptor_descriptor, FlightCallOptions_options=None): # real signature unknown; restored from __doc__
        """
        FlightClient.do_exchange(self, FlightDescriptor descriptor: FlightDescriptor, FlightCallOptions options: FlightCallOptions = None)
        Start a bidirectional data exchange with a server.
        
                Parameters
                ----------
                descriptor : FlightDescriptor
                    A descriptor for the flight.
                options : FlightCallOptions
                    RPC options.
        
                Returns
                -------
                writer : FlightStreamWriter
                reader : FlightStreamReader
        """
        pass

    def do_get(self, Ticket_ticket, FlightCallOptions_options=None): # real signature unknown; restored from __doc__
        """
        FlightClient.do_get(self, Ticket ticket: Ticket, FlightCallOptions options: FlightCallOptions = None)
        Request the data for a flight.
        
                Returns
                -------
                reader : FlightStreamReader
        """
        pass

    def do_put(self, FlightDescriptor_descriptor, Schema_schema, FlightCallOptions_options=None): # real signature unknown; restored from __doc__
        """
        FlightClient.do_put(self, FlightDescriptor descriptor: FlightDescriptor, Schema schema, FlightCallOptions options: FlightCallOptions = None)
        Upload data to a flight.
        
                Returns
                -------
                writer : FlightStreamWriter
                reader : FlightMetadataReader
        """
        pass

    def get_flight_info(self, FlightDescriptor_descriptor, FlightCallOptions_options=None): # real signature unknown; restored from __doc__
        """
        FlightClient.get_flight_info(self, FlightDescriptor descriptor: FlightDescriptor, FlightCallOptions options: FlightCallOptions = None)
        Request information about an available flight.
        """
        pass

    def get_schema(self, FlightDescriptor_descriptor, FlightCallOptions_options=None): # real signature unknown; restored from __doc__
        """
        FlightClient.get_schema(self, FlightDescriptor descriptor: FlightDescriptor, FlightCallOptions options: FlightCallOptions = None)
        Request schema for an available flight.
        """
        pass

    def list_actions(self, FlightCallOptions_options=None): # real signature unknown; restored from __doc__
        """
        FlightClient.list_actions(self, FlightCallOptions options: FlightCallOptions = None)
        List the actions available on a service.
        """
        pass

    def list_flights(self, bytes_criteria=None, FlightCallOptions_options=None): # real signature unknown; restored from __doc__
        """
        FlightClient.list_flights(self, bytes criteria: bytes = None, FlightCallOptions options: FlightCallOptions = None)
        List the flights available on a service.
        """
        pass

    def wait_for_available(self, timeout=5): # real signature unknown; restored from __doc__
        """
        FlightClient.wait_for_available(self, timeout=5)
        Block until the server can be contacted.
        
                Parameters
                ----------
                timeout : int, default 5
                    The maximum seconds to wait.
        """
        pass

    def __del__(self): # real signature unknown; restored from __doc__
        """ FlightClient.__del__(self) """
        pass

    def __enter__(self): # real signature unknown; restored from __doc__
        """ FlightClient.__enter__(self) """
        pass

    def __exit__(self, exc_type, exc_value, traceback): # real signature unknown; restored from __doc__
        """ FlightClient.__exit__(self, exc_type, exc_value, traceback) """
        pass

    def __init__(self, location, tls_root_certs=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ FlightClient.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ FlightClient.__setstate_cython__(self, __pyx_state) """
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000002441812EA50>'


