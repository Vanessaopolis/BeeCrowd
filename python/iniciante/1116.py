# https://www.beecrowd.com.br/judge/pt/problems/view/1116
# Linguagem Python 3.11

quantitade_casos = int(input())

for i in range(quantitade_casos):
    numero_x, numero_y = [int(valor) for valor in input().split(" ")]

    if numero_y == 0:
        print("divisao impossivel")

    else:
        print(f"{(numero_x / numero_y):.1f}")
