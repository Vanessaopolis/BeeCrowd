# https://www.beecrowd.com.br/judge/pt/problems/view/1534
# Linguagem Python 3.11

import sys

while True:
    try:
        dimensao = int(input())

        matriz = []
        linha_preenchida = []

        for i in range(dimensao):
            for j in range(dimensao):
                if i + j == dimensao - 1:
                    linha_preenchida.append(2)

                elif i == j:
                    linha_preenchida.append(1)

                else:
                    linha_preenchida.append(3)

            matriz.append(linha_preenchida)

            linha_preenchida = []

        for linha in matriz:
            print("".join(str(elemento) for elemento in linha))

    except EOFError:
        sys.exit()
