# https://www.beecrowd.com.br/judge/pt/problems/view/2493
# Linguagem Python 3.11

import sys


def main():
    while True:
        numero_expressoes = int(input())

        expressoes = []

        for numero in range(numero_expressoes):
            expressao = input()
            expressoes.append(expressao)

        perdedores = []

        for caso in range(numero_expressoes):
            nome, indice, operacao = input().split()
            indice = int(indice)

            espaco = expressoes[indice - 1].index(" ")
            igual = expressoes[indice - 1].index("=")

            x = int(expressoes[indice - 1][: espaco])
            y = int(expressoes[indice - 1][espaco + 1: igual])
            z = int(expressoes[indice - 1][igual + 1:])

            if x + y == z:
                if operacao != "+":
                    perdedores.append(nome)

            elif x - y == z:
                if operacao != "-":
                    perdedores.append(nome)

            elif x * y == z:
                if operacao != "*":
                    perdedores.append(nome)

            else:
                if operacao != "I":
                    perdedores.append(nome)

        if len(perdedores) == 0:
            print("You Shall All Pass!")

        elif len(perdedores) == numero_expressoes:
            print("None Shall Pass!")

        else:
            print(" ".join(sorted(perdedores)))


if __name__ == '__main__':
    try:
        main()

    except EOFError:
        sys.exit()
