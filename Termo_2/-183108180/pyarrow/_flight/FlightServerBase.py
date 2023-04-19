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


class FlightServerBase(__pyarrow_lib._Weakrefable):
    """
    FlightServerBase(location=None, auth_handler=None, tls_certificates=None, verify_client=None, root_certificates=None, middleware=None)
    A Flight service definition.
    
        To start the server, create an instance of this class with an
        appropriate location. The server will be running as soon as the
        instance is created; it is not required to call :meth:`serve`.
    
        Override methods to define your Flight service.
    
        Parameters
        ----------
        location : str, tuple or Location optional, default None
            Location to serve on. Either a gRPC URI like `grpc://localhost:port`,
            a tuple of (host, port) pair, or a Location instance.
            If None is passed then the server will be started on localhost with a
            system provided random port.
        auth_handler : ServerAuthHandler optional, default None
            An authentication mechanism to use. May be None.
        tls_certificates : list optional, default None
            A list of (certificate, key) pairs.
        verify_client : boolean optional, default False
            If True, then enable mutual TLS: require the client to present
            a client certificate, and validate the certificate.
        root_certificates : bytes optional, default None
            If enabling mutual TLS, this specifies the PEM-encoded root
            certificate used to validate client certificates.
        middleware : dict optional, default None
            A dictionary of :class:`ServerMiddlewareFactory` instances. The
            string keys can be used to retrieve the middleware instance within
            RPC handlers (see :meth:`ServerCallContext.get_middleware`).
    """
    def do_action(self, context, action): # real signature unknown; restored from __doc__
        """
        FlightServerBase.do_action(self, context, action)
        Execute a custom action.
        
                This method should return an iterator, or it should be a
                generator. Applications should override this method to
                implement their own behavior. The default method raises a
                NotImplementedError.
        
                Parameters
                ----------
                context : ServerCallContext
                    Common contextual information.
                action : Action
                    The action to execute.
        
                Returns
                -------
                iterator of bytes
        """
        pass

    def do_exchange(self, context, descriptor, reader, writer): # real signature unknown; restored from __doc__
        """
        FlightServerBase.do_exchange(self, context, descriptor, reader, writer)
        Write data to a flight.
        
                Applications should override this method to implement their
                own behavior. The default method raises a NotImplementedError.
        
                Parameters
                ----------
                context : ServerCallContext
                    Common contextual information.
                descriptor : FlightDescriptor
                    The descriptor for the flight provided by the client.
                reader : MetadataRecordBatchReader
                    A reader for data uploaded by the client.
                writer : MetadataRecordBatchWriter
                    A writer to send responses to the client.
        """
        pass

    def do_get(self, context, ticket): # real signature unknown; restored from __doc__
        """
        FlightServerBase.do_get(self, context, ticket)
        Write data to a flight.
        
                Applications should override this method to implement their
                own behavior. The default method raises a NotImplementedError.
        
                Parameters
                ----------
                context : ServerCallContext
                    Common contextual information.
                ticket : Ticket
                    The ticket for the flight.
        
                Returns
                -------
                FlightDataStream
                    A stream of data to send back to the client.
        """
        pass

    def do_put(self, context, descriptor, MetadataRecordBatchReader_reader, FlightMetadataWriter_writer): # real signature unknown; restored from __doc__
        """
        FlightServerBase.do_put(self, context, descriptor, MetadataRecordBatchReader reader: MetadataRecordBatchReader, FlightMetadataWriter writer: FlightMetadataWriter)
        Write data to a flight.
        
                Applications should override this method to implement their
                own behavior. The default method raises a NotImplementedError.
        
                Parameters
                ----------
                context : ServerCallContext
                    Common contextual information.
                descriptor : FlightDescriptor
                    The descriptor for the flight provided by the client.
                reader : MetadataRecordBatchReader
                    A reader for data uploaded by the client.
                writer : FlightMetadataWriter
                    A writer to send responses to the client.
        """
        pass

    def get_flight_info(self, context, descriptor): # real signature unknown; restored from __doc__
        """
        FlightServerBase.get_flight_info(self, context, descriptor)
        Get information about a flight.
        
                Applications should override this method to implement their
                own behavior. The default method raises a NotImplementedError.
        
                Parameters
                ----------
                context : ServerCallContext
                    Common contextual information.
                descriptor : FlightDescriptor
                    The descriptor for the flight provided by the client.
        
                Returns
                -------
                FlightInfo
        """
        pass

    def get_schema(self, context, descriptor): # real signature unknown; restored from __doc__
        """
        FlightServerBase.get_schema(self, context, descriptor)
        Get the schema of a flight.
        
                Applications should override this method to implement their
                own behavior. The default method raises a NotImplementedError.
        
                Parameters
                ----------
                context : ServerCallContext
                    Common contextual information.
                descriptor : FlightDescriptor
                    The descriptor for the flight provided by the client.
        
                Returns
                -------
                Schema
        """
        pass

    def list_actions(self, context): # real signature unknown; restored from __doc__
        """
        FlightServerBase.list_actions(self, context)
        List custom actions available on this server.
        
                Applications should override this method to implement their
                own behavior. The default method raises a NotImplementedError.
        
                Parameters
                ----------
                context : ServerCallContext
                    Common contextual information.
        
                Returns
                -------
                iterator of ActionType or tuple
        """
        pass

    def list_flights(self, context, criteria): # real signature unknown; restored from __doc__
        """
        FlightServerBase.list_flights(self, context, criteria)
        List flights available on this service.
        
                Applications should override this method to implement their
                own behavior. The default method raises a NotImplementedError.
        
                Parameters
                ----------
                context : ServerCallContext
                    Common contextual information.
                criteria : bytes
                    Filter criteria provided by the client.
        
                Returns
                -------
                iterator of FlightInfo
        """
        pass

    def run(self): # real signature unknown; restored from __doc__
        """
        FlightServerBase.run(self)
        Block until the server shuts down.
        
                .. deprecated:: 0.15.0
                    Use the ``FlightServer.serve`` method instead
        """
        pass

    def serve(self): # real signature unknown; restored from __doc__
        """
        FlightServerBase.serve(self)
        Block until the server shuts down.
        
                This method only returns if shutdown() is called or a signal a
                received.
        """
        pass

    def shutdown(self): # real signature unknown; restored from __doc__
        """
        FlightServerBase.shutdown(self)
        Shut down the server, blocking until current requests finish.
        
                Do not call this directly from the implementation of a Flight
                method, as then the server will block forever waiting for that
                request to finish. Instead, call this method from a background
                thread.
        """
        pass

    def wait(self): # real signature unknown; restored from __doc__
        """
        FlightServerBase.wait(self)
        Block until server is terminated with shutdown.
        """
        pass

    def __enter__(self): # real signature unknown; restored from __doc__
        """ FlightServerBase.__enter__(self) """
        pass

    def __exit__(self, exc_type, exc_value, traceback): # real signature unknown; restored from __doc__
        """ FlightServerBase.__exit__(self, exc_type, exc_value, traceback) """
        pass

    def __init__(self, location=None, auth_handler=None, tls_certificates=None, verify_client=None, root_certificates=None, middleware=None): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ FlightServerBase.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ FlightServerBase.__setstate_cython__(self, __pyx_state) """
        pass

    port = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Get the port that this server is listening on.

        Returns a non-positive value if the operation is invalid
        (e.g. init() was not called or server is listening on a domain
        socket).
        """


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000002441813A0C0>'


