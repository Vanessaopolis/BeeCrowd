# https://www.beecrowd.com.br/judge/pt/problems/view/1145
# Linguagem Python 3.11

quantidade_colunas, numero = [int(valor) for valor in input().split(" ")]

coluna = 1

for numero in range(1, numero + 1):
    if coluna != quantidade_colunas:
        print(numero, end=" ")

        coluna += 1

    else:
        print(numero)

        coluna = 1
