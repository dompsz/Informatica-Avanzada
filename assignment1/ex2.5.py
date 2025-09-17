import random

n = int(input("Enter number of rolls: "))

counts = [0] * 6

for _ in range(n):
    roll = random.randint(1, 6)
    counts[roll - 1] += 1

print(f"\nResults after {n} rolls:\n")
for i in range(6):
    rel_freq = counts[i] / n
    print(f"{i+1}: occurrences = {counts[i]}, relative frequency = {rel_freq:.2%}")
