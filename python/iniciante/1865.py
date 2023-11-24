# https://www.beecrowd.com.br/judge/pt/problems/view/1865
# Linguagem Python 3.11

testes = int(input())

for teste in range(testes):
    nome, forca = input().split(" ")

    if nome == "Thor":
        print("Y")

    else:
        print("N")
