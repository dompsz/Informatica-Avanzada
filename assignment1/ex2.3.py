import math

n = int(input("Enter number of terms: "))

s_loop = 0
for i in range(1, n + 1):
    s_loop += 6 / (i ** 2)
pi_loop = math.sqrt(s_loop)

s_list = sum(6 / (i ** 2) for i in range(1, n + 1))
pi_list = math.sqrt(s_list)

print(f"Approximation using loop: {pi_loop}")
print(f"Approximation using list comprehension: {pi_list}")
print(f"Actual math.pi: {math.pi}")

print("Difference (loop):", abs(math.pi - pi_loop))
print("Difference (list comprehension):", abs(math.pi - pi_list))
