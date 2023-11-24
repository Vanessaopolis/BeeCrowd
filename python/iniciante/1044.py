# https://www.beecrowd.com.br/judge/pt/problems/view/1044
# Linguagem Python 3.11

numero_a, numero_b = sorted([int(number) for number in input().split(" ")])

if numero_b // numero_a * numero_a == numero_b:
    print("Sao Multiplos")

else:
    print("Nao sao Multiplos")
