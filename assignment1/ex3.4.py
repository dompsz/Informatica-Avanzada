import random

num_parties = 5
total_seats = 50000

votes = [random.randint(2000, 10000) for _ in range(num_parties)]
print("Votes for each party:")
for i, v in enumerate(votes):
    print(f"Party {i}: {v} votes")

seats = [0] * num_parties

for _ in range(total_seats):
    quotients = [votes[i] / (seats[i] + 1) for i in range(num_parties)]
    max_index = quotients.index(max(quotients))
    seats[max_index] += 1

print("Result:")
for i, seat_count in enumerate(seats):
    print(f"Party {i}: {seat_count} seats")
