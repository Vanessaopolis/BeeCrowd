# https://www.beecrowd.com.br/judge/pt/problems/view/1172
# Linguagem Python 3.11

vetor = []

for valor in range(10):
    numero = int(input())
    vetor.append(numero)

for posicao in range(len(vetor)):
    if vetor[posicao] <= 0:
        vetor[posicao] = 1

    print(f"X[{posicao}] = {vetor[posicao]}")
