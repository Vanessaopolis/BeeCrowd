# https://www.beecrowd.com.br/judge/pt/problems/view/1178
# Linguagem Python 3.11

numero = float(input())

vetor = []

for i in range(100):
    vetor.append(numero)

    numero /= 2

for posicao in range(len(vetor)):
    print(f"N[{posicao}] = {vetor[posicao]:.4f}")
