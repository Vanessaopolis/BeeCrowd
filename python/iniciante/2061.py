# https://www.beecrowd.com.br/judge/pt/problems/view/2061
# Linguagem Python 3.11

def main():
    abas, acoes = list(map(int, input().split(" ")))

    for caso in range(acoes):
        acao = input().lower()

        if acao == "fechou":
            abas += 1

        elif acao == "clicou":
            abas -= 1

    print(abas)


if __name__ == '__main__':
    main()
