# https://www.beecrowd.com.br/judge/pt/problems/view/2551
# Linguagem Python 3.11

import sys


def main():
    while True:
        treinos = int(input())

        recorde = 0
        dias = []

        for treino in range(treinos):
            duracao, distancia = list(map(int, input().split()))

            velocidade = distancia / duracao

            if velocidade > recorde:
                recorde = velocidade
                dias.append(treino + 1)

        print("\n".join(str(d) for d in dias))


if __name__ == '__main__':
    try:
        main()

    except EOFError:
        sys.exit()
