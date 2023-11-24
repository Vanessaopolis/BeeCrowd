# https://www.beecrowd.com.br/judge/pt/problems/view/1958
# Linguagem Python 3.11

numero = float(input())

if str(numero)[0] == "-":
    sinal = "-"

else:
    sinal = "+"

if abs(numero) >= 1 or numero == 0:
    sinal_expoente = "+"

    e = 0

    while abs(int(numero)) >= 10:
        numero /= 10
        e += 1

    mantissa = abs(numero)

else:
    sinal_expoente = "-"
    e = 0

    while abs(int(numero)) == 0:
        numero *= 10
        e += 1

    mantissa = abs(numero)

exp = []

if e < 10:
    exp = ["0", str(e)]

else:
    for i in str(e):
        exp.append(str(i))

print(f"{sinal}{mantissa:.4f}E{sinal_expoente}" + "".join(exp))
