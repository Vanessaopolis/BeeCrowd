# https://www.beecrowd.com.br/judge/pt/problems/view/1858
# Linguagem Python 3.11

quantidade_pessoas = int(input())
pessoas = [int(valor) for valor in input().split(" ")]

escolha = min(pessoas)

print(pessoas.index(escolha) + 1)
