# https://www.beecrowd.com.br/judge/pt/problems/view/2533
# Linguagem Python 3.11

import sys


def main():
    while True:
        disciplinas = int(input())

        numerador = 0
        denominador = 0

        for disciplina in range(disciplinas):
            nota, carga = list(map(int, input().split(" ")))

            numerador += nota * carga
            denominador += carga * 100

        ira_media = numerador / denominador

        print(f"{ira_media:.4f}")


if __name__ == '__main__':
    try:
        main()

    except EOFError:
        sys.exit()
