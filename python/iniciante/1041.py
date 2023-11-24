# https://www.beecrowd.com.br/judge/pt/problems/view/1041
# Linguagem Python 3.11

x, y = [float(coordenada) for coordenada in input().split(" ")]

if x == y == 0:
    print("Origem")

elif x == 0 != y:
    print("Eixo Y")

elif y == 0 != x:
    print("Eixo X")

elif x > 0 and y > 0:
    print("Q1")

elif x < 0 < y:
    print("Q2")

elif x < 0 and y < 0:
    print("Q3")

else:
    print("Q4")
