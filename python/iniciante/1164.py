# https://www.beecrowd.com.br/judge/pt/problems/view/1164
# Linguagem Python 3.11

testes = int(input())

for teste in range(testes):
    numero = int(input())

    soma = 0

    for valor in range(1, numero):
        if numero % valor == 0:
            soma += valor

    if soma == numero:
        print(f"{numero} eh perfeito")

    else:
        print(f"{numero} nao eh perfeito")
