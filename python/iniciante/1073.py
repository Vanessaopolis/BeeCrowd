# https://www.beecrowd.com.br/judge/pt/problems/view/1073
# Linguagem Python 3.11

numero = int(input())

for i in range(2, numero + 1, 2):
    print(f"{i:d}^2 = {i ** 2}")
