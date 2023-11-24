# https://www.beecrowd.com.br/judge/pt/problems/view/1018
# Linguagem Python 3.11

valor = int(input())

print(f"{valor:d}")

cedulas = [100, 50, 20, 10, 5, 2, 1]

for nota in cedulas:
    quantidade = valor // nota

    print(f"{quantidade} nota(s) de R$ {nota},00")

    valor = valor % nota
