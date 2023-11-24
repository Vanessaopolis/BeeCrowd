# https://www.beecrowd.com.br/judge/pt/problems/view/1099
# Linguagem Python 3.11

quantidade_testes = int(input())

for i in range(quantidade_testes):
    inicio, fim = sorted([int(numero) for numero in input().split(" ")])

    if inicio % 2 == 0:
        inicio += 1

    else:
        inicio += 2

    soma_impares = 0
    for valor in range(inicio, fim, 2):
        soma_impares += valor

    print(soma_impares)
