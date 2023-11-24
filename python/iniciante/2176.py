# https://www.beecrowd.com.br/judge/pt/problems/view/2176
# Linguagem Python 3.11

def main():
    mensagem = input()
    quantidade = mensagem.count("1")

    if quantidade % 2 == 0:
        print(mensagem + "0")

    else:
        print(mensagem + "1")


if __name__ == '__main__':
    main()
