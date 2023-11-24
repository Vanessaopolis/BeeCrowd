# https://www.beecrowd.com.br/judge/pt/problems/view/1180
# Linguagem Python 3.11

N = int(input())
vetor = list(map(int, input().split()))

menor = min(vetor)
posicao = vetor.index(menor)

print(f"Menor valor: {menor}\nPosicao: {posicao}")
