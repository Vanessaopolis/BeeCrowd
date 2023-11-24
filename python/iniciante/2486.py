# https://www.beecrowd.com.br/judge/pt/problems/view/2486
# Linguagem Python 3.11

import sys


def main():
    while True:
        casos = int(input())

        if casos == 0:
            sys.exit()

        consumo = 0

        for caso in range(casos):
            informacoes = input().split(" ")

            quantidade = int(informacoes[0])
            alimento = informacoes[1]

            tabela_alimentos = {"suco": 120,
                                "morango": 85,
                                "mamao": 85,
                                "goiaba": 70,
                                "manga": 56,
                                "laranja": 50,
                                "brocolis": 34}

            consumo += tabela_alimentos[alimento] * quantidade

        if consumo > 130:
            print(f"Menos {consumo - 130} mg")

        elif consumo < 110:
            print(f"Mais {110 - consumo} mg")

        else:
            print(f"{consumo} mg")


if __name__ == '__main__':
    main()
