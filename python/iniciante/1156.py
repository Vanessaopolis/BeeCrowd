# https://www.beecrowd.com.br/judge/pt/problems/view/1156
# Linguagem Python 3.11

soma = 0
sequencia = range(1, 40, 2)

for valor in sequencia:
    soma += valor / 2 ** sequencia.index(valor)

print(f"{soma:.2f}")
