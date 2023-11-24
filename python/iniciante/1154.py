# https://www.beecrowd.com.br/judge/pt/problems/view/1154
# Linguagem Python 3.11

import sys

idades = []

while True:
    idade = int(input())

    if idade >= 0:
        idades.append(idade)

    else:
        media = sum(idades) / len(idades)
        print(f"{media:.2f}")

        sys.exit()
