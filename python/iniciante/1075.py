# https://www.beecrowd.com.br/judge/pt/problems/view/1075
# Linguagem Python 3.11

numero = int(input())

for i in range(10001):
    if i % numero == 2:
        print(i)
