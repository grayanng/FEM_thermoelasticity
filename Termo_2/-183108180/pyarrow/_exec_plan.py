# encoding: utf-8
# module pyarrow._exec_plan
# from C:\Users\akharin\PycharmProjects\pythonProject\venv\lib\site-packages\pyarrow\_exec_plan.cp39-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
from pyarrow.lib import tobytes

from pyarrow._dataset import InMemoryDataset


# functions

def _filter_table(table, expression, output_type=None): # real signature unknown; restored from __doc__
    """
    _filter_table(table, expression, output_type=Table)
    Filter rows of a table or dataset based on the provided expression.
    
        The result will be an output table with only the rows matching
        the provided expression.
    
        Parameters
        ----------
        table : Table or Dataset
            Table or Dataset that should be filtered.
        expression : Expression
            The expression on which rows should be filtered.
        output_type: Table or InMemoryDataset
            The output type for the filtered result.
    
        Returns
        -------
        result_table : Table or InMemoryDataset
    """
    pass

def _perform_join(join_type, left_operand, left_keys, right_operand, right_keys, left_suffix=None, right_suffix=None, use_threads=True, coalesce_keys=False, output_type=None): # real signature unknown; restored from __doc__
    """
    _perform_join(join_type, left_operand, left_keys, right_operand, right_keys, left_suffix=None, right_suffix=None, use_threads=True, coalesce_keys=False, output_type=Table)
    
        Perform join of two tables or datasets.
    
        The result will be an output table with the result of the join operation
    
        Parameters
        ----------
        join_type : str
            One of supported join types.
        left_operand : Table or Dataset
            The left operand for the join operation.
        left_keys : str or list[str]
            The left key (or keys) on which the join operation should be performed.
        right_operand : Table or Dataset
            The right operand for the join operation.
        right_keys : str or list[str]
            The right key (or keys) on which the join operation should be performed.
        left_suffix : str, default None
            Which suffix to add to left column names. This prevents confusion
            when the columns in left and right operands have colliding names.
        right_suffix : str, default None
            Which suffix to add to the right column names. This prevents confusion
            when the columns in left and right operands have colliding names.
        use_threads : bool, default True
            Whether to use multithreading or not.
        coalesce_keys : bool, default False
            If the duplicated keys should be omitted from one of the sides
            in the join result.
        output_type: Table or InMemoryDataset
            The output type for the exec plan result.
    
        Returns
        -------
        result_table : Table or InMemoryDataset
    """
    pass

def _sort_source(table_or_dataset, sort_options, output_type=None): # real signature unknown; restored from __doc__
    """ _sort_source(table_or_dataset, sort_options, output_type=Table) """
    pass

# no classes
# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x0000019498AEE700>'

__spec__ = None # (!) real value is "ModuleSpec(name='pyarrow._exec_plan', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x0000019498AEE700>, origin='C:\\\\Users\\\\akharin\\\\PycharmProjects\\\\pythonProject\\\\venv\\\\lib\\\\site-packages\\\\pyarrow\\\\_exec_plan.cp39-win_amd64.pyd')"

__test__ = {}

