# https://www.beecrowd.com.br/judge/pt/problems/view/2203
# Linguagem Python 3.11

import math
import sys


def main():
    while True:

        (x_fiddlesticks,
         y_fiddlesticks,
         x_invasor,
         y_invasor,
         velocidade_invasor,
         raio_conjuracao,
         raio_corvos) = list(map(int, input().split(" ")))

        alcance_poder = raio_conjuracao + raio_corvos
        distancia_inicial = math.sqrt((x_fiddlesticks - x_invasor) ** 2 + (y_fiddlesticks - y_invasor) ** 2)
        distancia_final = distancia_inicial + 1.5 * velocidade_invasor

        if distancia_final > alcance_poder:
            print("N")

        else:
            print("Y")


if __name__ == '__main__':
    try:
        main()

    except EOFError:
        sys.exit()
