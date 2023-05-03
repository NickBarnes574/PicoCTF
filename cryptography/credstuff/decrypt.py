#!/usr/bin/env python3

import linecache

# Description:
# Find the password of the user 'cultiris' and successfully
# decrypt it. The first user in usernames.txt corresponds to the
# first password in passwords.txt. The second user corresponds to
# the second password, and so on.

USERNAME = 'cultiris'
ROT_0 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
ROT_13 = 'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm'


def main():

    # open the file and save the data to a string
    with open("leak/usernames.txt", "r") as usernames:

        lines = usernames.readlines()
        for row in lines:

            # Return the line number if USERNAME is found
            if row.find(USERNAME) != -1:

                # Since index is zero-based, add 1 for offset
                line_num = lines.index(row) + 1

    # Get the password associated with the username
    password = linecache.getline('leak/passwords.txt', line_num)

    # Run a ROT_13 caesar cipher
    decrypt(password)


def decrypt(password):

    # Rotate alphabet characters
    cipher = password.maketrans(ROT_0, ROT_13)

    # Translate the cipher
    result = password.translate(cipher)

    print(result)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt as e:
        print("Shutdown")
