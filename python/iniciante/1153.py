# https://www.beecrowd.com.br/judge/pt/problems/view/1153
# Linguagem Python 3.11

numero = int(input())

fatorial = 1

for valor in range(1, numero + 1):
    fatorial *= valor

print(fatorial)
