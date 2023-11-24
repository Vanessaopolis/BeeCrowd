# https://www.beecrowd.com.br/judge/pt/problems/view/2168
# Linguagem Python 3.11

def main():
    numero = int(input())
    cameras_esquinas = []

    for esquina in range(numero + 1):
        esquina_preenchida = list(map(int, input().split(" ")))
        cameras_esquinas.append(esquina_preenchida)

    quadras = []

    for linha in range(numero):
        seguranca_rua = []

        for coluna in range(numero):
            quadra = [cameras_esquinas[linha][coluna: coluna + 2], cameras_esquinas[linha + 1][coluna: coluna + 2]]

            if sum(quadra[0]) + sum(quadra[1]) >= 2:
                seguranca_rua.append("S")

            else:
                seguranca_rua.append("U")

        quadras.append(seguranca_rua)

    for rua in quadras:
        print("".join(rua))


if __name__ == '__main__':
    main()
