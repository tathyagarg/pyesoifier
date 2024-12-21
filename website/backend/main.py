import os
import random
import string
from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

import pyesoify

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

OUTPUT_DIR = Path('temp_out')

class Code(BaseModel):
    code: str


def random_string(n=10):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=n))

@app.post("/translate")
def read_root(code: Code) -> dict[str, str]:
    fname = random_string();

    out_file = OUTPUT_DIR / f'{fname}.py'

    pyesoify.esoterify(code.code, output=out_file.as_posix())

    with open(out_file, 'r') as f:
        out_code = f.read()

    os.remove(out_file)

    return {'code': out_code}

@app.get('/version')
def get_version() -> dict[str, str]:
    return {'version': pyesoify.__version__}

