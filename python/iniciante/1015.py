# https://www.beecrowd.com.br/judge/pt/problems/view/1015
# Linguagem Python 3.11

import math


x1, y1 = [float(coordenada) for coordenada in input().split(" ")]
x2, y2 = [float(coordinate) for coordinate in input().split(" ")]

distancia = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

print(f"{distancia:.4f}")
