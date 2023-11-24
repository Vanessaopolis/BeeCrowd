# https://www.beecrowd.com.br/judge/pt/problems/view/2031
# Linguagem Python 3.11

def main():
    testes = int(input())

    for teste in range(testes):
        jogador1 = input()
        jogador2 = input()

        if jogador1 == jogador2:
            if jogador1 == "papel":
                print("Ambos venceram")

            elif jogador1 == "pedra":
                print("Sem ganhador")

            else:
                print("Aniquilacao mutua")

        elif jogador2 != "ataque" and (jogador1 == "ataque" or jogador1 == "pedra"):
            print("Jogador 1 venceu")

        else:
            print("Jogador 2 venceu")


if __name__ == '__main__':
    main()
