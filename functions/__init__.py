"""
I've used __builtins__ extensively without obfuscation. This is because the obfuscation of __builtins__ is not necessary (it's tricky, too).
"""
from .print import PRINT 
from ._str import STR 
from .chr import CHR

SUPPORTED_FUNCTIONS: dict[str, str] = {'print': PRINT, 'str': STR, 'chr': CHR}

def obfs_function(func_name: str) -> str:
    return SUPPORTED_FUNCTIONS.get(func_name, func_name)
