# https://www.beecrowd.com.br/judge/pt/problems/view/2143
# Linguagem Python 3.11

def main():
    import sys

    while True:
        testes = int(input())

        if testes == 0:
            sys.exit()

        for teste in range(testes):
            pessoas = int(input())

            if pessoas % 2 == 0:
                pedidos = 2 + (pessoas - 2) * 2

            else:
                pedidos = 1 + (pessoas - 1) * 2

            print(pedidos)


if __name__ == '__main__':
    main()
