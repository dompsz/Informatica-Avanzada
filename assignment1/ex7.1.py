def sum_iterables(it1, it2):
    for a, b in zip(it1, it2):
        yield a + b

print(list(sum_iterables(range(3, 6), [1, 4, -1])))
