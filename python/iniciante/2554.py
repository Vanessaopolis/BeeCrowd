# https://www.beecrowd.com.br/judge/pt/problems/view/2554
# Linguagem Python 3.11

import sys


def main():
    while True:
        quantidade_pessoas, quantidade_datas = list(map(int, input().split()))

        datas = []

        for data in range(quantidade_datas):
            possibilidade = input()

            posicao_final_data = possibilidade.index(" ")

            data = possibilidade[: posicao_final_data]
            votos = list(map(int, possibilidade[posicao_final_data + 1:].split()))

            if sum(votos) == quantidade_pessoas:
                datas.append(data)

        if datas:
            print(datas[0])

        else:
            print("Pizza antes de FdI")


if __name__ == '__main__':
    try:
        main()

    except EOFError:
        sys.exit()
