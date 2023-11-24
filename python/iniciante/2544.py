# https://www.beecrowd.com.br/judge/pt/problems/view/2544
# Linguagem Python 3.11

import sys


def main():
    while True:
        copias = int(input())
        usos = 0

        while copias // 2 != 0:
            copias = copias // 2
            usos += 1

        print(usos)


if __name__ == '__main__':
    try:
        main()

    except EOFError:
        sys.exit()
