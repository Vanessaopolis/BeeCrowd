# https://www.beecrowd.com.br/judge/pt/problems/view/2152
# Linguagem Python 3.11

def main():
    testes = int(input())

    for teste in range(testes):
        hora, minuto, ocorrencia = [int(x) for x in input().split()]
        if ocorrencia:
            acao = "abriu"

        else:
            acao = "fechou"

        print(f"{hora:02d}:{minuto:02d} - A porta {acao}!")


if __name__ == '__main__':
    main()
