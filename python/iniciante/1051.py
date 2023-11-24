# https://www.beecrowd.com.br/judge/pt/problems/view/1051
# Linguagem Python 3.11

salario = float(input())

if salario <= 2000:
    print("Isento")

else:

    if salario <= 3000:
        taxa = (salario - 2000) * 0.08

    elif salario <= 4500:
        taxa = 80 + (salario - 3000) * 0.18

    else:
        taxa = 350 + (salario - 4500) * 0.28

    print(f"R$ {taxa:.2f}")
