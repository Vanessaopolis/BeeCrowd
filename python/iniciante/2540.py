# https://www.beecrowd.com.br/judge/pt/problems/view/2540
# Linguagem Python 3.11

import sys


def main():
    while True:
        jogadores = int(input())

        votos = list(map(int, input().split(" ")))

        if sum(votos) >= 2 / 3 * jogadores:
            print("impeachment")

        else:
            print("acusacao arquivada")


if __name__ == '__main__':
    try:
        main()

    except EOFError:
        sys.exit()
