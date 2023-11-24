# https://www.beecrowd.com.br/judge/pt/problems/view/2029
# Linguagem Python 3.11

def main():
    import sys

    while True:
        try:
            volume = float(input())
            diametro = float(input())

            PI = 3.14

            area = PI * diametro ** 2 / 4

            altura = volume / area

            print(f"ALTURA = {altura:.2f}\n"
                  f"AREA = {area:.2f}")

        except EOFError:
            sys.exit()


if __name__ == '__main__':
    main()
