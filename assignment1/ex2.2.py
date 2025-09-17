v1 = [int(x) for x in input("Enter 3 numbers for vector 1 (separated by spaces): ").split()]
v2 = [int(x) for x in input("Enter 3 numbers for vector 2 (separated by spaces): ").split()]

dot_product = sum(v1[i] * v2[i] for i in range(3))

print("Dot product:", dot_product)
