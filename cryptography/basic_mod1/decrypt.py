#!/usr/bin/env python3

# Description:
# Take each number mod 37 and map it to the following character set:
# 0-25 is the alphabet (uppercase),
# 26-35 are the decimal digits,
# and 36 is an underscore.
# Wrap your decrypted message in the picoCTF flag format (i.e. picoCTF{decrypted_message})

MAGIC_NUMBER = 37

# Number range representing uppercase characters
ALPHA_LOWER_BOUND = 0
ALPHA_UPPER_BOUND = 25

# Number range representing digits
DIGIT_LOWER_BOUND = 26
DIGIT_UPPER_BOUND = 35

# Number representing underscore
UNDERSCORE = 36

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
        mod = number % MAGIC_NUMBER

        # Convert to uppercase character
        if mod >= ALPHA_LOWER_BOUND and mod <= ALPHA_UPPER_BOUND:
            ascii_char = chr(mod + ASCII_UPPERCASE)

        # Convert to digit
        elif mod >= DIGIT_LOWER_BOUND and mod <= DIGIT_UPPER_BOUND:
            ascii_char = chr((mod-DIGIT_LOWER_BOUND) + ASCII_DIGIT)

        # Convert to underscore
        elif mod == UNDERSCORE:
            ascii_char = '_'

        result += str(ascii_char)
    print(f"picoCTF{{{result}}}")


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt as e:
        print("Shutdown")
