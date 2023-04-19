# encoding: utf-8
# module pyarrow._s3fs
# from C:\Users\akharin\PycharmProjects\pythonProject\venv\lib\site-packages\pyarrow\_s3fs.cp39-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
from pyarrow.lib import KeyValueMetadata, frombytes, tobytes

import enum as __enum
import pyarrow._fs as __pyarrow__fs


# Variables with simple values

Debug = 5

Error = 2

Fatal = 1

Info = 4

Off = 0

Trace = 6

Warn = 3

# functions

def finalize_s3(): # real signature unknown; restored from __doc__
    """ finalize_s3() """
    pass

def initialize_s3(S3LogLevel_log_level=None): # real signature unknown; restored from __doc__
    """
    initialize_s3(S3LogLevel log_level=S3LogLevel.Fatal)
    
        Initialize S3 support
    
        Parameters
        ----------
        log_level : S3LogLevel
            level of logging
    
        Examples
        --------
        >>> fs.initialize_s3(fs.S3LogLevel.Error) # doctest: +SKIP
    """
    pass

def resolve_s3_region(bucket): # real signature unknown; restored from __doc__
    """
    resolve_s3_region(bucket)
    
        Resolve the S3 region of a bucket.
    
        Parameters
        ----------
        bucket : str
            A S3 bucket name
    
        Returns
        -------
        region : str
            A S3 region name
    
        Examples
        --------
        >>> fs.resolve_s3_region('voltrondata-labs-datasets')
        'us-east-2'
    """
    pass

def __pyx_unpickle___Pyx_EnumMeta(*args, **kwargs): # real signature unknown
    pass

# classes

class S3RetryStrategy(object):
    """
    Base class for AWS retry strategies for use with S3.
    
        Parameters
        ----------
        max_attempts : int, default 3
            The maximum number of retry attempts to attempt before failing.
    """
    def __init__(self, max_attempts=3): # real signature unknown; restored from __doc__
        """ S3RetryStrategy.__init__(self, max_attempts=3) """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'pyarrow._s3fs', '__doc__': '\\n    Base class for AWS retry strategies for use with S3.\\n\\n    Parameters\\n    ----------\\n    max_attempts : int, default 3\\n        The maximum number of retry attempts to attempt before failing.\\n    ', '__init__': <cyfunction S3RetryStrategy.__init__ at 0x0000017D7C6232B0>, '__dict__': <attribute '__dict__' of 'S3RetryStrategy' objects>, '__weakref__': <attribute '__weakref__' of 'S3RetryStrategy' objects>})"


class AwsDefaultS3RetryStrategy(S3RetryStrategy):
    """
    Represents an AWS Default retry strategy for use with S3.
    
        Parameters
        ----------
        max_attempts : int, default 3
            The maximum number of retry attempts to attempt before failing.
    """
    def __init__(self, max_attempts=3): # real signature unknown; restored from __doc__
        """ S3RetryStrategy.__init__(self, max_attempts=3) """
        pass


class AwsStandardS3RetryStrategy(S3RetryStrategy):
    """
    Represents an AWS Standard retry strategy for use with S3.
    
        Parameters
        ----------
        max_attempts : int, default 3
            The maximum number of retry attempts to attempt before failing.
    """
    def __init__(self, max_attempts=3): # real signature unknown; restored from __doc__
        """ S3RetryStrategy.__init__(self, max_attempts=3) """
        pass


class S3FileSystem(__pyarrow__fs.FileSystem):
    """
    S3FileSystem(access_key=None, *, secret_key=None, session_token=None, bool anonymous=False, region=None, request_timeout=None, connect_timeout=None, scheme=None, endpoint_override=None, bool background_writes=True, default_metadata=None, role_arn=None, session_name=None, external_id=None, load_frequency=900, proxy_options=None, allow_bucket_creation=False, allow_bucket_deletion=False, retry_strategy: S3RetryStrategy = AwsStandardS3RetryStrategy(max_attempts=3))
    
        S3-backed FileSystem implementation
    
        If neither access_key nor secret_key are provided, and role_arn is also not
        provided, then attempts to initialize from AWS environment variables,
        otherwise both access_key and secret_key must be provided.
    
        If role_arn is provided instead of access_key and secret_key, temporary
        credentials will be fetched by issuing a request to STS to assume the
        specified role.
    
        Note: S3 buckets are special and the operations available on them may be
        limited or more expensive than desired.
    
        When S3FileSystem creates new buckets (assuming allow_bucket_creation is 
        True), it does not pass any non-default settings. In AWS S3, the bucket and 
        all objects will be not publicly visible, and will have no bucket policies 
        and no resource tags. To have more control over how buckets are created,
        use a different API to create them.
    
        Parameters
        ----------
        access_key : str, default None
            AWS Access Key ID. Pass None to use the standard AWS environment
            variables and/or configuration file.
        secret_key : str, default None
            AWS Secret Access key. Pass None to use the standard AWS environment
            variables and/or configuration file.
        session_token : str, default None
            AWS Session Token.  An optional session token, required if access_key
            and secret_key are temporary credentials from STS.
        anonymous : boolean, default False
            Whether to connect anonymously if access_key and secret_key are None.
            If true, will not attempt to look up credentials using standard AWS
            configuration methods.
        role_arn : str, default None
            AWS Role ARN.  If provided instead of access_key and secret_key,
            temporary credentials will be fetched by assuming this role.
        session_name : str, default None
            An optional identifier for the assumed role session.
        external_id : str, default None
            An optional unique identifier that might be required when you assume
            a role in another account.
        load_frequency : int, default 900
            The frequency (in seconds) with which temporary credentials from an
            assumed role session will be refreshed.
        region : str, default None
            AWS region to connect to. If not set, the AWS SDK will attempt to
            determine the region using heuristics such as environment variables,
            configuration profile, EC2 metadata, or default to 'us-east-1' when SDK
            version <1.8. One can also use :func:`pyarrow.fs.resolve_s3_region` to
            automatically resolve the region from a bucket name.
        request_timeout : double, default None
            Socket read timeouts on Windows and macOS, in seconds.
            If omitted, the AWS SDK default value is used (typically 3 seconds).
            This option is ignored on non-Windows, non-macOS systems.
        connect_timeout : double, default None
            Socket connection timeout, in seconds.
            If omitted, the AWS SDK default value is used (typically 1 second).
        scheme : str, default 'https'
            S3 connection transport scheme.
        endpoint_override : str, default None
            Override region with a connect string such as "localhost:9000"
        background_writes : boolean, default True
            Whether file writes will be issued in the background, without
            blocking.
        default_metadata : mapping or pyarrow.KeyValueMetadata, default None
            Default metadata for open_output_stream.  This will be ignored if
            non-empty metadata is passed to open_output_stream.
        proxy_options : dict or str, default None
            If a proxy is used, provide the options here. Supported options are:
            'scheme' (str: 'http' or 'https'; required), 'host' (str; required),
            'port' (int; required), 'username' (str; optional),
            'password' (str; optional).
            A proxy URI (str) can also be provided, in which case these options
            will be derived from the provided URI.
            The following are equivalent::
    
                S3FileSystem(proxy_options='http://username:password@localhost:8020')
                S3FileSystem(proxy_options={'scheme': 'http', 'host': 'localhost',
                                            'port': 8020, 'username': 'username',
                                            'password': 'password'})
        allow_bucket_creation : bool, default False
            Whether to allow CreateDir at the bucket-level. This option may also be 
            passed in a URI query parameter.
        allow_bucket_deletion : bool, default False
            Whether to allow DeleteDir at the bucket-level. This option may also be 
            passed in a URI query parameter.
        retry_strategy : S3RetryStrategy, default AwsStandardS3RetryStrategy(max_attempts=3)
            The retry strategy to use with S3; fail after max_attempts. Available
            strategies are AwsStandardS3RetryStrategy, AwsDefaultS3RetryStrategy.
    
        Examples
        --------
        >>> from pyarrow import fs
        >>> s3 = fs.S3FileSystem(region='us-west-2')
        >>> s3.get_file_info(fs.FileSelector(
        ...    'power-analysis-ready-datastore/power_901_constants.zarr/FROCEAN', recursive=True
        ... ))
        [<FileInfo for 'power-analysis-ready-datastore/power_901_constants.zarr/FROCEAN/.zarray...
    
        For usage of the methods see examples for :func:`~pyarrow.fs.LocalFileSystem`.
    """
    @classmethod
    def _reconstruct(cls, type_cls, kwargs): # real signature unknown; restored from __doc__
        """ S3FileSystem._reconstruct(type cls, kwargs) """
        pass

    def __init__(self, access_key=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self): # real signature unknown; restored from __doc__
        """ S3FileSystem.__reduce__(self) """
        pass

    region = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        The AWS region this filesystem connects to.
        """


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x0000017D6E02AA20>'


class S3LogLevel(__enum.IntEnum):
    """ An enumeration. """
    def _generate_next_value_(name, start, count, last_values): # reliably restored by inspect
        """
        Generate the next value when not given.
        
                name: the name of the member
                start: the initial start value or None
                count: the number of existing members
                last_value: the last value assigned or None
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(cls, value): # reliably restored by inspect
        # no doc
        pass

    Debug = 5
    Error = 2
    Fatal = 1
    Info = 4
    Off = 0
    Trace = 6
    Warn = 3
    _member_map_ = {
        'Debug': 5,
        'Error': 2,
        'Fatal': 1,
        'Info': 4,
        'Off': 0,
        'Trace': 6,
        'Warn': 3,
    }
    _member_names_ = [
        'Off',
        'Fatal',
        'Error',
        'Warn',
        'Info',
        'Debug',
        'Trace',
    ]
    _member_type_ = int
    _value2member_map_ = {
        0: 0,
        1: 1,
        2: 2,
        3: 3,
        4: 4,
        5: 5,
        6: 6,
    }


# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x0000017D6E02A910>'

__spec__ = None # (!) real value is "ModuleSpec(name='pyarrow._s3fs', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x0000017D6E02A910>, origin='C:\\\\Users\\\\akharin\\\\PycharmProjects\\\\pythonProject\\\\venv\\\\lib\\\\site-packages\\\\pyarrow\\\\_s3fs.cp39-win_amd64.pyd')"

__test__ = {
    'initialize_s3 (line 39)': '\n    Initialize S3 support\n\n    Parameters\n    ----------\n    log_level : S3LogLevel\n        level of logging\n\n    Examples\n    --------\n    >>> fs.initialize_s3(fs.S3LogLevel.Error) # doctest: +SKIP\n    ',
    'resolve_s3_region (line 61)': "\n    Resolve the S3 region of a bucket.\n\n    Parameters\n    ----------\n    bucket : str\n        A S3 bucket name\n\n    Returns\n    -------\n    region : str\n        A S3 region name\n\n    Examples\n    --------\n    >>> fs.resolve_s3_region('voltrondata-labs-datasets')\n    'us-east-2'\n    ",
}

