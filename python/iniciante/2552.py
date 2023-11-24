# https://www.beecrowd.com.br/judge/pt/problems/view/2552
# Linguagem Python 3.11

import sys


def main():
    while True:
        linhas, colunas = list(map(int, input().split()))

        paes = []
        tabuleiro = []

        for i in range(linhas):
            linha_preenchida = list(map(int, input().split()))

            paes.append(linha_preenchida)
            tabuleiro.append([0] * colunas)

        for linha in range(linhas):
            for coluna in range(colunas):
                if paes[linha][coluna] == 1:
                    tabuleiro[linha][coluna] = 9

                else:
                    celula_acima = 0
                    celula_abaixo = 0
                    celula_esquerda = 0
                    celula_direita = 0

                    if linha != linhas - 1:
                        celula_abaixo = paes[linha + 1][coluna]

                    if linha != 0:
                        celula_acima = paes[linha - 1][coluna]

                    if coluna != colunas - 1:
                        celula_direita = paes[linha][coluna + 1]

                    if coluna != 0:
                        celula_esquerda = paes[linha][coluna - 1]

                    soma = celula_acima + celula_abaixo + celula_direita + celula_esquerda

                    tabuleiro[linha][coluna] = soma

        for linha_tab in tabuleiro:
            print("".join(str(valor) for valor in linha_tab))


if __name__ == '__main__':
    try:
        main()

    except EOFError:
        sys.exit()
