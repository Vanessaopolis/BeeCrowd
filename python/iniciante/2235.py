# https://www.beecrowd.com.br/judge/pt/problems/view/2235
# Linguagem Python 3.11

def main():
    credito1, credito2, credito3 = sorted(list(map(int, input().split(" "))))

    if credito1 == credito2 or credito2 == credito3:
        print("S")

    elif credito3 == credito1 + credito2:
        print("S")

    else:
        print("N")


if __name__ == '__main__':
    main()
