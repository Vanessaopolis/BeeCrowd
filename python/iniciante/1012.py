# https://www.beecrowd.com.br/judge/pt/problems/view/1012
# Linguagem Python 3.11

lado_a, lado_b, lado_c = [float(lado) for lado in input().split()]

area_triangulo = lado_a * lado_c / 2
area_circulo = 3.14159 * lado_c ** 2
area_trapezio = (lado_a + lado_b) * lado_c / 2
area_quadrado = lado_b ** 2
area_retangulo = lado_a * lado_b

print(f"TRIANGULO: {area_triangulo:.3f}")
print(f"CIRCULO: {area_circulo:.3f}")
print(f"TRAPEZIO: {area_trapezio:.3f}")
print(f"QUADRADO: {area_quadrado:.3f}")
print(f"RETANGULO: {area_retangulo:.3f}")
