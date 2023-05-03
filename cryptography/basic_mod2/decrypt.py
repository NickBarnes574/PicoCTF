#!/usr/bin/env python3

# Description:
# Take each number mod 41 and find the modular inverse for the result.
# Then map to the following character set:
# 1-26 are the alphabet,
# 27-36 are the decimal digits,
# and 37 is an underscore.
# Wrap your decrypted message in the picoCTF flag format(i.e. picoCTF{decrypted_message})

MAGIC_NUMBER = 41

# Number range representing uppercase characters
ALPHA_LOWER_BOUND = 1
ALPHA_UPPER_BOUND = 26

# Number range representing digits
DIGIT_LOWER_BOUND = 27
DIGIT_UPPER_BOUND = 36

# Number representing underscore
UNDERSCORE = 37

# Start of the uppercase ASCII character set
ASCII_UPPERCASE = 65

# Start of the digit ASCII character set
ASCII_DIGIT = 48


def main():

    # open the file and save the data to a string
    with open("message.txt", "r") as file:
        data = file.read()

    # convert string to a list of integers
    num_list = list(map(int, data.split()))

    # decrypt the list
    decrypt(num_list)


def decrypt(num_list):
    result = ''
    for number in num_list:

        # Get the modular inverse
        mod_inverse = pow(number, -1, MAGIC_NUMBER)

        # Convert to uppercase character
        if mod_inverse >= ALPHA_LOWER_BOUND and mod_inverse <= ALPHA_UPPER_BOUND:
            ascii_char = chr(mod_inverse + (ASCII_UPPERCASE - 1))

        # Convert to digit
        elif mod_inverse >= DIGIT_LOWER_BOUND and mod_inverse <= DIGIT_UPPER_BOUND:
            ascii_char = chr((mod_inverse-DIGIT_LOWER_BOUND) + ASCII_DIGIT)

        # Convert to underscore
        elif mod_inverse == UNDERSCORE:
            ascii_char = '_'

        result += str(ascii_char)
    print(f"picoCTF{{{result}}}")


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt as e:
        print("Shutdown")
