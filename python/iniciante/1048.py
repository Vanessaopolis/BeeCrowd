# https://www.beecrowd.com.br/judge/pt/problems/view/1048
# Linguagem Python 3.11

salario = float(input())

if salario > 2000:
    porcentagem = 4

elif salario > 1200:
    porcentagem = 7

elif salario > 800:
    porcentagem = 10

elif salario > 400:
    porcentagem = 12

else:
    porcentagem = 15

ajuste = salario * porcentagem / 100

novo_salario = salario + ajuste

print(f"Novo salario: {novo_salario:.2f}"
      f"\nReajuste ganho: {ajuste:.2f}"
      f"\nEm percentual: {porcentagem:d} %")
