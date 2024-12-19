import ast
import functions

print(functions._str.STR)

def get_code(fpath="examples/code.py") -> str:
    with open(fpath, "r") as f:
        code = f.read()

    return code

def main(code: str) -> None:
    for elem in ast.parse(code).body:
        # print(ast.dump(elem))
        if isinstance(elem, ast.Expr):
            if isinstance(elem.value, ast.Call) \
                and isinstance(elem.value.func, ast.Name) \
                and isinstance(elem.value.func.ctx, ast.Load):
                print()
                # print(functions.obfs_function(elem.value.func.id))

if __name__ == "__main__":
    main(get_code())
