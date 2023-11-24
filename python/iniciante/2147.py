# https://www.beecrowd.com.br/judge/pt/problems/view/2147
# Linguagem Python 3.11

def main():
    testes = int(input())

    for teste in range(testes):
        texto = input()

        tempo = 0.01 * len(texto)

        print(f"{tempo:.2f}")


if __name__ == '__main__':
    main()
