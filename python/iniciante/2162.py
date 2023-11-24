# https://www.beecrowd.com.br/judge/pt/problems/view/2162
# Linguagem Python 3.11

def main():
    quantidade_medidas = int(input())
    altura = list(map(int, input().split(" ")))

    padrao = True

    picos_seguidos = 0
    vales_seguidos = 0

    for medida in range(quantidade_medidas - 1):
        if altura[medida] > altura[medida + 1]:
            vales_seguidos += 1
            picos_seguidos = 0

        elif altura[medida] < altura[medida + 1]:
            picos_seguidos += 1
            vales_seguidos = 0

        if picos_seguidos != 1 or vales_seguidos != 1 or altura[medida] == altura[medida + 1]:
            padrao = False

            break

    if padrao:
        print("1")

    else:
        print("0")


if __name__ == '__main__':
    main()
