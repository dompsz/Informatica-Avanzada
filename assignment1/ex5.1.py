def recursive_max(num):
    if len(num) == 1:
        return num[0]
    else:
        return max(num[0], recursive_max(num[1:]))

numbers = [3, 7, 2, 9, 5, 15]
print("Maximum value:", recursive_max(numbers))
