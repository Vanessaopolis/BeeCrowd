# https://www.beecrowd.com.br/judge/pt/problems/view/2164
# Linguagem Python 3.11

def main():
    import math

    numero = int(input())

    raiz5 = math.sqrt(5)

    fibonacci = (((1 + raiz5) / 2) ** numero - ((1 - raiz5) / 2) ** numero) / raiz5

    print(f"{fibonacci:.1f}")


if __name__ == '__main__':
    main()
