def apply(it1, it2, f=None):
    if f is None:
        f = lambda x, y: x + y
    for a, b in zip(it1, it2):
        yield f(a, b)

print(list(apply(range(3, 7), [1, 4, -1, 2], lambda x, y: x * y)))
print(list(apply(range(3, 7), [1, 4, -1, 2])))
