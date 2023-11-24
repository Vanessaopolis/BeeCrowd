# https://www.beecrowd.com.br/judge/pt/problems/view/1045
# Linguagem Python 3.11

lado_a, lado_b, lado_c = sorted([float(lado) for lado in input().split(" ")], reverse=True)

if lado_a >= lado_b + lado_c:
    print("NAO FORMA TRIANGULO")

else:
    if lado_a ** 2 == lado_b ** 2 + lado_c ** 2:
        classificacao_angulo = "RETANGULO"

    elif lado_a ** 2 > lado_b ** 2 + lado_c ** 2:
        classificacao_angulo = "OBTUSANGULO"

    else:
        classificacao_angulo = "ACUTANGULO"

    classificacao_lado = None

    if lado_a == lado_b == lado_c:
        classificacao_lado = "EQUILATERO"

    elif lado_a == lado_b or lado_a == lado_c or lado_b == lado_c:
        classificacao_lado = "ISOSCELES"

    print(f"TRIANGULO {classificacao_angulo}")

    if classificacao_lado is not None:
        print(f"TRIANGULO {classificacao_lado}")
