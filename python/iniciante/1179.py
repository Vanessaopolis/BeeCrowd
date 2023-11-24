# https://www.beecrowd.com.br/judge/pt/problems/view/1179
# Linguagem Python 3.11

par = []
impar = []

for i in range(15):
    numero = int(input())

    if numero % 2 == 0:
        par.append(numero)

    else:
        impar.append(numero)

    if len(par) == 5:
        for n in range(5):
            print(f"par[{n}] = {par[n]}")

        par = []

    if len(impar) == 5:
        for m in range(5):
            print(f"impar[{m}] = {impar[m]}")

        impar = []

for p1 in range(len(impar)):
    print(f"impar[{p1}] = {impar[p1]}")

for p2 in range(len(par)):
    print(f"par[{p2}] = {par[p2]}")
