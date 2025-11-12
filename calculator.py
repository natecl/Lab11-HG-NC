# https://github.com/natecl/Lab11-HG-NC.git
# Partner 1: Hanna Green
# Partner 2: Nathan Chin-Lue

"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math

def square_root(a):
    try:
        return math.sqrt(a)
    except ValueError:
        return ValueError
def hypotenuse(a, b):
    return math.hypot(a, b)

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    if a==0:
        raise ZeroDivisionError("Cannot divide by zero")
    return b/a

def log(a,b):
    if a<=0 or a==1:
        raise ValueError("invalid base for logarithm")
    if b<=0:
        raise ValueError("invalid argument for logarithm")
    return math.log(a, b)

def exp(a,b):
    return a**b

