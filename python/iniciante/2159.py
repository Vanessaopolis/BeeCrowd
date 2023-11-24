# https://www.beecrowd.com.br/judge/pt/problems/view/2159
# Linguagem Python 3.11

def main():
    import math

    numero = int(input())

    minimo = numero / math.log(numero)
    maximo = 1.25506 * minimo

    print(f"{minimo:.1f} {maximo:.1f}")


if __name__ == '__main__':
    main()
