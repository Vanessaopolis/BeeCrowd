# https://www.beecrowd.com.br/judge/pt/problems/view/1962
# Linguagem Python 3.11

testes = int(input())

for teste in range(testes):
    anos = int(input())

    if anos >= 2015:
        print(f"{anos - 2015 + 1} A.C.")

    else:
        print(f"{2015 - anos} D.C.")
