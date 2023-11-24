# https://www.beecrowd.com.br/judge/pt/problems/view/1827
# Linguagem Python 3.11

import sys
import math

while True:
    try:
        dimensao = int(input())

        matriz = []
        linha_preenchida = []

        for i in range(dimensao):
            for j in range(dimensao):
                linha_preenchida.append(0)

            matriz.append(linha_preenchida)

            linha_preenchida = []

        quadrado1 = math.trunc(dimensao / 3)

        for posicao in range(dimensao):
            matriz[posicao][posicao] = 2

            matriz[posicao][dimensao - posicao - 1] = 3

            if quadrado1 <= posicao < dimensao - quadrado1:
                matriz[posicao][quadrado1: dimensao - quadrado1] = [1] * (dimensao - 2 * quadrado1)

            matriz[math.trunc(dimensao / 2)][math.trunc(dimensao / 2)] = 4

        for linha in matriz:
            print("".join(str(elemento) for elemento in linha))

        print()

    except EOFError:
        sys.exit()
