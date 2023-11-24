# https://www.beecrowd.com.br/judge/pt/problems/view/2059
# Linguagem Python 3.11

def main():
    escolha_jogador1, numero1, numero2, jogador1_roubou, jogador2_acusou = list(map(int, input().split(" ")))

    if jogador1_roubou:
        if jogador2_acusou:
            print("Jogador 2 ganha!")

        else:
            print("Jogador 1 ganha!")
    else:
        if jogador2_acusou:
            print("Jogador 1 ganha!")

        else:
            soma = numero1 + numero2

            if (escolha_jogador1 and soma % 2 == 0) or (not escolha_jogador1 and soma % 2 != 0):
                print("Jogador 1 ganha!")

            else:
                print("Jogador 2 ganha!")


if __name__ == '__main__':
    main()
