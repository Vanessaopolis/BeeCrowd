# https://www.beecrowd.com.br/judge/pt/problems/view/1866
# Linguagem Python 3.11

testes = int(input())

for teste in range(testes):
    numero = int(input())

    if numero % 2 == 0:
        print("0")

    else:
        print("1")
