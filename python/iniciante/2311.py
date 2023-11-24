# https://www.beecrowd.com.br/judge/pt/problems/view/2311
# Linguagem Python 3.11

def main():
    competidores = int(input())

    for competidor in range(competidores):
        nome = input()
        dificuldade = float(input())
        notas = sorted(list(map(float, input().split(" "))))

        resultado = sum(notas[1:len(notas) - 1]) * dificuldade

        print(f"{nome} {resultado:.2f}")


if __name__ == '__main__':
    main()
