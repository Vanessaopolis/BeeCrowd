# https://www.beecrowd.com.br/judge/pt/problems/view/1478
# Linguagem Python 3.11

import sys

while True:
    dimensao = int(input())

    if dimensao == 0:
        sys.exit()

    else:
        matriz = []
        linha_preenchida = []

        for i in range(dimensao):
            for j in range(dimensao):
                linha_preenchida.append(0)

            matriz.append(linha_preenchida)

            linha_preenchida = []

        for linha in range(dimensao):
            for coluna in range(dimensao):
                matriz[linha][coluna] = abs(linha - coluna) + 1

        for linha in matriz:
            texto = ""

            for coluna in linha:
                texto += f" {coluna:3d}"

            print(texto[1:])

        print()
