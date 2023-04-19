# encoding: utf-8
# module pyarrow._json
# from C:\Users\akharin\PycharmProjects\pythonProject\venv\lib\site-packages\pyarrow\_json.cp39-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import pyarrow.lib as __pyarrow_lib


# functions

def read_json(input_file, read_options=None, parse_options=None, MemoryPool_memory_pool=None): # real signature unknown; restored from __doc__
    """
    read_json(input_file, read_options=None, parse_options=None, MemoryPool memory_pool=None)
    
        Read a Table from a stream of JSON data.
    
        Parameters
        ----------
        input_file : str, path or file-like object
            The location of JSON data. Currently only the line-delimited JSON
            format is supported.
        read_options : pyarrow.json.ReadOptions, optional
            Options for the JSON reader (see ReadOptions constructor for defaults).
        parse_options : pyarrow.json.ParseOptions, optional
            Options for the JSON parser
            (see ParseOptions constructor for defaults).
        memory_pool : MemoryPool, optional
            Pool to allocate Table memory from.
    
        Returns
        -------
        :class:`pyarrow.Table`
            Contents of the JSON file as a in-memory table.
    """
    pass

# classes

class ParseOptions(__pyarrow_lib._Weakrefable):
    """
    ParseOptions(explicit_schema=None, newlines_in_values=None, unexpected_field_behavior=None)
    
        Options for parsing JSON files.
    
        Parameters
        ----------
        explicit_schema : Schema, optional (default None)
            Optional explicit schema (no type inference, ignores other fields).
        newlines_in_values : bool, optional (default False)
            Whether objects may be printed across multiple lines (for example
            pretty printed). If false, input must end with an empty line.
        unexpected_field_behavior : str, default "infer"
            How JSON fields outside of explicit_schema (if given) are treated.
    
            Possible behaviors:
    
             - "ignore": unexpected JSON fields are ignored
             - "error": error out on unexpected JSON fields
             - "infer": unexpected JSON fields are type-inferred and included in
               the output
    """
    def __init__(self, explicit_schema=None, newlines_in_values=None, unexpected_field_behavior=None): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self): # real signature unknown; restored from __doc__
        """ ParseOptions.__reduce__(self) """
        pass

    explicit_schema = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Optional explicit schema (no type inference, ignores other fields)
        """

    newlines_in_values = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Whether newline characters are allowed in JSON values.
        Setting this to True reduces the performance of multi-threaded
        JSON reading.
        """

    unexpected_field_behavior = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        How JSON fields outside of explicit_schema (if given) are treated.

        Possible behaviors:

         - "ignore": unexpected JSON fields are ignored
         - "error": error out on unexpected JSON fields
         - "infer": unexpected JSON fields are type-inferred and included in
           the output

        Set to "infer" by default.
        """


    __slots__ = ()


class ReadOptions(__pyarrow_lib._Weakrefable):
    """
    ReadOptions(use_threads=None, block_size=None)
    
        Options for reading JSON files.
    
        Parameters
        ----------
        use_threads : bool, optional (default True)
            Whether to use multiple threads to accelerate reading
        block_size : int, optional
            How much bytes to process at a time from the input stream.
            This will determine multi-threading granularity as well as
            the size of individual chunks in the Table.
    """
    def __init__(self, use_threads=None, block_size=None): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self): # real signature unknown; restored from __doc__
        """ ReadOptions.__reduce__(self) """
        pass

    block_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        How much bytes to process at a time from the input stream.

        This will determine multi-threading granularity as well as the size of
        individual chunks in the Table.
        """

    use_threads = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Whether to use multiple threads to accelerate reading.
        """


    __slots__ = ()


# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x000001D873B5A910>'

__spec__ = None # (!) real value is "ModuleSpec(name='pyarrow._json', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x000001D873B5A910>, origin='C:\\\\Users\\\\akharin\\\\PycharmProjects\\\\pythonProject\\\\venv\\\\lib\\\\site-packages\\\\pyarrow\\\\_json.cp39-win_amd64.pyd')"

__test__ = {}

