# https://www.beecrowd.com.br/judge/pt/problems/view/1963
# Linguagem Python 3.11

valor_novo, valor_antigo = [float(x) for x in input().split(" ")]

porcentagem = (valor_antigo - valor_novo) / valor_novo * 100

print(f"{porcentagem:.2f}%")
