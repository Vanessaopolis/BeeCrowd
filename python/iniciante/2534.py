# https://www.beecrowd.com.br/judge/pt/problems/view/2534
# Linguagem Python 3.11

import sys


def main():
    while True:
        quantidades = list(map(int, input().split(" ")))

        quantidade_notas, quantidade_consultas = quantidades
        notas = []

        for i in range(quantidade_notas):
            nota = int(input())
            notas.append(nota)

        notas.sort(reverse=True)

        for j in range(quantidade_consultas):
            posicao = int(input()) - 1
            print(notas[posicao])


if __name__ == '__main__':
    try:
        main()

    except EOFError:
        sys.exit()
