import ast

from pyesoify.obfuscate import obfuscate


def esoterify(code: str, output: str) -> None:
    import sys
    if output:
        sys.stdout = open(output, 'w')

    print('__builtins__:', end='(')
    for elem in ast.parse(code).body:
        print(obfuscate(elem), end='')

    print(')=__import__("builtins").__dict__')
