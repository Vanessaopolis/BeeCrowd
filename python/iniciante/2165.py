# https://www.beecrowd.com.br/judge/pt/problems/view/2165
# Linguagem Python 3.11

def main():
    texto = input()

    if len(texto) <= 140:
        print("TWEET")

    else:
        print("MUTE")


if __name__ == '__main__':
    main()
