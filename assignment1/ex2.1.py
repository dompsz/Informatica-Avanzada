
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

def pick(x,y,c):
    match c:
        case "+":
            return sum(x,y)
        case "-":
            return sub(x,y)
        case "*" | "x":
            return mul(x, y)
        case "/":
            return div(x,y)
        case _:
            return 'not implemented operation'

i = float(input("first number: "))
j = float(input("second number: "))
c = input("operation (+-*x/): ")

print(pick(i,j,c))