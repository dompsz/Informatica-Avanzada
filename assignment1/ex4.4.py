import random

def random_sample(l, k):
    n = len(l)
    selected = []
    chosen_count = 0
    for j, item in enumerate(l, start=1):
        remaining_to_choose = k - chosen_count
        remaining_items = n - j + 1
        if random.random() <= remaining_to_choose / remaining_items:
            selected.append(item)
            chosen_count += 1
        if chosen_count == k:
            break
    return selected

l = ['a', 'b', 'c', 'd', 'e']
k = 3
counts = {}

for _ in range(100000):
    sample = tuple(sorted(random_sample(l, k)))
    counts[sample] = counts.get(sample, 0) + 1

for comb, count in counts.items():
    print(comb, '-->', count)
