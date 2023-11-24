# https://www.beecrowd.com.br/judge/pt/problems/view/1435
# Linguagem Python 3.11

import sys

while True:
    dimensao = int(input())

    if dimensao == 0:
        sys.exit()

    else:
        matriz = []
        linha_preenchida = [0] * dimensao

        for i in range(dimensao):
            for j in range(dimensao):
                linha_preenchida.append(0)

            matriz.append(linha_preenchida)

            linha_preenchida = []

        for linha in range(dimensao):
            matriz[linha][linha + 1: dimensao - linha - 1] \
                = [linha + 1] * len(matriz[linha][linha + 1: dimensao - linha - 1])

            matriz[linha][dimensao - linha: linha] \
                = [dimensao - linha] * len(matriz[linha][dimensao - linha: linha])

            if linha < dimensao / 2:
                matriz[linha][: linha] = [e for e in range(1, linha + 1)]
                matriz[linha][dimensao - linha:] = [d for d in range(linha, 0, -1)]

            else:
                matriz[linha][: dimensao - linha - 1] = [e for e in range(1, dimensao - linha)]
                matriz[linha][linha + 1:] = [d for d in range(dimensao - linha - 1, 0, -1)]

            for coluna in range(dimensao):
                if linha == coluna:
                    if linha < dimensao / 2:
                        matriz[linha][coluna] = linha + 1

                    else:
                        matriz[linha][coluna] = dimensao - linha

                elif linha + coluna == dimensao - 1 and linha != coluna:
                    if linha < dimensao / 2:
                        matriz[linha][coluna] = dimensao - coluna

                    else:
                        matriz[linha][coluna] = dimensao - linha

        for linha in range(dimensao):
            texto = ""

            for coluna in range(dimensao):
                texto += " %3d" % matriz[linha][coluna]

            print(texto[1:])

        print()
