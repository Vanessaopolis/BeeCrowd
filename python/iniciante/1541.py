# https://www.beecrowd.com.br/judge/pt/problems/view/1541
# Linguagem Python 3.11

import sys
import math

while True:
    valores = [int(x) for x in input().split()]

    if valores == [0]:
        sys.exit()

    else:
        lado_a, lado_b, lado_c = valores

        area_total = lado_a * lado_b

        area_terreno = area_total * 100 / lado_c

        lado = math.trunc(math.sqrt(area_terreno))

        print(lado)
