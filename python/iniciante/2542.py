# https://www.beecrowd.com.br/judge/pt/problems/view/2542
# Linguagem Python 3.11

import sys


def main():
    while True:
        atributos = int(input())
        cartas_marcos, cartas_leonardo = list(map(int, input().split()))
        
        baralho_marcos = []
        baralho_leonardo = []
        
        for carta_m in range(cartas_marcos):
            carta = list(map(int, input().split()))
            baralho_marcos.append(carta)

        for carta_l in range(cartas_leonardo):
            carta = list(map(int, input().split()))
            baralho_leonardo.append(carta)

        escolha_m, escolha_l = [(int(c) - 1) for c in input().split()]

        atributo = int(input()) - 1

        if baralho_marcos[escolha_m][atributo] > baralho_leonardo[escolha_l][atributo]:
            print("Marcos")

        elif baralho_marcos[escolha_m][atributo] < baralho_leonardo[escolha_l][atributo]:
            print("Leonardo")

        else:
            print("Empate")


if __name__ == '__main__':
    try:
        main()

    except EOFError:
        sys.exit()
