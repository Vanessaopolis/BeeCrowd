# https://www.beecrowd.com.br/judge/pt/problems/view/1149
# Linguagem Python 3.11

valores = [int(x) for x in input().split()]

posicao_positivo = 1
soma = 0

while valores[posicao_positivo] <= 0:
    posicao_positivo += 1

for valor in range(valores[posicao_positivo]):
    soma += valores[0] + valor

print(soma)
