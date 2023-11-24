# https://www.beecrowd.com.br/judge/pt/problems/view/2006
# Linguagem Python 3.11

def main():
    from sys import stdin

    cha_correto = int(stdin.readline())

    palpites = list(map(int, stdin.readline().split(" ")))

    print(palpites.count(cha_correto))


if __name__ == '__main__':
    main()
