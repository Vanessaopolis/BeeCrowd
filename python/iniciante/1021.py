# https://www.beecrowd.com.br/judge/pt/problems/view/1021
# Linguagem Python 3.11

valor = float(input())

valor = int(valor * 100)

cedulas = [100, 50, 20, 10, 5, 2, 1, 0.50, 0.25, 0.10, 0.05, 0.01]

for nota in cedulas:
    quantidade = valor // int(nota * 100)

    if nota == 100:
        print("NOTAS:")

    elif nota == 1:
        print("MOEDAS:")

    if nota > 1:
        print(f"{quantidade} nota(s) de R$ {nota:.2f}")

    elif nota <= 1:
        print(f"{quantidade} moeda(s) de R$ {nota:.2f}")

    valor = valor % int(nota * 100)
