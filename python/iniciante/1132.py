# https://www.beecrowd.com.br/judge/pt/problems/view/1132
# Linguagem Python 3.11

numero_1 = int(input())
numero_2 = int(input())

inicio, fim = sorted([numero_1, numero_2])
fim += 1

soma = 0

for i in range(inicio, fim):
    if i // 13 * 13 != i:
        soma += i

print(soma)
