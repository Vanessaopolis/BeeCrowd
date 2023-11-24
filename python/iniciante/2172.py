# https://www.beecrowd.com.br/judge/pt/problems/view/2172
# Linguagem Python 3.11

def main():
    while True:
        aumento, experiencia = list(map(int, input().split(" ")))

        if aumento == experiencia == 0:
            break

        print(aumento * experiencia)


if __name__ == '__main__':
    main()
