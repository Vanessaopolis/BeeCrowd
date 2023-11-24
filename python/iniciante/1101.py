# https://www.beecrowd.com.br/judge/pt/problems/view/1101
# Linguagem Python 3.11

import sys

while True:
    inicio, fim = sorted([int(valor) for valor in input().split(" ")])

    if inicio <= 0 or fim <= 0:
        sys.exit()

    numeros = range(inicio, fim + 1)

    for numero in numeros:
        print(numero, end=" ")

    print(f"Sum={sum(numeros)}")