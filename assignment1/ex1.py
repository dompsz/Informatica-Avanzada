import math

x = int(input('number x: '))
b = int(input('base b: '))
c = int(input('new base c: '))

print("log_b(x) =", math.log(x, b))
print(" = ")
print(math.log(x, c), " / ", math.log(b, c))
