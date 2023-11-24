# https://www.beecrowd.com.br/judge/pt/problems/view/1914
# Linguagem Python 3.11

testes = int(input())

for teste in range(testes):
    jogador1, escolha1, jogador2, escolha2 = input().split(" ")

    numero1, numero2 = [int(numero) for numero in input().split()]
    soma = numero1 + numero2

    if soma % 2 == 0:
        if escolha1 == "PAR":
            print(jogador1)
        else:
            print(jogador2)

    else:
        if escolha1 == "IMPAR":
            print(jogador1)
        else:
            print(jogador2)
