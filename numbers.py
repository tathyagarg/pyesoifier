"""
numbers.py
~~~~~~~~~~

This module contains the numbers used in the code.
The first ten numbers are defined through the equivalent of the following lambda calculus expressions:

TWO = lambda f: lambda x: f(f(x))
THREE = lambda f: lambda x: f(f(f(x)))
...

Where `f` is the increment function, and x is 1.
The increment function is defined as:
INCREMENT = lambda x: x.__add__(1)

This is impractical to do for larger numbers. So numbers post 10 will be defined uniquely.
"""
ONE = "(()).__eq__(())"
INCREMENT = f"lambda _:_.__add__({ONE})"

TWO = f"({INCREMENT})({ONE})"
THREE = f"({INCREMENT})({TWO})"
FOUR = f"({INCREMENT})({THREE})"
FIVE = f"({INCREMENT})({FOUR})"
SIX = f"({INCREMENT})({FIVE})"
SEVEN = f"({INCREMENT})({SIX})"
EIGHT = f"({INCREMENT})({SEVEN})"
NINE = f"({INCREMENT})({EIGHT})"
TEN = f"({INCREMENT})({NINE})"

FOURTEEN = f"{TWO}.__mul__({SEVEN})" 
FIFTEEN = f"({INCREMENT})({FOURTEEN})"

HUNDERED = f"{TEN}.__mul__({TEN})"
HUNDERED_FIFTEEN = f"({HUNDERED}).__add__({FIFTEEN})"

HUNDERED_TEN = f"(az:={TEN},az.__mul__(az).__add__(az)).__getitem__({ONE})"

