"""
I've used __builtins__ extensively without obfuscation. This is because the obfuscation of __builtins__ is not necessary (it's tricky, too).
"""
from .print import PRINT as print

SUPPORTED_FUNCTIONS: dict[str, str] = {'print': print}

def obfs_function(func_name: str) -> str:
    return SUPPORTED_FUNCTIONS.get(func_name, func_name)
