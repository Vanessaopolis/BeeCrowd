# https://www.beecrowd.com.br/judge/pt/problems/view/1036
# Linguagem Python 3.11

import math

a, b, c = [float(paremetro) for paremetro in input().split(" ")]

delta = b ** 2 - 4 * a * c

if a == 0 or delta < 0:
    print("Impossivel calcular")

else:
    raiz1 = (-b + math.sqrt(delta)) / (2 * a)
    raiz2 = (-b - math.sqrt(delta)) / (2 * a)

    print(f"R1 = {raiz1:.5f}\n"
          f"R2 = {raiz2:.5f}")
