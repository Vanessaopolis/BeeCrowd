# https://www.beecrowd.com.br/judge/pt/problems/view/1837
# Linguagem Python 3.11

dividendo, divisor = [int(x) for x in input().split(" ")]

quociente = dividendo // abs(divisor)
resto = dividendo % abs(divisor)

if divisor < 0:
    quociente = - quociente

print(quociente, resto)
