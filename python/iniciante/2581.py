# https://www.beecrowd.com.br/judge/pt/problems/view/2581
# Linguagem Python 3.11

import sys


def main():
    while True:
        casos = int(input())

        for caso in range(casos):
            pergunta = input()

            print("I am Toorg!")


if __name__ == '__main__':
    try:
        main()

    except EOFError:
        sys.exit()
