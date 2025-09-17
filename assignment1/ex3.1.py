import re

def sum(x,y):
    return x + y

def sub(x,y):
    return x - y

def mul(x,y):
    return x * y

def div(x,y):
    if y == 0:
        return "division error"
    return x / y

def pick(o):
    #regex handling the operations including negative numbers and floats
    match = re.fullmatch(r'\s*([-+]?\d*\.?\d+)\s*([+\-*/x])\s*([-+]?\d*\.?\d+)\s*', o)
    if not match:
        return "invalid input"

    x = float(match.group(1))
    c = match.group(2)
    y = float(match.group(3))

    match c:
        case "+":
            return sum(x,y)
        case "-":
            return sub(x,y)
        case "*" | "x":
            return mul(x,y)
        case "/":
            return div(x,y)
        case _:
            return "not implemented operation"

print(pick(input("Enter operation: ")))