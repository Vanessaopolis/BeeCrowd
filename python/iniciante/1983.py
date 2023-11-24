# https://www.beecrowd.com.br/judge/pt/problems/view/1983
# Linguagem Python 3.11

from sys import stdin


def main():
    quantidade_alunos = int(stdin.readline())

    lista_notas = {}

    for aluno in range(quantidade_alunos):
        matricula, nota = stdin.readline().split(" ")

        lista_notas[int(matricula)] = float(nota)

    matricula_maior_nota = max(lista_notas, key=lista_notas.get)

    if lista_notas[matricula_maior_nota] >= 8:
        print(matricula_maior_nota)

    else:
        print("Minimum note not reached")


if __name__ == '__main__':
    main()
