# https://www.beecrowd.com.br/judge/pt/problems/view/1080
# Linguagem Python 3.11

numeros = []

for i in range(100):
    number = int(input())
    numeros.append(number)

maior = max(numeros)

posicao = numeros.index(maior) + 1

print(f"{maior}\n{posicao}")
