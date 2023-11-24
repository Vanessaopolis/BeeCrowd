# https://www.beecrowd.com.br/judge/pt/problems/view/2502
# Linguagem Python 3.11

import sys


def main():
    while True:
        chave, frases = list(map(int, input().split(" ")))

        cifra1 = input()
        cifra2 = input()

        cifra = cifra1 + cifra2

        for frase in range(frases):
            texto = input()

            convertido = ""

            for caractere in texto:
                if caractere.upper() in cifra:
                    posicao = cifra.find(caractere.upper()) - chave

                    if posicao < 0:
                        posicao += len(cifra)

                    if caractere == caractere.upper() and caractere != caractere.lower():
                        convertido += cifra[posicao].upper()

                    else:
                        convertido += cifra[posicao].lower()

                else:
                    convertido += caractere

            print(convertido)

        print()


if __name__ == '__main__':
    try:
        main()

    except EOFError:
        sys.exit()
