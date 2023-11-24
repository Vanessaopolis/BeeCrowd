# https://www.beecrowd.com.br/judge/pt/problems/view/1071
# Linguagem Python 3.11

limites_intervalo = []

for i in range(2):
    limit = int(input())
    limites_intervalo.append(limit)

limites_intervalo.sort()

PRIMEIRO = limites_intervalo[0] + 1
ULTIMO = limites_intervalo[1]

soma_impares = 0

for numero in range(PRIMEIRO, ULTIMO):
    if numero % 2 != 0:
        soma_impares += numero

print(soma_impares)
