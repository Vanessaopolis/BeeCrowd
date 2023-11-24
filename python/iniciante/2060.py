# https://www.beecrowd.com.br/judge/pt/problems/view/2060
# Linguagem Python 3.11

def main():
    casos = int(input())

    numeros = list(map(int, input().split(" ")))

    multiplo2 = 0
    multiplo3 = 0
    multiplo4 = 0
    multiplo5 = 0

    for numero in numeros:
        if numero % 2 == 0:
            multiplo2 += 1

        if numero % 3 == 0:
            multiplo3 += 1

        if numero % 4 == 0:
            multiplo4 += 1

        if numero % 5 == 0:
            multiplo5 += 1

    print(f"{multiplo2} Multiplo(s) de 2\n"
          f"{multiplo3} Multiplo(s) de 3\n"
          f"{multiplo4} Multiplo(s) de 4\n"
          f"{multiplo5} Multiplo(s) de 5")


if __name__ == '__main__':
    main()
