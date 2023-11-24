# https://www.beecrowd.com.br/judge/pt/problems/view/1175
# Linguagem Python 3.11

vetor = []

for n in range(20):
    numero = int(input())
    vetor.append(numero)

for posicao in range(10):
    temp = vetor[posicao]

    posicao_trocada = 19 - posicao

    vetor[posicao] = vetor[posicao_trocada]
    vetor[posicao_trocada] = temp

for posicao in range(20):
    print(f"N[{posicao}] = {vetor[posicao]}")
