# https://www.beecrowd.com.br/judge/pt/problems/view/1973
# Linguagem Python 3.11

def main():
    from sys import stdin

    estrelas = int(stdin.readline())
    carneiros = list(map(int, stdin.readline().split()))

    total_carneiros = sum(carneiros)

    estrelas_atacadas = [0] * estrelas

    i = 0

    while 0 <= i < estrelas:
        impar = carneiros[i] % 2

        if carneiros[i] != 0:
            carneiros[i] -= 1

            total_carneiros -= 1

            estrelas_atacadas[i] = 1

        if impar:
            i += 1

        else:
            i -= 1

    ataques = estrelas_atacadas.count(1)

    print(ataques, total_carneiros)


if __name__ == '__main__':
    main()
