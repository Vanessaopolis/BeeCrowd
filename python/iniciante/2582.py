# https://www.beecrowd.com.br/judge/pt/problems/view/2582
# Linguagem Python 3.11

def main():
    casos = int(input())

    musica = ["PROXYCITY", "P.Y.N.G.", "DNSUEY!",
              "SERVERS", "HOST!", "CRIPTONIZE",
              "OFFLINE DAY", "SALT", "ANSWER!",
              "RAR?", "WIFI ANTENNAS"]

    for teste in range(casos):
        posicao_escolhida = sum(list(map(int, input().split())))

        print(musica[posicao_escolhida])


if __name__ == '__main__':
    main()
