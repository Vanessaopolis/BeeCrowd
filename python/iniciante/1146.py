# https://www.beecrowd.com.br/judge/pt/problems/view/1146
# Linguagem Python 3.11

import sys

while True:
    numero = int(input())
    if numero == 0:
        sys.exit()

    else:
        print(" ".join(str(numero) for numero in range(1, numero + 1)))
