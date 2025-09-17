N = int(input("Find primes up to N: "))

if N < 2:
    print("No primes in this range.")
else:
    numbers = list(range(2, N + 1))

    for i in numbers:
        if i != 0:
            for j in range(i*2, N + 1, i):
                if j in numbers:
                    numbers[numbers.index(j)] = 0

    primes = [num for num in numbers if num != 0]

    print("Prime numbers up to", N, ":")
    print(primes)
