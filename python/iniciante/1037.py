# https://www.beecrowd.com.br/judge/pt/problems/view/1037
# Linguagem Python 3.11

numero = float(input())

if numero < 0 or numero > 100:
    print("Fora de intervalo")

elif numero > 75:
    print("Intervalo (75,100]")

elif numero > 50:
    print("Intervalo (50,75]")

elif numero > 25:
    print("Intervalo (25,50]")

else:
    print("Intervalo [0,25]")
