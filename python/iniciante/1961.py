# https://www.beecrowd.com.br/judge/pt/problems/view/1961
# Linguagem Python 3.11

pulo, canos = [int(x) for x in input().split(" ")]

alturas = [int(y) for y in input().split(" ")]

resultado = "YOU WIN"

for i in range(canos - 1):
    if abs(alturas[i] - alturas[i + 1]) > pulo:
        resultado = "GAME OVER"

        break

print(resultado)


