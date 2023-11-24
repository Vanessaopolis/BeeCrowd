# https://www.beecrowd.com.br/judge/pt/problems/view/1097
# Linguagem Python 3.11

j_inicial = 7

for i in range(1, 10, 2):

    for j in range(j_inicial, j_inicial - 3, -1):
        print(f"I={i} J={j}")

    j_inicial += 2
