# https://www.beecrowd.com.br/judge/pt/problems/view/1134
# Linguagem Python 3.11

codigo = 0

alcool = 0
gasolina = 0
diesel = 0

while codigo != 4:
    codigo = int(input())

    if codigo == 1:
        alcool += 1

    elif codigo == 2:
        gasolina += 1

    elif codigo == 3:
        diesel += 1

print(f"MUITO OBRIGADO\n"
      f"Alcool: {alcool}\n"
      f"Gasolina: {gasolina}\n"
      f"Diesel: {diesel}")
