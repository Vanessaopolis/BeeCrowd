# https://www.beecrowd.com.br/judge/pt/problems/view/1150
# Linguagem Python 3.11

numero_x = int(input())

while True:
    numero_z = int(input())

    if numero_z > numero_x:
        break

soma = 0
quantidade = 0

for x in range(numero_x, numero_z + 1):
    soma += x
    quantidade += 1

    if soma > numero_z:
        break

print(quantidade)
