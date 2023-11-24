# https://www.beecrowd.com.br/judge/pt/problems/view/2167
# Linguagem Python 3.11

def main():
    testes = int(input())
    lista_rotacoes = list(map(int, input().split(" ")))

    posicao_queda = 0

    for rotacao in range(testes)[1:]:
        if lista_rotacoes[rotacao] < lista_rotacoes[rotacao - 1]:
            posicao_queda = rotacao + 1

            break

    print(posicao_queda)


if __name__ == '__main__':
    main()
