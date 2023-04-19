# encoding: utf-8
# module pyarrow._fs
# from C:\Users\akharin\PycharmProjects\pythonProject\venv\lib\site-packages\pyarrow\_fs.cp39-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import os as os # C:\Users\akharin\AppData\Local\Programs\Python\Python39\lib\os.py
import pathlib as pathlib # C:\Users\akharin\AppData\Local\Programs\Python\Python39\lib\pathlib.py
import sys as sys # <module 'sys' (built-in)>
from pyarrow.lib import _detect_compression, frombytes, tobytes

import abc as __abc
import datetime as __datetime
import enum as __enum
import pyarrow.lib as __pyarrow_lib


# Variables with simple values

Directory = 3

File = 2

NotFound = 0

Unknown = 1

# functions

def abstractmethod(funcobj): # reliably restored by inspect
    """
    A decorator indicating abstract methods.
    
        Requires that the metaclass is ABCMeta or derived from it.  A
        class that has a metaclass derived from ABCMeta cannot be
        instantiated unless all of its abstract methods are overridden.
        The abstract methods can be called using any of the normal
        'super' call mechanisms.  abstractmethod() may be used to declare
        abstract methods for properties and descriptors.
    
        Usage:
    
            class C(metaclass=ABCMeta):
                @abstractmethod
                def my_abstract_method(self, ...):
                    ...
    """
    pass

def _copy_files(FileSystem_source_fs, unicode_source_path, FileSystem_destination_fs, unicode_destination_path, int64_t_chunk_size, bool_use_threads): # real signature unknown; restored from __doc__
    """ _copy_files(FileSystem source_fs, unicode source_path, FileSystem destination_fs, unicode destination_path, int64_t chunk_size, bool use_threads) """
    pass

def _copy_files_selector(FileSystem_source_fs, FileSelector_source_sel, FileSystem_destination_fs, unicode_destination_base_dir, int64_t_chunk_size, bool_use_threads): # real signature unknown; restored from __doc__
    """ _copy_files_selector(FileSystem source_fs, FileSelector source_sel, FileSystem destination_fs, unicode destination_base_dir, int64_t chunk_size, bool use_threads) """
    pass

def _file_type_to_string(ty): # real signature unknown; restored from __doc__
    """ _file_type_to_string(ty) """
    pass

def _stringify_path(path): # reliably restored by inspect
    """ Convert *path* to a string or unicode path if possible. """
    pass

def __pyx_unpickle___Pyx_EnumMeta(*args, **kwargs): # real signature unknown
    pass

# classes

class ABC(object):
    """
    Helper class that provides a standard way to create an ABC using
        inheritance.
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _abc_impl = None # (!) real value is '<_abc._abc_data object at 0x00000231CFC75680>'
    __abstractmethods__ = frozenset()
    __slots__ = ()


class FileInfo(__pyarrow_lib._Weakrefable):
    """
    FileInfo(path, FileType type=FileType.Unknown, mtime=None, *, mtime_ns=None, size=None)
    
        FileSystem entry info.
    
        Parameters
        ----------
        path : str
            The full path to the filesystem entry.
        type : FileType
            The type of the filesystem entry.
        mtime : datetime or float, default None
            If given, the modification time of the filesystem entry.
            If a float is given, it is the number of seconds since the
            Unix epoch.
        mtime_ns : int, default None
            If given, the modification time of the filesystem entry,
            in nanoseconds since the Unix epoch.
            `mtime` and `mtime_ns` are mutually exclusive.
        size : int, default None
            If given, the filesystem entry size in bytes.  This should only
            be given if `type` is `FileType.File`.
    
        Examples
        --------
        Generate a file:
    
        >>> from pyarrow import fs
        >>> local = fs.LocalFileSystem()
        >>> path_fs = local_path + '/pyarrow-fs-example.dat'
        >>> with local.open_output_stream(path_fs) as stream:
        ...     stream.write(b'data')
        4
    
        Get FileInfo object using ``get_file_info()``:
    
        >>> file_info = local.get_file_info(path_fs)
        >>> file_info
        <FileInfo for '.../pyarrow-fs-example.dat': type=FileType.File, size=4>
    
        Inspect FileInfo attributes:
    
        >>> file_info.type
        <FileType.File: 2>
    
        >>> file_info.is_file
        True
    
        >>> file_info.path
        '/.../pyarrow-fs-example.dat'
    
        >>> file_info.base_name
        'pyarrow-fs-example.dat'
    
        >>> file_info.size
        4
    
        >>> file_info.extension
        'dat'
    
        >>> file_info.mtime # doctest: +SKIP
        datetime.datetime(2022, 6, 29, 7, 56, 10, 873922, tzinfo=datetime.timezone.utc)
    
        >>> file_info.mtime_ns # doctest: +SKIP
        1656489370873922073
    """
    def __init__(self, path, FileType_type=None, mtime=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ FileInfo.__reduce_cython__(self) """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ FileInfo.__setstate_cython__(self, __pyx_state) """
        pass

    base_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        The file base name.

        Component after the last directory separator.

        Examples
        --------
        >>> file_info = local.get_file_info(path)
        >>> file_info.base_name
        'pyarrow-fs-example.dat'
        """

    extension = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        The file extension.

        Examples
        --------
        >>> file_info = local.get_file_info(path)
        >>> file_info.extension
        'dat'
        """

    is_file = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        """

    mtime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        The time of last modification, if available.

        Returns
        -------
        mtime : datetime.datetime or None

        Examples
        --------
        >>> file_info = local.get_file_info(path)
        >>> file_info.mtime # doctest: +SKIP
        datetime.datetime(2022, 6, 29, 7, 56, 10, 873922, tzinfo=datetime.timezone.utc)
        """

    mtime_ns = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        The time of last modification, if available, expressed in nanoseconds
        since the Unix epoch.

        Returns
        -------
        mtime_ns : int or None

        Examples
        --------
        >>> file_info = local.get_file_info(path)
        >>> file_info.mtime_ns # doctest: +SKIP
        1656489370873922073
        """

    path = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        The full file path in the filesystem.

        Examples
        --------
        >>> file_info = local.get_file_info(path)
        >>> file_info.path
        '/.../pyarrow-fs-example.dat'
        """

    size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        The size in bytes, if available.

        Only regular files are guaranteed to have a size.

        Returns
        -------
        size : int or None
        """

    type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Type of the file.

        The returned enum values can be the following:

        - FileType.NotFound: target does not exist
        - FileType.Unknown: target exists but its type is unknown (could be a
          special file such as a Unix socket or character device, or
          Windows NUL / CON / ...)
        - FileType.File: target is a regular file
        - FileType.Directory: target is a regular directory

        Returns
        -------
        type : FileType
        """


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x00000231E06F5DB0>'


class FileSelector(__pyarrow_lib._Weakrefable):
    """
    FileSelector(base_dir, bool allow_not_found=False, bool recursive=False)
    
        File and directory selector.
    
        It contains a set of options that describes how to search for files and
        directories.
    
        Parameters
        ----------
        base_dir : str
            The directory in which to select files. Relative paths also work, use
            '.' for the current directory and '..' for the parent.
        allow_not_found : bool, default False
            The behavior if `base_dir` doesn't exist in the filesystem.
            If false, an error is returned.
            If true, an empty selection is returned.
        recursive : bool, default False
            Whether to recurse into subdirectories.
    
        Examples
        --------
        List the contents of a directory and subdirectories:
    
        >>> selector_1 = fs.FileSelector(local_path, recursive=True)
        >>> local.get_file_info(selector_1) # doctest: +SKIP
        [<FileInfo for 'tmp/alphabet/example.dat': type=FileType.File, size=4>,
        <FileInfo for 'tmp/alphabet/subdir': type=FileType.Directory>,
        <FileInfo for 'tmp/alphabet/subdir/example_copy.dat': type=FileType.File, size=4>]
    
        List only the contents of the base directory:
    
        >>> selector_2 = fs.FileSelector(local_path)
        >>> local.get_file_info(selector_2) # doctest: +SKIP
        [<FileInfo for 'tmp/alphabet/example.dat': type=FileType.File, size=4>,
        <FileInfo for 'tmp/alphabet/subdir': type=FileType.Directory>]
    
        Return empty selection if the directory doesn't exist:
    
        >>> selector_not_found = fs.FileSelector(local_path + '/missing',
        ...                                      recursive=True,
        ...                                      allow_not_found=True)
        >>> local.get_file_info(selector_not_found)
        []
    """
    def __init__(self, base_dir, bool_allow_not_found=False, bool_recursive=False): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ FileSelector.__reduce_cython__(self) """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ FileSelector.__setstate_cython__(self, __pyx_state) """
        pass

    allow_not_found = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    base_dir = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    recursive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x00000231E06F5E10>'


class FileSystem(__pyarrow_lib._Weakrefable):
    """
    FileSystem()
    
        Abstract file system API.
    """
    def copy_file(self, src, dest): # real signature unknown; restored from __doc__
        """
        FileSystem.copy_file(self, src, dest)
        
                Copy a file.
        
                If the destination exists and is a directory, an error is returned.
                Otherwise, it is replaced.
        
                Parameters
                ----------
                src : str
                    The path of the file to be copied from.
                dest : str
                    The destination path where the file is copied to.
        
                Examples
                --------
                >>> local.copy_file(path,
                ...                 local_path + '/pyarrow-fs-example_copy.dat')
        
                Inspect the file info:
        
                >>> local.get_file_info(local_path + '/pyarrow-fs-example_copy.dat')
                <FileInfo for '/.../pyarrow-fs-example_copy.dat': type=FileType.File, size=4>
                >>> local.get_file_info(path)
                <FileInfo for '/.../pyarrow-fs-example.dat': type=FileType.File, size=4>
        """
        pass

    def create_dir(self, path, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        FileSystem.create_dir(self, path, *, bool recursive=True)
        
                Create a directory and subdirectories.
        
                This function succeeds if the directory already exists.
        
                Parameters
                ----------
                path : str
                    The path of the new directory.
                recursive : bool, default True
                    Create nested directories as well.
        """
        pass

    def delete_dir(self, path): # real signature unknown; restored from __doc__
        """
        FileSystem.delete_dir(self, path)
        
                Delete a directory and its contents, recursively.
        
                Parameters
                ----------
                path : str
                    The path of the directory to be deleted.
        """
        pass

    def delete_dir_contents(self, path, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        FileSystem.delete_dir_contents(self, path, *, bool accept_root_dir=False, bool missing_dir_ok=False)
        
                Delete a directory's contents, recursively.
        
                Like delete_dir, but doesn't delete the directory itself.
        
                Parameters
                ----------
                path : str
                    The path of the directory to be deleted.
                accept_root_dir : boolean, default False
                    Allow deleting the root directory's contents
                    (if path is empty or "/")
                missing_dir_ok : boolean, default False
                    If False then an error is raised if path does
                    not exist
        """
        pass

    def delete_file(self, path): # real signature unknown; restored from __doc__
        """
        FileSystem.delete_file(self, path)
        
                Delete a file.
        
                Parameters
                ----------
                path : str
                    The path of the file to be deleted.
        """
        pass

    def equals(self, FileSystem_other): # real signature unknown; restored from __doc__
        """ FileSystem.equals(self, FileSystem other) """
        pass

    def from_uri(self, uri): # real signature unknown; restored from __doc__
        """
        FileSystem.from_uri(uri)
        
                Create a new FileSystem from URI or Path.
        
                Recognized URI schemes are "file", "mock", "s3fs", "gs", "gcs", "hdfs" and "viewfs".
                In addition, the argument can be a pathlib.Path object, or a string
                describing an absolute local path.
        
                Parameters
                ----------
                uri : string
                    URI-based path, for example: file:///some/local/path.
        
                Returns
                -------
                tuple of (FileSystem, str path)
                    With (filesystem, path) tuple where path is the abstract path
                    inside the FileSystem instance.
        
                Examples
                --------
                Create a new FileSystem subclass from a URI:
        
                >>> uri = 'file:///{}/pyarrow-fs-example.dat'.format(local_path)
                >>> local_new, path_new = fs.FileSystem.from_uri(uri)
                >>> local_new
                <pyarrow._fs.LocalFileSystem object at ...
                >>> path_new
                '/.../pyarrow-fs-example.dat'
        
                Or from a s3 bucket:
        
                >>> fs.FileSystem.from_uri("s3://usgs-landsat/collection02/")
                (<pyarrow._s3fs.S3FileSystem object at ...>, 'usgs-landsat/collection02')
        """
        pass

    def get_file_info(self, paths_or_selector): # real signature unknown; restored from __doc__
        """
        FileSystem.get_file_info(self, paths_or_selector)
        
                Get info for the given files.
        
                Any symlink is automatically dereferenced, recursively. A non-existing
                or unreachable file returns a FileStat object and has a FileType of
                value NotFound. An exception indicates a truly exceptional condition
                (low-level I/O error, etc.).
        
                Parameters
                ----------
                paths_or_selector : FileSelector, path-like or list of path-likes
                    Either a selector object, a path-like object or a list of
                    path-like objects. The selector's base directory will not be
                    part of the results, even if it exists. If it doesn't exist,
                    use `allow_not_found`.
        
                Returns
                -------
                FileInfo or list of FileInfo
                    Single FileInfo object is returned for a single path, otherwise
                    a list of FileInfo objects is returned.
        
                Examples
                --------
                >>> local
                <pyarrow._fs.LocalFileSystem object at ...>
                >>> local.get_file_info("/{}/pyarrow-fs-example.dat".format(local_path))
                <FileInfo for '/.../pyarrow-fs-example.dat': type=FileType.File, size=4>
        """
        pass

    def move(self, src, dest): # real signature unknown; restored from __doc__
        """
        FileSystem.move(self, src, dest)
        
                Move / rename a file or directory.
        
                If the destination exists:
                - if it is a non-empty directory, an error is returned
                - otherwise, if it has the same type as the source, it is replaced
                - otherwise, behavior is unspecified (implementation-dependent).
        
                Parameters
                ----------
                src : str
                    The path of the file or the directory to be moved.
                dest : str
                    The destination path where the file or directory is moved to.
        
                Examples
                --------
                Create a new folder with a file:
        
                >>> local.create_dir('/tmp/other_dir')
                >>> local.copy_file(path,'/tmp/move_example.dat')
        
                Move the file:
        
                >>> local.move('/tmp/move_example.dat',
                ...            '/tmp/other_dir/move_example_2.dat')
        
                Inspect the file info:
        
                >>> local.get_file_info('/tmp/other_dir/move_example_2.dat')
                <FileInfo for '/tmp/other_dir/move_example_2.dat': type=FileType.File, size=4>
                >>> local.get_file_info('/tmp/move_example.dat')
                <FileInfo for '/tmp/move_example.dat': type=FileType.NotFound>
        
                Delete the folder:
                >>> local.delete_dir('/tmp/other_dir')
        """
        pass

    def normalize_path(self, path): # real signature unknown; restored from __doc__
        """
        FileSystem.normalize_path(self, path)
        
                Normalize filesystem path.
        
                Parameters
                ----------
                path : str
                    The path to normalize
        
                Returns
                -------
                normalized_path : str
                    The normalized path
        """
        pass

    def open_append_stream(self, path, compression=None, buffer_size=None, metadata=None): # real signature unknown; restored from __doc__
        """
        FileSystem.open_append_stream(self, path, compression=u'detect', buffer_size=None, metadata=None)
        
                Open an output stream for appending.
        
                If the target doesn't exist, a new empty file is created.
        
                .. note::
                    Some filesystem implementations do not support efficient
                    appending to an existing file, in which case this method will
                    raise NotImplementedError.
                    Consider writing to multiple files (using e.g. the dataset layer)
                    instead.
        
                Parameters
                ----------
                path : str
                    The source to open for writing.
                compression : str optional, default 'detect'
                    The compression algorithm to use for on-the-fly compression.
                    If "detect" and source is a file path, then compression will be
                    chosen based on the file extension.
                    If None, no compression will be applied. Otherwise, a well-known
                    algorithm name must be supplied (e.g. "gzip").
                buffer_size : int optional, default None
                    If None or 0, no buffering will happen. Otherwise the size of the
                    temporary write buffer.
                metadata : dict optional, default None
                    If not None, a mapping of string keys to string values.
                    Some filesystems support storing metadata along the file
                    (such as "Content-Type").
                    Unsupported metadata keys will be ignored.
        
                Returns
                -------
                stream : NativeFile
        
                Examples
                --------
                Append new data to a FileSystem subclass with nonempty file:
        
                >>> with local.open_append_stream(path) as f:
                ...     f.write(b'+newly added')
                12
        
                Print out the content fo the file:
        
                >>> with local.open_input_file(path) as f:
                ...     print(f.readall())
                b'data+newly added'
        """
        pass

    def open_input_file(self, path): # real signature unknown; restored from __doc__
        """
        FileSystem.open_input_file(self, path)
        
                Open an input file for random access reading.
        
                Parameters
                ----------
                path : str
                    The source to open for reading.
        
                Returns
                -------
                stream : NativeFile
        
                Examples
                --------
                Print the data from the file with `open_input_file()`:
        
                >>> with local.open_input_file(path) as f:
                ...     print(f.readall())
                b'data'
        """
        pass

    def open_input_stream(self, path, compression=None, buffer_size=None): # real signature unknown; restored from __doc__
        """
        FileSystem.open_input_stream(self, path, compression=u'detect', buffer_size=None)
        
                Open an input stream for sequential reading.
        
                Parameters
                ----------
                path : str
                    The source to open for reading.
                compression : str optional, default 'detect'
                    The compression algorithm to use for on-the-fly decompression.
                    If "detect" and source is a file path, then compression will be
                    chosen based on the file extension.
                    If None, no compression will be applied. Otherwise, a well-known
                    algorithm name must be supplied (e.g. "gzip").
                buffer_size : int optional, default None
                    If None or 0, no buffering will happen. Otherwise the size of the
                    temporary read buffer.
        
                Returns
                -------
                stream : NativeFile
        
                Examples
                --------
                Print the data from the file with `open_input_stream()`:
        
                >>> with local.open_input_stream(path) as f:
                ...     print(f.readall())
                b'data'
        """
        pass

    def open_output_stream(self, path, compression=None, buffer_size=None, metadata=None): # real signature unknown; restored from __doc__
        """
        FileSystem.open_output_stream(self, path, compression=u'detect', buffer_size=None, metadata=None)
        
                Open an output stream for sequential writing.
        
                If the target already exists, existing data is truncated.
        
                Parameters
                ----------
                path : str
                    The source to open for writing.
                compression : str optional, default 'detect'
                    The compression algorithm to use for on-the-fly compression.
                    If "detect" and source is a file path, then compression will be
                    chosen based on the file extension.
                    If None, no compression will be applied. Otherwise, a well-known
                    algorithm name must be supplied (e.g. "gzip").
                buffer_size : int optional, default None
                    If None or 0, no buffering will happen. Otherwise the size of the
                    temporary write buffer.
                metadata : dict optional, default None
                    If not None, a mapping of string keys to string values.
                    Some filesystems support storing metadata along the file
                    (such as "Content-Type").
                    Unsupported metadata keys will be ignored.
        
                Returns
                -------
                stream : NativeFile
        
                Examples
                --------
                >>> local = fs.LocalFileSystem()
                >>> with local.open_output_stream(path) as stream:
                ...     stream.write(b'data')
                4
        """
        pass

    def _wrap_input_stream(self, stream, path, compression, buffer_size): # real signature unknown; restored from __doc__
        """ FileSystem._wrap_input_stream(self, stream, path, compression, buffer_size) """
        pass

    def _wrap_output_stream(self, stream, path, compression, buffer_size): # real signature unknown; restored from __doc__
        """ FileSystem._wrap_output_stream(self, stream, path, compression, buffer_size) """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ FileSystem.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ FileSystem.__setstate_cython__(self, __pyx_state) """
        pass

    type_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        The filesystem's type name.
        """


    __hash__ = None
    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x00000231E06F5E70>'


class FileSystemHandler(__abc.ABC):
    """ An abstract class exposing methods to implement PyFileSystem's behavior. """
    def copy_file(self, src, dest): # real signature unknown; restored from __doc__
        """
        FileSystemHandler.copy_file(self, src, dest)
        
                Implement PyFileSystem.copy_file(...).
        
                Parameters
                ----------
                src : str
                    path of what should be copied.
                dest : str
                    path of where it should be copied to.
        """
        pass

    def create_dir(self, path, recursive): # real signature unknown; restored from __doc__
        """
        FileSystemHandler.create_dir(self, path, recursive)
        
                Implement PyFileSystem.create_dir(...).
        
                Parameters
                ----------
                path : str
                    path of the directory.
                recursive : bool
                    if the parent directories should be created too.
        """
        pass

    def delete_dir(self, path): # real signature unknown; restored from __doc__
        """
        FileSystemHandler.delete_dir(self, path)
        
                Implement PyFileSystem.delete_dir(...).
        
                Parameters
                ----------
                path : str
                    path of the directory.
        """
        pass

    def delete_dir_contents(self, path, missing_dir_ok=False): # real signature unknown; restored from __doc__
        """
        FileSystemHandler.delete_dir_contents(self, path, missing_dir_ok=False)
        
                Implement PyFileSystem.delete_dir_contents(...).
        
                Parameters
                ----------
                path : str
                    path of the directory.
                missing_dir_ok : bool
                    if False an error should be raised if path does not exist
        """
        pass

    def delete_file(self, path): # real signature unknown; restored from __doc__
        """
        FileSystemHandler.delete_file(self, path)
        
                Implement PyFileSystem.delete_file(...).
        
                Parameters
                ----------
                path : str
                    path of the file.
        """
        pass

    def delete_root_dir_contents(self): # real signature unknown; restored from __doc__
        """
        FileSystemHandler.delete_root_dir_contents(self)
        
                Implement PyFileSystem.delete_dir_contents("/", accept_root_dir=True).
        """
        pass

    def get_file_info(self, paths): # real signature unknown; restored from __doc__
        """
        FileSystemHandler.get_file_info(self, paths)
        
                Implement PyFileSystem.get_file_info(paths).
        
                Parameters
                ----------
                paths : list of str
                    paths for which we want to retrieve the info.
        """
        pass

    def get_file_info_selector(self, selector): # real signature unknown; restored from __doc__
        """
        FileSystemHandler.get_file_info_selector(self, selector)
        
                Implement PyFileSystem.get_file_info(selector).
        
                Parameters
                ----------
                selector : FileSelector
                    selector for which we want to retrieve the info.
        """
        pass

    def get_type_name(self): # real signature unknown; restored from __doc__
        """
        FileSystemHandler.get_type_name(self)
        
                Implement PyFileSystem.type_name.
        """
        pass

    def move(self, src, dest): # real signature unknown; restored from __doc__
        """
        FileSystemHandler.move(self, src, dest)
        
                Implement PyFileSystem.move(...).
        
                Parameters
                ----------
                src : str
                    path of what should be moved.
                dest : str
                    path of where it should be moved to.
        """
        pass

    def normalize_path(self, path): # real signature unknown; restored from __doc__
        """
        FileSystemHandler.normalize_path(self, path)
        
                Implement PyFileSystem.normalize_path(...).
        
                Parameters
                ----------
                path : str
                    path of what should be normalized.
        """
        pass

    def open_append_stream(self, path, metadata): # real signature unknown; restored from __doc__
        """
        FileSystemHandler.open_append_stream(self, path, metadata)
        
                Implement PyFileSystem.open_append_stream(...).
        
                Parameters
                ----------
                path : str
                    path of what should be opened.
                metadata :  mapping
                    Mapping of string keys to string values.
                    Some filesystems support storing metadata along the file
                    (such as "Content-Type").
        """
        pass

    def open_input_file(self, path): # real signature unknown; restored from __doc__
        """
        FileSystemHandler.open_input_file(self, path)
        
                Implement PyFileSystem.open_input_file(...).
        
                Parameters
                ----------
                path : str
                    path of what should be opened.
        """
        pass

    def open_input_stream(self, path): # real signature unknown; restored from __doc__
        """
        FileSystemHandler.open_input_stream(self, path)
        
                Implement PyFileSystem.open_input_stream(...).
        
                Parameters
                ----------
                path : str
                    path of what should be opened.
        """
        pass

    def open_output_stream(self, path, metadata): # real signature unknown; restored from __doc__
        """
        FileSystemHandler.open_output_stream(self, path, metadata)
        
                Implement PyFileSystem.open_output_stream(...).
        
                Parameters
                ----------
                path : str
                    path of what should be opened.
                metadata :  mapping
                    Mapping of string keys to string values.
                    Some filesystems support storing metadata along the file
                    (such as "Content-Type").
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    _abc_impl = None # (!) real value is '<_abc._abc_data object at 0x00000231E07008C0>'
    __abstractmethods__ = frozenset({'create_dir', 'delete_dir', 'get_file_info', 'delete_dir_contents', 'copy_file', 'open_input_stream', 'open_input_file', 'get_type_name', 'normalize_path', 'move', 'delete_root_dir_contents', 'open_output_stream', 'get_file_info_selector', 'open_append_stream', 'delete_file'})
    __dict__ = None # (!) real value is 'mappingproxy({\'__module__\': \'pyarrow._fs\', \'__doc__\': "\\n    An abstract class exposing methods to implement PyFileSystem\'s behavior.\\n    ", \'get_type_name\': <cyfunction FileSystemHandler.get_type_name at 0x00000231D221D5F0>, \'get_file_info\': <cyfunction FileSystemHandler.get_file_info at 0x00000231D2203BA0>, \'get_file_info_selector\': <cyfunction FileSystemHandler.get_file_info_selector at 0x00000231D20F2930>, \'create_dir\': <cyfunction FileSystemHandler.create_dir at 0x00000231D20F2860>, \'delete_dir\': <cyfunction FileSystemHandler.delete_dir at 0x00000231D20F26C0>, \'delete_dir_contents\': <cyfunction FileSystemHandler.delete_dir_contents at 0x00000231D20F25F0>, \'delete_root_dir_contents\': <cyfunction FileSystemHandler.delete_root_dir_contents at 0x00000231E06D9A00>, \'delete_file\': <cyfunction FileSystemHandler.delete_file at 0x00000231E06D9930>, \'move\': <cyfunction FileSystemHandler.move at 0x00000231E06D9860>, \'copy_file\': <cyfunction FileSystemHandler.copy_file at 0x00000231E06D9AD0>, \'open_input_stream\': <cyfunction FileSystemHandler.open_input_stream at 0x00000231E06D9BA0>, \'open_input_file\': <cyfunction FileSystemHandler.open_input_file at 0x00000231E06D9C70>, \'open_output_stream\': <cyfunction FileSystemHandler.open_output_stream at 0x00000231E06D9D40>, \'open_append_stream\': <cyfunction FileSystemHandler.open_append_stream at 0x00000231E06D9E10>, \'normalize_path\': <cyfunction FileSystemHandler.normalize_path at 0x00000231E06D9EE0>, \'__dict__\': <attribute \'__dict__\' of \'FileSystemHandler\' objects>, \'__weakref__\': <attribute \'__weakref__\' of \'FileSystemHandler\' objects>, \'__abstractmethods__\': frozenset({\'create_dir\', \'delete_dir\', \'get_file_info\', \'delete_dir_contents\', \'copy_file\', \'open_input_stream\', \'open_input_file\', \'get_type_name\', \'normalize_path\', \'move\', \'delete_root_dir_contents\', \'open_output_stream\', \'get_file_info_selector\', \'open_append_stream\', \'delete_file\'}), \'_abc_impl\': <_abc._abc_data object at 0x00000231E07008C0>})'


class FileType(__enum.IntEnum):
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

    Directory = 3
    File = 2
    NotFound = 0
    Unknown = 1
    _member_map_ = {
        'Directory': 3,
        'File': 2,
        'NotFound': 0,
        'Unknown': 1,
    }
    _member_names_ = [
        'NotFound',
        'Unknown',
        'File',
        'Directory',
    ]
    _member_type_ = int
    _value2member_map_ = {
        0: 0,
        1: 1,
        2: 2,
        3: 3,
    }


class LocalFileSystem(FileSystem):
    """
    LocalFileSystem(use_mmap=False, *)
    
        A FileSystem implementation accessing files on the local machine.
    
        Details such as symlinks are abstracted away (symlinks are always followed,
        except when deleting an entry).
    
        Parameters
        ----------
        use_mmap : bool, default False
            Whether open_input_stream and open_input_file should return
            a mmap'ed file or a regular file.
    
        Examples
        --------
        Create a FileSystem object with LocalFileSystem constructor:
    
        >>> from pyarrow import fs
        >>> local = fs.LocalFileSystem()
        >>> local
        <pyarrow._fs.LocalFileSystem object at ...>
    
        and write data on to the file:
    
        >>> with local.open_output_stream('/tmp/local_fs.dat') as stream:
        ...     stream.write(b'data')
        4
        >>> with local.open_input_stream('/tmp/local_fs.dat') as stream:
        ...     print(stream.readall())
        b'data'
    
        Create a FileSystem object inferred from a URI of the saved file:
    
        >>> local_new, path = fs.LocalFileSystem().from_uri('/tmp/local_fs.dat')
        >>> local_new
        <pyarrow._fs.LocalFileSystem object at ...
        >>> path
        '/tmp/local_fs.dat'
    
        Check if FileSystems `local` and `local_new` are equal:
    
        >>> local.equals(local_new)
        True
    
        Compare two different FileSystems:
    
        >>> local2 = fs.LocalFileSystem(use_mmap=True)
        >>> local.equals(local2)
        False
    
        Copy a file and print out the data:
    
        >>> local.copy_file('/tmp/local_fs.dat', '/tmp/local_fs-copy.dat')
        >>> with local.open_input_stream('/tmp/local_fs-copy.dat') as stream:
        ...     print(stream.readall())
        ...
        b'data'
    
        Open an output stream for appending, add text and print the new data:
    
        >>> with local.open_append_stream('/tmp/local_fs-copy.dat') as f:
        ...     f.write(b'+newly added')
        12
    
        >>> with local.open_input_stream('/tmp/local_fs-copy.dat') as f:
        ...     print(f.readall())
        b'data+newly added'
    
        Create a directory, copy a file into it and then delete the whole directory:
    
        >>> local.create_dir('/tmp/new_folder')
        >>> local.copy_file('/tmp/local_fs.dat', '/tmp/new_folder/local_fs.dat')
        >>> local.get_file_info('/tmp/new_folder')
        <FileInfo for '/tmp/new_folder': type=FileType.Directory>
        >>> local.delete_dir('/tmp/new_folder')
        >>> local.get_file_info('/tmp/new_folder')
        <FileInfo for '/tmp/new_folder': type=FileType.NotFound>
    
        Create a directory, copy a file into it and then delete
        the content of the directory:
    
        >>> local.create_dir('/tmp/new_folder')
        >>> local.copy_file('/tmp/local_fs.dat', '/tmp/new_folder/local_fs.dat')
        >>> local.get_file_info('/tmp/new_folder/local_fs.dat')
        <FileInfo for '/tmp/new_folder/local_fs.dat': type=FileType.File, size=4>
        >>> local.delete_dir_contents('/tmp/new_folder')
        >>> local.get_file_info('/tmp/new_folder')
        <FileInfo for '/tmp/new_folder': type=FileType.Directory>
        >>> local.get_file_info('/tmp/new_folder/local_fs.dat')
        <FileInfo for '/tmp/new_folder/local_fs.dat': type=FileType.NotFound>
    
        Create a directory, copy a file into it and then delete
        the file from the directory:
    
        >>> local.create_dir('/tmp/new_folder')
        >>> local.copy_file('/tmp/local_fs.dat', '/tmp/new_folder/local_fs.dat')
        >>> local.delete_file('/tmp/new_folder/local_fs.dat')
        >>> local.get_file_info('/tmp/new_folder/local_fs.dat')
        <FileInfo for '/tmp/new_folder/local_fs.dat': type=FileType.NotFound>
        >>> local.get_file_info('/tmp/new_folder')
        <FileInfo for '/tmp/new_folder': type=FileType.Directory>
    
        Move the file:
    
        >>> local.move('/tmp/local_fs-copy.dat', '/tmp/new_folder/local_fs-copy.dat')
        >>> local.get_file_info('/tmp/new_folder/local_fs-copy.dat')
        <FileInfo for '/tmp/new_folder/local_fs-copy.dat': type=FileType.File, size=16>
        >>> local.get_file_info('/tmp/local_fs-copy.dat')
        <FileInfo for '/tmp/local_fs-copy.dat': type=FileType.NotFound>
    
        To finish delete the file left:
        >>> local.delete_file('/tmp/local_fs.dat')
    """
    @classmethod
    def _reconstruct(cls, type_cls, kwargs): # real signature unknown; restored from __doc__
        """ LocalFileSystem._reconstruct(type cls, kwargs) """
        pass

    def __init__(self, use_mmap=False, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self): # real signature unknown; restored from __doc__
        """ LocalFileSystem.__reduce__(self) """
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x00000231E06F5ED0>'


class PyFileSystem(FileSystem):
    """
    PyFileSystem(handler)
    
        A FileSystem with behavior implemented in Python.
    
        Parameters
        ----------
        handler : FileSystemHandler
            The handler object implementing custom filesystem behavior.
    
        Examples
        --------
        Create an fsspec-based filesystem object for GitHub:
    
        >>> from fsspec.implementations import github
        >>> gfs = github.GithubFileSystem('apache', 'arrow') # doctest: +SKIP
    
        Get a PyArrow FileSystem object:
    
        >>> from pyarrow.fs import PyFileSystem, FSSpecHandler
        >>> pa_fs = PyFileSystem(FSSpecHandler(gfs)) # doctest: +SKIP
    
        Use :func:`~pyarrow.fs.FileSystem` functionality ``get_file_info()``:
    
        >>> pa_fs.get_file_info('README.md') # doctest: +SKIP
        <FileInfo for 'README.md': type=FileType.File, size=...>
    """
    def __init__(self, handler): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self): # real signature unknown; restored from __doc__
        """ PyFileSystem.__reduce__(self) """
        pass

    handler = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        The filesystem's underlying handler.

        Returns
        -------
        handler : FileSystemHandler
        """


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x00000231E06FF030>'


class SubTreeFileSystem(FileSystem):
    """
    SubTreeFileSystem(base_path, FileSystem base_fs)
    
        Delegates to another implementation after prepending a fixed base path.
    
        This is useful to expose a logical view of a subtree of a filesystem,
        for example a directory in a LocalFileSystem.
    
        Note, that this makes no security guarantee. For example, symlinks may
        allow to "escape" the subtree and access other parts of the underlying
        filesystem.
    
        Parameters
        ----------
        base_path : str
            The root of the subtree.
        base_fs : FileSystem
            FileSystem object the operations delegated to.
    
        Examples
        --------
        Create a LocalFileSystem instance:
    
        >>> from pyarrow import fs
        >>> local = fs.LocalFileSystem()
        >>> with local.open_output_stream('/tmp/local_fs.dat') as stream:
        ...     stream.write(b'data')
        4
    
        Create a directory and a SubTreeFileSystem instance:
    
        >>> local.create_dir('/tmp/sub_tree')
        >>> subtree = fs.SubTreeFileSystem('/tmp/sub_tree', local)
    
        Write data into the existing file:
    
        >>> with subtree.open_append_stream('sub_tree_fs.dat') as f:
        ...     f.write(b'+newly added')
        12
    
        Print out the attributes:
    
        >>> subtree.base_fs
        <pyarrow._fs.LocalFileSystem object at ...>
        >>> subtree.base_path
        '/tmp/sub_tree/'
    
        Get info for the given directory or given file:
    
        >>> subtree.get_file_info('')
        <FileInfo for '': type=FileType.Directory>
        >>> subtree.get_file_info('sub_tree_fs.dat')
        <FileInfo for 'sub_tree_fs.dat': type=FileType.File, size=12>
    
        Delete the file and directory:
    
        >>> subtree.delete_file('sub_tree_fs.dat')
        >>> local.delete_dir('/tmp/sub_tree')
        >>> local.delete_file('/tmp/local_fs.dat')
    
        For usage of the methods see examples for :func:`~pyarrow.fs.LocalFileSystem`.
    """
    def __init__(self, base_path, FileSystem_base_fs): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self): # real signature unknown; restored from __doc__
        """ SubTreeFileSystem.__reduce__(self) """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    base_fs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    base_path = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x00000231E06F5F30>'


class timezone(__datetime.tzinfo):
    """ Fixed offset from UTC implementation of tzinfo. """
    def dst(self, *args, **kwargs): # real signature unknown
        """ Return None. """
        pass

    def fromutc(self, *args, **kwargs): # real signature unknown
        """ datetime in UTC -> datetime in local time. """
        pass

    def tzname(self, *args, **kwargs): # real signature unknown
        """ If name is specified when timezone is created, returns the name.  Otherwise returns offset as 'UTC(+|-)HH:MM'. """
        pass

    def utcoffset(self, *args, **kwargs): # real signature unknown
        """ Return fixed offset. """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __getinitargs__(self, *args, **kwargs): # real signature unknown
        """ pickle support """
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

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    max = datetime.timezone(datetime.timedelta(seconds=86340))
    min = datetime.timezone(datetime.timedelta(days=-1, seconds=60))
    utc = datetime.timezone.utc


class _MockFileSystem(FileSystem):
    """ _MockFileSystem(datetime current_time=None) """
    def __init__(self, datetime_current_time=None): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ _MockFileSystem.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ _MockFileSystem.__setstate_cython__(self, __pyx_state) """
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x00000231E06F5F90>'


# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x00000231D20FF700>'

__spec__ = None # (!) real value is "ModuleSpec(name='pyarrow._fs', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x00000231D20FF700>, origin='C:\\\\Users\\\\akharin\\\\PycharmProjects\\\\pythonProject\\\\venv\\\\lib\\\\site-packages\\\\pyarrow\\\\_fs.cp39-win_amd64.pyd')"

__test__ = {
    'FileInfo.base_name.__get__ (line 241)': "\n        The file base name.\n\n        Component after the last directory separator.\n\n        Examples\n        --------\n        >>> file_info = local.get_file_info(path)\n        >>> file_info.base_name\n        'pyarrow-fs-example.dat'\n        ",
    'FileInfo.extension.__get__ (line 271)': "\n        The file extension.\n\n        Examples\n        --------\n        >>> file_info = local.get_file_info(path)\n        >>> file_info.extension\n        'dat'\n        ",
    'FileInfo.mtime.__get__ (line 284)': '\n        The time of last modification, if available.\n\n        Returns\n        -------\n        mtime : datetime.datetime or None\n\n        Examples\n        --------\n        >>> file_info = local.get_file_info(path)\n        >>> file_info.mtime # doctest: +SKIP\n        datetime.datetime(2022, 6, 29, 7, 56, 10, 873922, tzinfo=datetime.timezone.utc)\n        ',
    'FileInfo.mtime_ns.__get__ (line 304)': '\n        The time of last modification, if available, expressed in nanoseconds\n        since the Unix epoch.\n\n        Returns\n        -------\n        mtime_ns : int or None\n\n        Examples\n        --------\n        >>> file_info = local.get_file_info(path)\n        >>> file_info.mtime_ns # doctest: +SKIP\n        1656489370873922073\n        ',
    'FileInfo.path.__get__ (line 228)': "\n        The full file path in the filesystem.\n\n        Examples\n        --------\n        >>> file_info = local.get_file_info(path)\n        >>> file_info.path\n        '/.../pyarrow-fs-example.dat'\n        ",
    'FileSystem.copy_file (line 680)': "\n        Copy a file.\n\n        If the destination exists and is a directory, an error is returned.\n        Otherwise, it is replaced.\n\n        Parameters\n        ----------\n        src : str\n            The path of the file to be copied from.\n        dest : str\n            The destination path where the file is copied to.\n\n        Examples\n        --------\n        >>> local.copy_file(path,\n        ...                 local_path + '/pyarrow-fs-example_copy.dat')\n\n        Inspect the file info:\n\n        >>> local.get_file_info(local_path + '/pyarrow-fs-example_copy.dat')\n        <FileInfo for '/.../pyarrow-fs-example_copy.dat': type=FileType.File, size=4>\n        >>> local.get_file_info(path)\n        <FileInfo for '/.../pyarrow-fs-example.dat': type=FileType.File, size=4>\n        ",
    'FileSystem.from_uri (line 424)': '\n        Create a new FileSystem from URI or Path.\n\n        Recognized URI schemes are "file", "mock", "s3fs", "gs", "gcs", "hdfs" and "viewfs".\n        In addition, the argument can be a pathlib.Path object, or a string\n        describing an absolute local path.\n\n        Parameters\n        ----------\n        uri : string\n            URI-based path, for example: file:///some/local/path.\n\n        Returns\n        -------\n        tuple of (FileSystem, str path)\n            With (filesystem, path) tuple where path is the abstract path\n            inside the FileSystem instance.\n\n        Examples\n        --------\n        Create a new FileSystem subclass from a URI:\n\n        >>> uri = \'file:///{}/pyarrow-fs-example.dat\'.format(local_path)\n        >>> local_new, path_new = fs.FileSystem.from_uri(uri)\n        >>> local_new\n        <pyarrow._fs.LocalFileSystem object at ...\n        >>> path_new\n        \'/.../pyarrow-fs-example.dat\'\n\n        Or from a s3 bucket:\n\n        >>> fs.FileSystem.from_uri("s3://usgs-landsat/collection02/")\n        (<pyarrow._s3fs.S3FileSystem object at ...>, \'usgs-landsat/collection02\')\n        ',
    'FileSystem.get_file_info (line 523)': '\n        Get info for the given files.\n\n        Any symlink is automatically dereferenced, recursively. A non-existing\n        or unreachable file returns a FileStat object and has a FileType of\n        value NotFound. An exception indicates a truly exceptional condition\n        (low-level I/O error, etc.).\n\n        Parameters\n        ----------\n        paths_or_selector : FileSelector, path-like or list of path-likes\n            Either a selector object, a path-like object or a list of\n            path-like objects. The selector\'s base directory will not be\n            part of the results, even if it exists. If it doesn\'t exist,\n            use `allow_not_found`.\n\n        Returns\n        -------\n        FileInfo or list of FileInfo\n            Single FileInfo object is returned for a single path, otherwise\n            a list of FileInfo objects is returned.\n\n        Examples\n        --------\n        >>> local\n        <pyarrow._fs.LocalFileSystem object at ...>\n        >>> local.get_file_info("/{}/pyarrow-fs-example.dat".format(local_path))\n        <FileInfo for \'/.../pyarrow-fs-example.dat\': type=FileType.File, size=4>\n        ',
    'FileSystem.move (line 636)': "\n        Move / rename a file or directory.\n\n        If the destination exists:\n        - if it is a non-empty directory, an error is returned\n        - otherwise, if it has the same type as the source, it is replaced\n        - otherwise, behavior is unspecified (implementation-dependent).\n\n        Parameters\n        ----------\n        src : str\n            The path of the file or the directory to be moved.\n        dest : str\n            The destination path where the file or directory is moved to.\n\n        Examples\n        --------\n        Create a new folder with a file:\n\n        >>> local.create_dir('/tmp/other_dir')\n        >>> local.copy_file(path,'/tmp/move_example.dat')\n\n        Move the file:\n\n        >>> local.move('/tmp/move_example.dat',\n        ...            '/tmp/other_dir/move_example_2.dat')\n\n        Inspect the file info:\n\n        >>> local.get_file_info('/tmp/other_dir/move_example_2.dat')\n        <FileInfo for '/tmp/other_dir/move_example_2.dat': type=FileType.File, size=4>\n        >>> local.get_file_info('/tmp/move_example.dat')\n        <FileInfo for '/tmp/move_example.dat': type=FileType.NotFound>\n\n        Delete the folder:\n        >>> local.delete_dir('/tmp/other_dir')\n        ",
    'FileSystem.open_append_stream (line 878)': '\n        Open an output stream for appending.\n\n        If the target doesn\'t exist, a new empty file is created.\n\n        .. note::\n            Some filesystem implementations do not support efficient\n            appending to an existing file, in which case this method will\n            raise NotImplementedError.\n            Consider writing to multiple files (using e.g. the dataset layer)\n            instead.\n\n        Parameters\n        ----------\n        path : str\n            The source to open for writing.\n        compression : str optional, default \'detect\'\n            The compression algorithm to use for on-the-fly compression.\n            If "detect" and source is a file path, then compression will be\n            chosen based on the file extension.\n            If None, no compression will be applied. Otherwise, a well-known\n            algorithm name must be supplied (e.g. "gzip").\n        buffer_size : int optional, default None\n            If None or 0, no buffering will happen. Otherwise the size of the\n            temporary write buffer.\n        metadata : dict optional, default None\n            If not None, a mapping of string keys to string values.\n            Some filesystems support storing metadata along the file\n            (such as "Content-Type").\n            Unsupported metadata keys will be ignored.\n\n        Returns\n        -------\n        stream : NativeFile\n\n        Examples\n        --------\n        Append new data to a FileSystem subclass with nonempty file:\n\n        >>> with local.open_append_stream(path) as f:\n        ...     f.write(b\'+newly added\')\n        12\n\n        Print out the content fo the file:\n\n        >>> with local.open_input_file(path) as f:\n        ...     print(f.readall())\n        b\'data+newly added\'\n        ',
    'FileSystem.open_input_file (line 743)': "\n        Open an input file for random access reading.\n\n        Parameters\n        ----------\n        path : str\n            The source to open for reading.\n\n        Returns\n        -------\n        stream : NativeFile\n\n        Examples\n        --------\n        Print the data from the file with `open_input_file()`:\n\n        >>> with local.open_input_file(path) as f:\n        ...     print(f.readall())\n        b'data'\n        ",
    'FileSystem.open_input_stream (line 776)': '\n        Open an input stream for sequential reading.\n\n        Parameters\n        ----------\n        path : str\n            The source to open for reading.\n        compression : str optional, default \'detect\'\n            The compression algorithm to use for on-the-fly decompression.\n            If "detect" and source is a file path, then compression will be\n            chosen based on the file extension.\n            If None, no compression will be applied. Otherwise, a well-known\n            algorithm name must be supplied (e.g. "gzip").\n        buffer_size : int optional, default None\n            If None or 0, no buffering will happen. Otherwise the size of the\n            temporary read buffer.\n\n        Returns\n        -------\n        stream : NativeFile\n\n        Examples\n        --------\n        Print the data from the file with `open_input_stream()`:\n\n        >>> with local.open_input_stream(path) as f:\n        ...     print(f.readall())\n        b\'data\'\n        ',
    'FileSystem.open_output_stream (line 821)': '\n        Open an output stream for sequential writing.\n\n        If the target already exists, existing data is truncated.\n\n        Parameters\n        ----------\n        path : str\n            The source to open for writing.\n        compression : str optional, default \'detect\'\n            The compression algorithm to use for on-the-fly compression.\n            If "detect" and source is a file path, then compression will be\n            chosen based on the file extension.\n            If None, no compression will be applied. Otherwise, a well-known\n            algorithm name must be supplied (e.g. "gzip").\n        buffer_size : int optional, default None\n            If None or 0, no buffering will happen. Otherwise the size of the\n            temporary write buffer.\n        metadata : dict optional, default None\n            If not None, a mapping of string keys to string values.\n            Some filesystems support storing metadata along the file\n            (such as "Content-Type").\n            Unsupported metadata keys will be ignored.\n\n        Returns\n        -------\n        stream : NativeFile\n\n        Examples\n        --------\n        >>> local = fs.LocalFileSystem()\n        >>> with local.open_output_stream(path) as stream:\n        ...     stream.write(b\'data\')\n        4\n        ',
}

