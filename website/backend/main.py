import os
import random
import string
from pathlib import Path

from fastapi import FastAPI

import pyesoify

app = FastAPI()

INPUT_DIR = Path('temp_inp')
OUTPUT_DIR = Path('temp_out')

def random_string(n=10):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=n))

@app.post("/translate")
def read_root(code: str) -> str:
    fname = random_string();

    inp_file = INPUT_DIR / f'{fname}.py'
    out_file = OUTPUT_DIR / f'{fname}.py'

    with open(inp_file, 'w') as f:
        f.write(code)

    pyesoify.esoterify(inp_file, output=OUTPUT_DIR / f'{fname}.py')
    with open(out_file, 'r') as f:
        out_code = f.read()

    os.remove(inp_file)
    os.remove(out_file)

    return out_code
