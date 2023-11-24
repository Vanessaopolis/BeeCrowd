# https://www.beecrowd.com.br/judge/pt/problems/view/1173
# Linguagem Python 3.11

vetor = []

numero = int(input())

for i in range(10):
    vetor.append(numero)

    numero *= 2

for posicao in range(len(vetor)):
    print(f"N[{posicao}] = {vetor[posicao]}")
