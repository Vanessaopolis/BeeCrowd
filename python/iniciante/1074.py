# https://www.beecrowd.com.br/judge/pt/problems/view/1074
# Linguagem Python 3.11

quantidade_numeros = int(input())

for i in range(quantidade_numeros):
    numero = int(input())

    if numero == 0:
        print("NULL")

    else:
        if numero % 2 == 0:
            print("EVEN", end=" ")

        else:
            print("ODD", end=" ")

        if numero > 0:
            print("POSITIVE")

        else:
            print("NEGATIVE")
