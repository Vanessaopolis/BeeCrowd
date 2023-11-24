# https://www.beecrowd.com.br/judge/pt/problems/view/1174
# Linguagem Python 3.11

vetor = []

for i in range(100):
    numero = float(input())
    vetor.append(numero)


for posicao in range(len(vetor)):
    if vetor[posicao] <= 10:
        print(f"A[{posicao}] = {vetor[posicao]:.1f}")
