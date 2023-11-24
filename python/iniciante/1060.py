# https://www.beecrowd.com.br/judge/pt/problems/view/1060
# Linguagem Python 3.11

quantidade_positivos = 0

for i in range(6):
    numero = float(input())

    if numero > 0:
        quantidade_positivos += 1

print(f"{quantidade_positivos:d} valores positivos")
