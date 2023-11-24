# https://www.beecrowd.com.br/judge/pt/problems/view/2523
# Linguagem Python 3.11

import sys


def main():
    while True:
        caracteres = input()

        numero = int(input())
        lampadas = list(map(int, input().split(" ")))

        for lampada in lampadas:
            print(caracteres[lampada - 1], end="")

        print()


if __name__ == '__main__':
    try:
        main()

    except EOFError:
        sys.exit()
