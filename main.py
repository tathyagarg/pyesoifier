import ast
import functions
import operators
import numbers
from typing import Any
import string_factory

def get_code(fpath="examples/code.py") -> str:
    with open(fpath, "r") as f:
        code = f.read()

    return code

def obfs_type(value: Any) -> str:
    if isinstance(value, str):
        return string_factory.make_string(value)
    if isinstance(value, int):
        return numbers.obfs_number(value)
    return str(value)

def obfs_name(name: str) -> str:
    return name + str(abs(hash(name)))

def obfuscate(elem):
    if isinstance(elem, ast.Expr):
        if isinstance(elem.value, ast.Call) \
            and isinstance(elem.value.func, ast.Name) \
            and isinstance(elem.value.func.ctx, ast.Load):
            params = map(lambda arg: obfuscate(arg), elem.value.args)

            return functions.obfs_function(elem.value.func.id) + '(' + ','.join(params) + ')' + ','
    elif isinstance(elem, ast.Assign):
        return obfuscate(elem.targets[0]) + ':=' + obfuscate(elem.value) + ','
    elif isinstance(elem, ast.BinOp):
        return f"{obfuscate(elem.left)}.{operators.obfs_operator(elem.op)}({obfuscate(elem.right)})" 
    elif isinstance(elem, ast.Constant):
        return obfs_type(elem.value)
    elif isinstance(elem, ast.Name):
        return obfs_name(elem.id)
    return ''
    


def main(code: str) -> None:
    print('__builtins__: ', end='(')
    for elem in ast.parse(code).body:
        print(obfuscate(elem))

    print(')=__import__("builtins").__dict__')

if __name__ == "__main__":
    main(get_code())
