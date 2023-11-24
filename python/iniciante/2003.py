# https://www.beecrowd.com.br/judge/pt/problems/view/2003
# Linguagem Python 3.11

def main():
    import sys

    while True:
        try:
            hora, minuto = [int(valor) for valor in input().split(":")]

            atraso = 0

            if hora + 1 >= 8:
                atraso = (hora + 1 - 8) * 60 + minuto

            print(f"Atraso maximo: {atraso}")

        except EOFError:
            sys.exit()


if __name__ == '__main__':
    main()
