# https://www.beecrowd.com.br/judge/pt/problems/view/1158
# Linguagem Python 3.11

numero_linhas = int(input())

for numero in range(numero_linhas):
    numero_inicial, quantidade_impares = [int(a) for a in input().split()]

    if numero_inicial % 2 == 1:
        print(sum(range(numero_inicial, numero_inicial + 2 * quantidade_impares, 2)))

    else:
        print(sum(range(numero_inicial + 1, numero_inicial + 2 * quantidade_impares, 2)))
