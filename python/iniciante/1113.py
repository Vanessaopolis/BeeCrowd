# https://www.beecrowd.com.br/judge/pt/problems/view/1113
# Linguagem Python 3.11

import sys

while True:
    numero_x, numero_y = [int(valor) for valor in input().split(" ")]

    if numero_x == numero_y:
        sys.exit()

    elif numero_x > numero_y:
        print("Decrescente")

    else:
        print("Crescente")
