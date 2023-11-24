# https://www.beecrowd.com.br/judge/pt/problems/view/1589
# Linguagem Python 3.11

testes = int(input())

for teste in range(testes):
    raio1, raio2 = [int(raio) for raio in input().split(" ")]

    print(raio1 + raio2)
