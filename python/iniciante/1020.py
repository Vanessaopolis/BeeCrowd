# https://www.beecrowd.com.br/judge/pt/problems/view/1020
# Linguagem Python 3.11

total_dias = int(input())

valores_conversoes = [365, 30, 1]
quantidades = []

for valor in valores_conversoes:
    conversao = total_dias // valor

    quantidades.append(conversao)

    total_dias = total_dias % valor

anos, meses, dias = quantidades

print(f"{anos} ano(s)\n"
      f"{meses} mes(es)\n"
      f"{dias} dia(s)")
