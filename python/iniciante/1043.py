# https://www.beecrowd.com.br/judge/pt/problems/view/1043
# Linguagem Python 3.11

lado_a, lado_b, lado_c = [float(lado) for lado in input().split(" ")]

if (abs(lado_b - lado_c) < lado_a < lado_b + lado_c
        and abs(lado_a - lado_c) < lado_b < lado_a + lado_c
        and abs(lado_a - lado_b) < lado_c < lado_a + lado_b):

    perimetro_triangulo = lado_a + lado_b + lado_c

    print(f"Perimetro = {perimetro_triangulo:.1f}")

else:
    area_trapezio = (lado_a + lado_b) * lado_c / 2

    print(f"Area = {area_trapezio:.1f}")
