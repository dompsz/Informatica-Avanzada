import random

def random_sample(l, k):
    n = len(l)
    selected = []
    chosen_count = 0

    for j, item in enumerate(l, start=1):
        remaining_to_choose = k - chosen_count
        remaining_items = n - j + 1
        probability = remaining_to_choose / remaining_items
        if random.random() <= probability:
            selected.append(item)
            chosen_count += 1
        if chosen_count == k:
            break

    return selected

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
k = 3
sample = random_sample(l, k)
print("Random sample of", k, "items:", sample)
#not sure if i understood the task correctly