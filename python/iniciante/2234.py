# https://www.beecrowd.com.br/judge/pt/problems/view/2234
# Linguagem Python 3.11

def main():
    consumidos, pessoas = list(map(int, input().split(" ")))

    print(f"{consumidos / pessoas:.2f}")


if __name__ == '__main__':
    main()
