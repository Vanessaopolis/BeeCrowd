# https://www.beecrowd.com.br/judge/pt/problems/view/2057
# Linguagem Python 3.11

def main():
    horario_saida, duracao_viagem, diferenca_hora = list(map(int, input().split(" ")))

    horario_chegada = horario_saida + duracao_viagem + diferenca_hora

    if horario_chegada >= 24:
        horario_chegada -= 24

    elif horario_chegada < 0:
        horario_chegada += 24

    print(horario_chegada)


if __name__ == '__main__':
    main()

