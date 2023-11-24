# https://www.beecrowd.com.br/judge/pt/problems/view/2310
# Linguagem Python 3.11

def main():
    numero_jogadores = int(input())

    total_saques = 0
    total_bloqueios = 0
    total_ataques = 0

    total_saques_concluidos = 0
    total_bloqueios_concluidos = 0
    total_ataques_concluidos = 0

    for jogador in range(numero_jogadores):
        nome = input()
        saques, bloqueios, ataques = list(map(int, input().split(" ")))
        saques_concluidos, bloqueios_concluidos, ataques_concluidos = list(map(int, input().split(" ")))

        total_saques += saques
        total_bloqueios += bloqueios
        total_ataques += ataques

        total_saques_concluidos += saques_concluidos
        total_bloqueios_concluidos += bloqueios_concluidos
        total_ataques_concluidos += ataques_concluidos

    pontos_saques = total_saques_concluidos / total_saques * 100
    pontos_bloqueios = total_bloqueios_concluidos / total_bloqueios * 100
    pontos_ataques = total_ataques_concluidos / total_ataques * 100

    print(f"Pontos de Saque: {pontos_saques:.2f} %.\n"
          f"Pontos de Bloqueio: {pontos_bloqueios:.2f} %.\n"
          f"Pontos de Ataque: {pontos_ataques:.2f} %.")


if __name__ == '__main__':
    main()
