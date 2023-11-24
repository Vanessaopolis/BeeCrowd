# https://www.beecrowd.com.br/judge/pt/problems/view/1177
# Linguagem Python 3.11

limite = int(input())

vetor = []

while len(vetor) != 1000:
    for valor in range(limite):
        vetor.append(valor)

        if len(vetor) == 1000:
            break

for numero in range(len(vetor)):
    print(f"N[{numero}] = {vetor[numero]}")
