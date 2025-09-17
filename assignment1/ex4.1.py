dni_letters = "TRWAGMYFPDXBNJZSQVHLCKE"

def get_dni_letter(dni_number):
    return dni_letters[dni_number % 23]

def verify(dni_input):
    if len(dni_input) != 9 or not dni_input[:8].isdigit():
        print("Invalid format")
        return

    number = int(dni_input[:8])
    letter = dni_input[8]
    correct_letter = get_dni_letter(number)

    if letter == correct_letter:
        print(f"{dni_input} DNI is correct")
    else:
        print(f"{dni_input} is invalid. Correct letter should be {correct_letter}")
    return

verify(input("Enter DNI with a letter: ").upper())