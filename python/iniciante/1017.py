# https://www.beecrowd.com.br/judge/pt/problems/view/1017
# Linguagem Python 3.11

horas = int(input())
velocidade = int(input())

CAR_CONSUMPTION = 12

litros = horas * velocidade / 12

print(f"{litros:.3f}")
