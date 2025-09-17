import time

def gcd_iterative(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def gcd_recursive(a, b):
    if b == 0:
        return a
    else:
        return gcd_recursive(b, a % b)

a, b = 213721372137, 211521152115

# i was curious about the time efficiency difference
start = time.time()
result_iter = gcd_iterative(a, b)
end = time.time()
iter_time = end - start

start = time.time()
result_rec = gcd_recursive(a, b)
end = time.time()
rec_time = end - start

print(f"Iterative GCD: {result_iter}")
print(f"Recursive GCD: {result_rec}")
print(f"Time difference (iter - rec): {iter_time - rec_time:} seconds")
#Turns out i cant make it more than 0 by any means
