# encoding: utf-8
# module pyarrow._parquet_encryption
# from C:\Users\akharin\PycharmProjects\pythonProject\venv\lib\site-packages\pyarrow\_parquet_encryption.cp39-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import io as io # C:\Users\akharin\AppData\Local\Programs\Python\Python39\lib\io.py
import warnings as warnings # C:\Users\akharin\AppData\Local\Programs\Python\Python39\lib\warnings.py
from pyarrow.lib import ArrowException, frombytes, tobytes

import pyarrow.lib as __pyarrow_lib


# no functions
# classes

class CryptoFactory(__pyarrow_lib._Weakrefable):
    """
    CryptoFactory(kms_client_factory)
     A factory that produces the low-level FileEncryptionProperties and
        FileDecryptionProperties objects, from the high-level parameters.
    """
    def file_decryption_properties(self, KmsConnectionConfig_kms_connection_config, DecryptionConfiguration_decryption_config=None): # real signature unknown; restored from __doc__
        """
        CryptoFactory.file_decryption_properties(self, KmsConnectionConfig kms_connection_config, DecryptionConfiguration decryption_config=None)
        Create file decryption properties.
        
                Parameters
                ----------
                kms_connection_config : KmsConnectionConfig
                    Configuration of connection to KMS
        
                decryption_config : DecryptionConfiguration, default None
                    Configuration of the decryption, such as cache timeout.
                    Can be None.
        
                Returns
                -------
                file_decryption_properties : FileDecryptionProperties
                    File decryption properties.
        """
        pass

    def file_encryption_properties(self, KmsConnectionConfig_kms_connection_config, EncryptionConfiguration_encryption_config): # real signature unknown; restored from __doc__
        """
        CryptoFactory.file_encryption_properties(self, KmsConnectionConfig kms_connection_config, EncryptionConfiguration encryption_config)
        Create file encryption properties.
        
                Parameters
                ----------
                kms_connection_config : KmsConnectionConfig
                    Configuration of connection to KMS
        
                encryption_config : EncryptionConfiguration
                    Configuration of the encryption, such as which columns to encrypt
        
                Returns
                -------
                file_encryption_properties : FileEncryptionProperties
                    File encryption properties.
        """
        pass

    def remove_cache_entries_for_all_tokens(self): # real signature unknown; restored from __doc__
        """ CryptoFactory.remove_cache_entries_for_all_tokens(self) """
        pass

    def remove_cache_entries_for_token(self, access_token): # real signature unknown; restored from __doc__
        """ CryptoFactory.remove_cache_entries_for_token(self, access_token) """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        """
        Create CryptoFactory.
        
                Parameters
                ----------
                kms_client_factory : a callable that accepts KmsConnectionConfig
                    and returns a KmsClient
        """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ CryptoFactory.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ CryptoFactory.__setstate_cython__(self, __pyx_state) """
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x00000215D6D85C60>'
    __slots__ = ()


class DecryptionConfiguration(__pyarrow_lib._Weakrefable):
    """
    DecryptionConfiguration(cache_lifetime=None, *)
    Configuration of the decryption, such as cache timeout.
    """
    def __init__(self, cache_lifetime=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ DecryptionConfiguration.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ DecryptionConfiguration.__setstate_cython__(self, __pyx_state) """
        pass

    cache_lifetime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Lifetime of cached entities (key encryption keys,
        local wrapping keys, KMS client objects)."""


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x00000215D6D85B40>'
    __slots__ = ()


class EncryptionConfiguration(__pyarrow_lib._Weakrefable):
    """
    EncryptionConfiguration(footer_key, column_keys=None, *, encryption_algorithm=None, plaintext_footer=None, double_wrapping=None, cache_lifetime=None, internal_key_material=None, data_key_length_bits=None)
    Configuration of the encryption, such as which columns to encrypt
    """
    def __init__(self, footer_key, column_keys=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ EncryptionConfiguration.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ EncryptionConfiguration.__setstate_cython__(self, __pyx_state) """
        pass

    cache_lifetime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Lifetime of cached entities (key encryption keys,
        local wrapping keys, KMS client objects)."""

    column_keys = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        List of columns to encrypt, with master key IDs.
        """

    data_key_length_bits = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Length of data encryption keys (DEKs), randomly generated by parquet key
        management tools. Can be 128, 192 or 256 bits."""

    double_wrapping = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Use double wrapping - where data encryption keys (DEKs) are
        encrypted with key encryption keys (KEKs), which in turn are
        encrypted with master keys.
        If set to false, use single wrapping - where DEKs are
        encrypted directly with master keys."""

    encryption_algorithm = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Parquet encryption algorithm.
        Can be "AES_GCM_V1" (default), or "AES_GCM_CTR_V1"."""

    footer_key = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """ID of the master key for footer encryption/signing"""

    internal_key_material = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Store key material inside Parquet file footers; this mode doesn’t
        produce additional files. If set to false, key material is stored in
        separate files in the same folder, which enables key rotation for
        immutable Parquet files."""

    plaintext_footer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Write files with plaintext footer."""


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x00000215C878F690>'
    __slots__ = ()


class KmsClient(__pyarrow_lib._Weakrefable):
    """
    KmsClient()
    The abstract base class for KmsClient implementations.
    """
    def unwrap_key(self, wrapped_key, master_key_identifier): # real signature unknown; restored from __doc__
        """
        KmsClient.unwrap_key(self, wrapped_key, master_key_identifier)
        Unwrap a key - decrypt it with the master key.
        """
        pass

    def wrap_key(self, key_bytes, master_key_identifier): # real signature unknown; restored from __doc__
        """
        KmsClient.wrap_key(self, key_bytes, master_key_identifier)
        Wrap a key - encrypt it with the master key.
        """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ KmsClient.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ KmsClient.__setstate_cython__(self, __pyx_state) """
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x00000215D6D85C00>'


class KmsConnectionConfig(__pyarrow_lib._Weakrefable):
    """
    KmsConnectionConfig(kms_instance_id=None, *, kms_instance_url=None, key_access_token=None, custom_kms_conf=None)
    Configuration of the connection to the Key Management Service (KMS)
    """
    def refresh_key_access_token(self, value): # real signature unknown; restored from __doc__
        """ KmsConnectionConfig.refresh_key_access_token(self, value) """
        pass

    def __init__(self, kms_instance_id=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ KmsConnectionConfig.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ KmsConnectionConfig.__setstate_cython__(self, __pyx_state) """
        pass

    custom_kms_conf = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A dictionary with KMS-type-specific configuration"""

    key_access_token = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Authorization token that will be passed to KMS."""

    kms_instance_id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """ID of the KMS instance that will be used for encryption
        (if multiple KMS instances are available)."""

    kms_instance_url = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """URL of the KMS instance."""


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x00000215D6D85BA0>'
    __slots__ = ()


class timedelta(object):
    """
    Difference between two datetime values.
    
    timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)
    
    All arguments are optional and default to 0.
    Arguments may be integers or floats, and may be positive or negative.
    """
    def total_seconds(self, *args, **kwargs): # real signature unknown
        """ Total seconds in the duration. """
        pass

    def __abs__(self, *args, **kwargs): # real signature unknown
        """ abs(self) """
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        """ Return self+value. """
        pass

    def __bool__(self, *args, **kwargs): # real signature unknown
        """ True if self else False """
        pass

    def __divmod__(self, *args, **kwargs): # real signature unknown
        """ Return divmod(self, value). """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __floordiv__(self, *args, **kwargs): # real signature unknown
        """ Return self//value. """
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __hash__(self, *args, **kwargs): # real signature unknown
        """ Return hash(self). """
        pass

    def __init__(self, days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0): # real signature unknown; restored from __doc__
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __mod__(self, *args, **kwargs): # real signature unknown
        """ Return self%value. """
        pass

    def __mul__(self, *args, **kwargs): # real signature unknown
        """ Return self*value. """
        pass

    def __neg__(self, *args, **kwargs): # real signature unknown
        """ -self """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __pos__(self, *args, **kwargs): # real signature unknown
        """ +self """
        pass

    def __radd__(self, *args, **kwargs): # real signature unknown
        """ Return value+self. """
        pass

    def __rdivmod__(self, *args, **kwargs): # real signature unknown
        """ Return divmod(value, self). """
        pass

    def __reduce__(self): # real signature unknown; restored from __doc__
        """ __reduce__() -> (cls, state) """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __rfloordiv__(self, *args, **kwargs): # real signature unknown
        """ Return value//self. """
        pass

    def __rmod__(self, *args, **kwargs): # real signature unknown
        """ Return value%self. """
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        """ Return value*self. """
        pass

    def __rsub__(self, *args, **kwargs): # real signature unknown
        """ Return value-self. """
        pass

    def __rtruediv__(self, *args, **kwargs): # real signature unknown
        """ Return value/self. """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    def __sub__(self, *args, **kwargs): # real signature unknown
        """ Return self-value. """
        pass

    def __truediv__(self, *args, **kwargs): # real signature unknown
        """ Return self/value. """
        pass

    days = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Number of days."""

    microseconds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Number of microseconds (>= 0 and less than 1 second)."""

    seconds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Number of seconds (>= 0 and less than 1 day)."""


    max = datetime.timedelta(days=999999999, seconds=86399, microseconds=999999)
    min = datetime.timedelta(days=-999999999)
    resolution = datetime.timedelta(microseconds=1)


# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x00000215C879A910>'

__spec__ = None # (!) real value is "ModuleSpec(name='pyarrow._parquet_encryption', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x00000215C879A910>, origin='C:\\\\Users\\\\akharin\\\\PycharmProjects\\\\pythonProject\\\\venv\\\\lib\\\\site-packages\\\\pyarrow\\\\_parquet_encryption.cp39-win_amd64.pyd')"

__test__ = {}

