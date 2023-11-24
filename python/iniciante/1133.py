# https://www.beecrowd.com.br/judge/pt/problems/view/1133
# Linguagem Python 3.11

numero_1 = int(input())
numero_2 = int(input())

inicio, fim = sorted([numero_1, numero_2])
inicio += 1

for i in range(inicio, fim):
    if i % 5 == 2 or i % 5 == 3:
        print(i)
