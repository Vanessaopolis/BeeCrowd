# https://www.beecrowd.com.br/judge/pt/problems/view/1929
# Linguagem Python 3.11

valores = [int(x) for x in input().split()]

lado_a, lado_b, lado_c, lado_d = sorted(valores, reverse=True)

resposta = "N"

for i in range(2):
    if lado_a < lado_b + lado_c:
        resposta = "S"
        break

    else:
        lado_a = lado_b
        lado_b = lado_c
        lado_c = lado_d

print(resposta)
