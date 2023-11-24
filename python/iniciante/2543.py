# https://www.beecrowd.com.br/judge/pt/problems/view/2543
# Linguagem Python 3.11

import sys


def main():
    while True:
        gameplays, id_aluno = list(map(int, input().split()))

        jogo_cs = 0

        for n in range(gameplays):
            id_gameplay, jogo = list(map(int, input().split()))

            if jogo == 0 and id_gameplay == id_aluno:
                jogo_cs += 1

        print(jogo_cs)


if __name__ == '__main__':
    try:
        main()

    except EOFError:
        sys.exit()
