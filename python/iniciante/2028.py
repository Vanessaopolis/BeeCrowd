# https://www.beecrowd.com.br/judge/pt/problems/view/2028
# Linguagem Python 3.11


def main():
    import sys

    caso = 1

    while True:
        try:
            numero = int(input())

            sequencia = ["0"]

            for i in range(1, numero + 1):
                for j in range(i):
                    sequencia.append(str(i))

            print(f"Caso {caso}: {len(sequencia)}", end=" ")

            if len(sequencia) > 1:
                print("numeros")

            else:
                print("numero")

            print(" ".join(sequencia))
            print()

            caso += 1

        except EOFError:
            sys.exit()


if __name__ == '__main__':
    main()
