# https://www.beecrowd.com.br/judge/pt/problems/view/1564
# Linguagem Python 3.11

import sys

while True:
    try:
        reclamacoes = int(input())

        if reclamacoes == 0:
            print("vai ter copa!")

        else:
            print("vai ter duas!")

    except EOFError:
        sys.exit()
