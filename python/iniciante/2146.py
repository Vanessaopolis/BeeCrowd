# https://www.beecrowd.com.br/judge/pt/problems/view/2146
# Linguagem Python 3.11

def main():
    while True:
        papel = int(input())

        print(papel - 1)


if __name__ == '__main__':
    import sys

    try:
        main()

    except EOFError:
        sys.exit()
