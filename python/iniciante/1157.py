# https://www.beecrowd.com.br/judge/pt/problems/view/1157
# Linguagem Python 3.11

numero = int(input())

for valor in range(1, numero + 1):
    if numero % valor == 0:
        print(valor)
