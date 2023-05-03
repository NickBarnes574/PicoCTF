#!/usr/bin/env python3

ID_1 = '>'
ID_2 = '</tspan><tspan'
ID_3 = '</tspan></text>'


def main():

    with open("drawing.flag.svg", "r") as file:

        result = ''
        lines = file.readlines()
        for row in lines:

            # Search for ID_2
            if row.find(ID_2) != -1:
                start = row.index(ID_1) + 1
                end = row.index(ID_2)
                substring = row[start:end]
                result += substring

            # Search for ID_3
            if row.find(ID_3) != -1:
                start = row.index(ID_1) + 1
                end = row.index(ID_3)
                substring = row[start:end]
                result += substring

        print(result.replace(" ", ""))


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt as e:
        print("Shutdown")
