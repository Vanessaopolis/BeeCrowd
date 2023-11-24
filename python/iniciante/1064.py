# https://www.beecrowd.com.br/judge/pt/problems/view/1064
# Linguagem Python 3.11

soma_positivos = 0
quantidade_positivos = 0

for i in range(6):
    numero = float(input())

    if numero > 0:
        soma_positivos += numero
        quantidade_positivos += 1

media = soma_positivos / quantidade_positivos

print(f"{quantidade_positivos:d} valores positivos\n{media:.1f}")
