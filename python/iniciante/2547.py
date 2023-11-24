# https://www.beecrowd.com.br/judge/pt/problems/view/2547
# Linguagem Python 3.11

import sys


def main():
    while True:
        visitantes, minima, maxima = list(map(int, input().split()))

        autorizados = 0

        for i in range(visitantes):
            altura = int(input())

            if minima <= altura <= maxima:
                autorizados += 1

        print(autorizados)


if __name__ == '__main__':
    try:
        main()

    except EOFError:
        sys.exit()
