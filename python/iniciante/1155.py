# https://www.beecrowd.com.br/judge/pt/problems/view/1155
# Linguagem Python 3.11

soma = 0

for numero in range(1, 101):
    soma += 1 / numero

print(f"{soma:.2f}")
