# https://www.beecrowd.com.br/judge/pt/problems/view/2126
# Linguagem Python 3.11

def main():
    import sys

    caso = 1

    while True:
        try:
            numero1 = int(input())
            numero2 = int(input())

            numero1 = str(numero1)
            numero2 = str(numero2)

            if numero1 not in numero2:
                print(f"Caso #{caso}:\nNao existe subsequencia\n")

            else:
                quantidade_subsedquencia = numero2.count(numero1)
                posicao = numero2.rfind(numero1) + 1

                print(f"Caso #{caso}:\n"
                      f"Qtd.Subsequencias: {quantidade_subsedquencia}\n"
                      f"Pos: {posicao}\n")

            caso += 1

        except EOFError:
            sys.exit()


if __name__ == '__main__':
    main()