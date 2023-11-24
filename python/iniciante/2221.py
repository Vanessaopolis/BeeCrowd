# https://www.beecrowd.com.br/judge/pt/problems/view/2221
# Linguagem Python 3.11

def main():
    partidas = int(input())

    for partida in range(partidas):
        bonus = int(input())
        ataque_dabriel, defesa_dabriel, level_dabriel = list(map(int, input().split(" ")))
        ataque_guarte, defesa_guarte, level_guarte = list(map(int, input().split(" ")))

        golpe_dabriel = (ataque_dabriel + defesa_dabriel) / 2
        golpe_guarte = (ataque_guarte + defesa_guarte) / 2

        if level_dabriel % 2 == 0:
            golpe_dabriel += bonus

        if level_guarte % 2 == 0:
            golpe_guarte += bonus

        if golpe_dabriel > golpe_guarte:
            print("Dabriel")

        elif golpe_dabriel < golpe_guarte:
            print("Guarte")

        else:
            print("Empate")


if __name__ == '__main__':
    main()
