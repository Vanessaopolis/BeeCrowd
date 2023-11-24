# https://www.beecrowd.com.br/judge/pt/problems/view/2163
# Linguagem Python 3.11

def main():
    linhas, colunas = list(map(int, input().split(" ")))

    terreno = []

    for linha in range(linhas):
        linha_completa = list(map(int, input().split(" ")))
        terreno.append(linha_completa)

    x = y = 0

    for linha in range(1, linhas - 1):
        for coluna in range(1, colunas - 1):
            celula = terreno[linha][coluna]

            acima = terreno[linha - 1][coluna]
            abaixo = terreno[linha + 1][coluna]
            esquerda = terreno[linha][coluna - 1]
            direita = terreno[linha][coluna + 1]

            superior_esquerda = terreno[linha - 1][coluna - 1]
            inferior_esquerda = terreno[linha + 1][coluna - 1]
            superior_direita = terreno[linha - 1][coluna + 1]
            inferior_direita = terreno[linha + 1][coluna + 1]

            if celula == 42 and (acima == abaixo == esquerda == direita ==
                                 superior_esquerda == inferior_esquerda == superior_direita == inferior_direita == 7):
                x = linha + 1
                y = coluna + 1

                break

    print(x, y)


if __name__ == '__main__':
    main()
