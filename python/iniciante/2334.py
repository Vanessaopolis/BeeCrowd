# https://www.beecrowd.com.br/judge/pt/problems/view/2334
# Linguagem Python 3.11

import sys


def main():
    while True:
        patos = int(input())

        if patos < 0:
            sys.exit()

        elif patos == 0:
            print("0")

        else:
            print(patos - 1)


if __name__ == '__main__':
    main()
