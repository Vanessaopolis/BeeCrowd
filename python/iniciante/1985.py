# https://www.beecrowd.com.br/judge/pt/problems/view/1985
# Linguagem Python 3.11

def main():
    from sys import stdin

    tabela_valores = {1001: 1.5,
                      1002: 2.5,
                      1003: 3.5,
                      1004: 4.5,
                      1005: 5.5}

    quantidade_produtos = int(stdin.readline())

    total = 0

    for produto in range(quantidade_produtos):
        codigo, quantidade = list(map(int, stdin.readline().split(" ")))

        total += tabela_valores[codigo] * quantidade

    print(f"{total:.2f}")


if __name__ == '__main__':
    main()
