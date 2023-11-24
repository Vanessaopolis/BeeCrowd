# https://www.beecrowd.com.br/judge/pt/problems/view/1144
# Linguagem Python 3.11

numero_linhas = int(input())

for linha in range(1, numero_linhas + 1):
    print(f"{linha + 1} {linha ** 2} {linha ** 3}")

    print(f"{linha + 1} {linha ** 2 + 1} {linha ** 3 + 1}")
