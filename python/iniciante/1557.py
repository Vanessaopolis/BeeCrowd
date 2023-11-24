# https://www.beecrowd.com.br/judge/pt/problems/view/1557
# Linguagem Python 3.11

import sys

while True:
    dimensao = int(input())

    if dimensao == 0:
        sys.exit()

    matriz = []
    linha_preenchida = []

    for i in range(dimensao):
        exp = i

        for j in range(dimensao):
            linha_preenchida.append(2 ** exp)
            exp += 1

        matriz.append(linha_preenchida)

        linha_preenchida = []

    tamanho = len(str(matriz[dimensao - 1][dimensao - 1]))

    for linha in matriz:
        texto = ""

        for coluna in linha:
            texto += f" {coluna:{tamanho}d}"

        print(texto[1:])

    print()
