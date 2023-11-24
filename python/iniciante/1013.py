# https://www.beecrowd.com.br/judge/pt/problems/view/1013
# Linguagem Python 3.11

numeros = [int(number) for number in input().split(" ")]

maior = max(numeros)

print(f"{maior:d} eh o maior")
