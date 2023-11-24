# https://www.beecrowd.com.br/judge/pt/problems/view/2166
# Linguagem Python 3.11

def main():
    repeticoes = int(input())

    numerador = 1
    denominador = 2

    for repeticao in range(repeticoes - 1):
        num = numerador
        numerador = denominador
        denominador = denominador * 2 + num

    raiz = 1

    if repeticoes != 0:
        raiz += (numerador / denominador)

    print(f"{raiz:.10f}")


if __name__ == '__main__':
    main()
