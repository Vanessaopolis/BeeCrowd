# https://www.beecrowd.com.br/judge/pt/problems/view/1142
# Linguagem Python 3.11

numero_linhas = int(input())

for linha in range(numero_linhas):
    colunas = [1 + 4 * linha, 2 + 4 * linha, 3 + 4 * linha, "PUM"]

    print(" ".join(str(coluna) for coluna in colunas))
