# https://www.beecrowd.com.br/judge/pt/problems/view/1789
# Linguagem Python 3.11

import sys

while True:
    try:
        lesmas = int(input())

        velocidades = [int(v) for v in input().split(" ")]

        maior_velocidade = max(velocidades)

        if maior_velocidade >= 20:
            print("3")

        elif maior_velocidade >= 10:
            print("2")

        else:
            print("1")

    except EOFError:
        sys.exit()
