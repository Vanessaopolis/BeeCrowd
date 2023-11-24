# https://www.beecrowd.com.br/judge/pt/problems/view/1035
# Linguagem Python 3.11

numero_a, numero_b, numero_c, numero_d = [int(numero) for numero in input().split(" ")]

condicao1 = numero_b > numero_c
condicao2 = numero_d > numero_a
condicao3 = (numero_c + numero_d) > (numero_a + numero_b)
condicao4 = numero_c, numero_d > 0
condicao5 = (numero_a % 2) == 0

if condicao1 and condicao2 and condicao3 and condicao4 and condicao5:
    print("Valores aceitos")

else:
    print("Valores nao aceitos")
