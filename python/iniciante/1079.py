# https://www.beecrowd.com.br/judge/pt/problems/view/1079
# Linguagem Python 3.11

quantidade_medias = int(input())

for i in range(quantidade_medias):
    nota1, nota2, nota3 = [float(valor) for valor in input().split(" ")]

    media = (nota1 * 2 + nota2 * 3 + nota3 * 5) / 10

    print(f"{media:.1f}")
