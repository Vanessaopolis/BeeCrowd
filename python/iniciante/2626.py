# https://www.beecrowd.com.br/judge/pt/problems/view/2626
# Linguagem Python 3.11

import sys


def main():

    while True:
        jogada_dodo, jogada_leo, jogada_pepper = input().lower().split()

        possibilidades_decisivas = [["pedra", "tesoura", "tesoura"],
                                    ["papel", "pedra", "pedra"],
                                    ["tesoura", "papel", "papel"]]

        if [jogada_dodo, jogada_leo, jogada_pepper] in possibilidades_decisivas:
            print("Os atributos dos monstros vao ser inteligencia, sabedoria...")

        elif [jogada_leo, jogada_dodo, jogada_pepper] in possibilidades_decisivas:
            print("Iron Maiden's gonna get you, no matter how far!")

        elif [jogada_pepper, jogada_dodo, jogada_leo] in possibilidades_decisivas:
            print("Urano perdeu algo muito precioso...")

        else:
            print("Putz vei, o Leo ta demorando muito pra jogar...")


if __name__ == '__main__':
    try:
        main()

    except EOFError:
        sys.exit()
