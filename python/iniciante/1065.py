# https://www.beecrowd.com.br/judge/pt/problems/view/1065
# Linguagem Python 3.11

quantidade_pares = 0

for i in range(5):
    numero = int(input())

    if numero % 2 == 0:
        quantidade_pares += 1

print(f"{quantidade_pares:d} valores pares")
