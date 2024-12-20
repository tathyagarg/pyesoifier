import os
import random
import string
from pathlib import Path

from fastapi import FastAPI
from pydantic import BaseModel

import pyesoify

app = FastAPI()

OUTPUT_DIR = Path('temp_out')

class Code(BaseModel):
    code: str


def random_string(n=10):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=n))

@app.post("/translate")
def read_root(code: Code) -> str:
    fname = random_string();

    out_file = OUTPUT_DIR / f'{fname}.py'

    with open(out_file, 'w') as f:
        pyesoify.esoterify(code.code, output=f)

    with open(out_file, 'r') as f:
        out_code = f.read()

    os.remove(out_file)

    return out_code
