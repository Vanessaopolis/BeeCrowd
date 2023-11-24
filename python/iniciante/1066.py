# https://www.beecrowd.com.br/judge/pt/problems/view/1066
# Linguagem Python 3.11

quantidade_pares = 0
quantidade_impares = 0

quantidade_positivos = 0
quantidade_negativos = 0

for i in range(5):
    number = int(input())

    if number % 2 == 0:
        quantidade_pares += 1

    else:
        quantidade_impares += 1

    if number > 0:
        quantidade_positivos += 1

    elif number < 0:
        quantidade_negativos += 1


print(f"{quantidade_pares} valor(es) par(es)"
      f"\n{quantidade_impares} valor(es) impar(es)"
      f"\n{quantidade_positivos} valor(es) positivo(s)"
      f"\n{quantidade_negativos} valor(es) negativo(s)")
