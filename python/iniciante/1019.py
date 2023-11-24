# https://www.beecrowd.com.br/judge/pt/problems/view/1019
# Linguagem Python 3.11

segundos_total = int(input())

valores_conversoes = [3600, 60, 1]

for valor in valores_conversoes:
    conversao = segundos_total // valor

    if valor != 1:
        print(conversao, end=":")

    else:
        print(conversao)

    segundos_total = segundos_total % valor

