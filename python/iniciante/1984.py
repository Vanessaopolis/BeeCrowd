# https://www.beecrowd.com.br/judge/pt/problems/view/1984
# Linguagem Python 3.11

def main():
    from sys import stdin, stdout

    numero = int(stdin.readline())

    print(str(numero)[::-1])


if __name__ == '__main__':
    main()
