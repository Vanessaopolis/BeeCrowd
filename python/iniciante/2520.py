# https://www.beecrowd.com.br/judge/pt/problems/view/2520
# Linguagem Python 3.11

import sys


def main():
    while True:
        linhas, colunas = list(map(int, input().split(" ")))

        matriz = []

        for i in range(linhas):
            linha_nova = list(map(int, input().split(" ")))

            matriz.append(linha_nova)

        x2 = y2 = x1 = y1 = 0

        for linha in range(linhas):
            for coluna in range(colunas):
                if matriz[linha][coluna] == 1:
                    x1 = linha
                    y1 = coluna

                elif matriz[linha][coluna] == 2:
                    x2 = linha
                    y2 = coluna

        tempo = abs(x1 - x2) + abs(y1 - y2)

        print(tempo)


if __name__ == '__main__':
    try:
        main()

    except EOFError:
        sys.exit()
