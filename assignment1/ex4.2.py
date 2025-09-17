import string

def create_code():
    letters = string.ascii_lowercase
    coded_letters = letters[1:] + letters[0]
    return dict(zip(letters, coded_letters))

def is_code_correct(code):
    letters = set(string.ascii_lowercase)
    return set(code.keys()) == letters and set(code.values()) == letters

def encode_string(code, s):
    return ''.join(code.get(c, c) for c in s.lower())

def main():
    code = create_code()
    if not is_code_correct(code):
        print("The code is incorrect.")
        return

    #loop or enter empty line to exit
    while True:
        line = input()
        if not line:
            break
        print(encode_string(code, line))

main()
