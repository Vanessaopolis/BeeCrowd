# https://www.beecrowd.com.br/judge/pt/problems/view/1072
# Linguagem Python 3.11

quantidade_numeros = int(input())

dentro = 0
fora = 0

for i in range(quantidade_numeros):
    numero = int(input())

    if 10 <= numero <= 20:
        dentro += 1

    else:
        fora += 1

print(f"{dentro} in\n{fora} out")
