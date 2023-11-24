# https://www.beecrowd.com.br/judge/pt/problems/view/1159
# Linguagem Python 3.11

while True:
    numero = int(input())

    if numero == 0:
        break

    elif numero % 2 == 0:
        print(sum(range(numero, numero + 10, 2)))

    else:
        print(sum(range(numero + 1, numero + 10, 2)))
