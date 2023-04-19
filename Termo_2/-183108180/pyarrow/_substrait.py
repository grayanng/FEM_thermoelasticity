# encoding: utf-8
# module pyarrow._substrait
# from C:\Users\akharin\PycharmProjects\pythonProject\venv\lib\site-packages\pyarrow\_substrait.cp39-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
from pyarrow.lib import Buffer, frombytes, py_buffer, tobytes


# functions

def get_supported_functions(): # real signature unknown; restored from __doc__
    """
    get_supported_functions()
    
        Get a list of Substrait functions that the underlying
        engine currently supports.
    
        Returns
        -------
        list[str]
            A list of function ids encoded as '{uri}#{name}'
    """
    pass

def run_query(plan, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    run_query(plan, *, table_provider=None, use_threads=True)
    
        Execute a Substrait plan and read the results as a RecordBatchReader.
    
        Parameters
        ----------
        plan : Union[Buffer, bytes]
            The serialized Substrait plan to execute.
        table_provider : object (optional)
            A function to resolve any NamedTable relation to a table.
            The function will receive a single argument which will be a list
            of strings representing the table name and should return a pyarrow.Table.
        use_threads : bool, default True
            If True then multiple threads will be used to run the query.  If False then
            all CPU intensive work will be done on the calling thread.
    
        Returns
        -------
        RecordBatchReader
            A reader containing the result of the executed query
    
        Examples
        --------
        >>> import pyarrow as pa
        >>> from pyarrow.lib import tobytes
        >>> import pyarrow.substrait as substrait
        >>> test_table_1 = pa.Table.from_pydict({"x": [1, 2, 3]})
        >>> test_table_2 = pa.Table.from_pydict({"x": [4, 5, 6]})
        >>> def table_provider(names):
        ...     if not names:
        ...        raise Exception("No names provided")
        ...     elif names[0] == "t1":
        ...        return test_table_1
        ...     elif names[1] == "t2":
        ...        return test_table_2
        ...     else:
        ...        raise Exception("Unrecognized table name")
        ... 
        >>> substrait_query = '''
        ...         {
        ...             "relations": [
        ...             {"rel": {
        ...                 "read": {
        ...                 "base_schema": {
        ...                     "struct": {
        ...                     "types": [
        ...                                 {"i64": {}}
        ...                             ]
        ...                     },
        ...                     "names": [
        ...                             "x"
        ...                             ]
        ...                 },
        ...                 "namedTable": {
        ...                         "names": ["t1"]
        ...                 }
        ...                 }
        ...             }}
        ...             ]
        ...         }
        ... '''
        >>> buf = pa._substrait._parse_json_plan(tobytes(substrait_query))
        >>> reader = pa.substrait.run_query(buf, table_provider)
        >>> reader.read_all()
        pyarrow.Table
        x: int64
        ----
        x: [[1,2,3]]
    """
    pass

def _parse_json_plan(plan): # real signature unknown; restored from __doc__
    """
    _parse_json_plan(plan)
    
        Parse a JSON plan into equivalent serialized Protobuf.
    
        Parameters
        ----------
        plan: bytes
            Substrait plan in JSON.
    
        Returns
        -------
        Buffer
            A buffer containing the serialized Protobuf plan.
    """
    pass

# no classes
# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x0000019C7FC4A910>'

__spec__ = None # (!) real value is "ModuleSpec(name='pyarrow._substrait', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x0000019C7FC4A910>, origin='C:\\\\Users\\\\akharin\\\\PycharmProjects\\\\pythonProject\\\\venv\\\\lib\\\\site-packages\\\\pyarrow\\\\_substrait.cp39-win_amd64.pyd')"

__test__ = {
    'run_query (line 51)': '\n    Execute a Substrait plan and read the results as a RecordBatchReader.\n\n    Parameters\n    ----------\n    plan : Union[Buffer, bytes]\n        The serialized Substrait plan to execute.\n    table_provider : object (optional)\n        A function to resolve any NamedTable relation to a table.\n        The function will receive a single argument which will be a list\n        of strings representing the table name and should return a pyarrow.Table.\n    use_threads : bool, default True\n        If True then multiple threads will be used to run the query.  If False then\n        all CPU intensive work will be done on the calling thread.\n\n    Returns\n    -------\n    RecordBatchReader\n        A reader containing the result of the executed query\n\n    Examples\n    --------\n    >>> import pyarrow as pa\n    >>> from pyarrow.lib import tobytes\n    >>> import pyarrow.substrait as substrait\n    >>> test_table_1 = pa.Table.from_pydict({"x": [1, 2, 3]})\n    >>> test_table_2 = pa.Table.from_pydict({"x": [4, 5, 6]})\n    >>> def table_provider(names):\n    ...     if not names:\n    ...        raise Exception("No names provided")\n    ...     elif names[0] == "t1":\n    ...        return test_table_1\n    ...     elif names[1] == "t2":\n    ...        return test_table_2\n    ...     else:\n    ...        raise Exception("Unrecognized table name")\n    ... \n    >>> substrait_query = \'\'\'\n    ...         {\n    ...             "relations": [\n    ...             {"rel": {\n    ...                 "read": {\n    ...                 "base_schema": {\n    ...                     "struct": {\n    ...                     "types": [\n    ...                                 {"i64": {}}\n    ...                             ]\n    ...                     },\n    ...                     "names": [\n    ...                             "x"\n    ...                             ]\n    ...                 },\n    ...                 "namedTable": {\n    ...                         "names": ["t1"]\n    ...                 }\n    ...                 }\n    ...             }}\n    ...             ]\n    ...         }\n    ... \'\'\'\n    >>> buf = pa._substrait._parse_json_plan(tobytes(substrait_query))\n    >>> reader = pa.substrait.run_query(buf, table_provider)\n    >>> reader.read_all()\n    pyarrow.Table\n    x: int64\n    ----\n    x: [[1,2,3]]\n    ',
}

