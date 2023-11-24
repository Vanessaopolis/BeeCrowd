# https://www.beecrowd.com.br/judge/pt/problems/view/1009
# Linguagem Python 3.11

nome = input()
salario_fixo = float(input())
vendas = float(input())

salario_final = salario_fixo + 0.15 * vendas

print(f"TOTAL = R$ {salario_final:.2f}")
