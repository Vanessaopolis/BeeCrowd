# https://www.beecrowd.com.br/judge/pt/problems/view/1067
# Linguagem Python 3.11

numero = int(input())

for i in range(1, numero, 2):
    print(i)

if numero % 2 != 0:
    print(numero)
