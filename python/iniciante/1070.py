# https://www.beecrowd.com.br/judge/pt/problems/view/1070
# Linguagem Python 3.11

numero = int(input())

if numero % 2 == 0:
    PRIMEIRO = numero + 1

else:
    PRIMEIRO = numero


ULTIMO = PRIMEIRO + 12

for i in range(PRIMEIRO, ULTIMO, 2):
    print(i)
