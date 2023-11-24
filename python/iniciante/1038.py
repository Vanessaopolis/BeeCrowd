# https://www.beecrowd.com.br/judge/pt/problems/view/1038
# Linguagem Python 3.11

codigo, quantidade = [int(item) for item in input().split(" ")]

precos = [4, 4.5, 5, 2, 1.5]

valor_total = precos[codigo - 1] * quantidade

print(f"Total: R$ {valor_total:.2f}")
