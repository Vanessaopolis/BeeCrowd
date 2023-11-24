# https://www.beecrowd.com.br/judge/pt/problems/view/2140
# Linguagem Python 3.11

def main():
    import sys

    while True:
        valor_venda, valor_recebido = list(map(int, input().split(" ")))

        if valor_venda == valor_recebido == 0:
            sys.exit()

        troco = valor_recebido - valor_venda
        notas = [2, 5, 10, 20, 50, 100]

        possibilidade = "impossible"

        for nota in notas:
            if abs(troco - nota) in notas:
                possibilidade = "possible"

                break

        print(possibilidade)


if __name__ == '__main__':
    main()
