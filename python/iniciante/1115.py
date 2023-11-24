# https://www.beecrowd.com.br/judge/pt/problems/view/1115
# Linguagem Python 3.11

import sys

while True:
    x, y = [int(coordenada) for coordenada in input().split(" ")]

    if x > 0 and y > 0:
        print("primeiro")

    elif x < 0 < y:
        print("segundo")

    elif x < 0 and y < 0:
        print("terceiro")

    elif x > 0 > y:
        print("quarto")

    else:
        sys.exit()
