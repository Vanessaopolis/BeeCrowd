# https://www.beecrowd.com.br/judge/pt/problems/view/2344
# Linguagem Python 3.11

def main():
    nota = int(input())

    if nota > 85:
        print("A")

    elif nota > 60:
        print("B")

    elif nota > 35:
        print("C")

    elif nota > 0:
        print("D")

    else:
        print("E")


if __name__ == '__main__':
    main()
