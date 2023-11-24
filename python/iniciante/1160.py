# https://www.beecrowd.com.br/judge/pt/problems/view/1160
# Linguagem Python 3.11

casos = int(input())

for valor in range(casos):
    populacaoA, populacaoB, crescimentoA, crescimentoB = [float(x) for x in input().split(" ")]

    anos = 0

    while populacaoA <= populacaoB:
        populacaoA += int(populacaoA * crescimentoA / 100)
        populacaoB += int(populacaoB * crescimentoB / 100)
        anos += 1

        if anos > 100:
            print("Mais de 1 seculo.")
            break

    if anos <= 100:
        print(f"{anos} anos.")
