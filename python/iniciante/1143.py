# https://www.beecrowd.com.br/judge/pt/problems/view/1143
# Linguagem Python 3.11

numero_linhas = int(input())

for linha in range(1, numero_linhas + 1):
    print(f"{linha} {linha ** 2} {linha ** 3}")
