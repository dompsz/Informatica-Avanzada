registrations = ["ABC123", "AX456", "BX789", "BY111", "CZ999", "CA555"]

cars_dict = {}

for reg in registrations:
    first_letter = reg[0].upper()
    if first_letter not in cars_dict:
        cars_dict[first_letter] = []
    cars_dict[first_letter].append(reg)

letter = input("Search by letter: ").upper()

if letter in cars_dict:
    print(f"Car registrations starting with '{letter}':")
    for reg in cars_dict[letter]:
        print(reg)
else:
    print(f"No car registrations start with '{letter}'.")
