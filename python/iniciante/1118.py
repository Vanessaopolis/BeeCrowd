# https://www.beecrowd.com.br/judge/pt/problems/view/1118
# Linguagem Python 3.11

def validacao_notas():
    quantidade_notas_validas = 0
    notas_validas = 0

    while quantidade_notas_validas != 2:
        nota = float(input())

        if nota < 0 or nota > 10:
            print("nota invalida")

        else:
            quantidade_notas_validas += 1
            notas_validas += nota

    media = notas_validas / 2

    print(f"media = {media:.2f}")


novo_calc = 1

while novo_calc != 2:

    if novo_calc == 1:
        validacao_notas()

    print("novo calculo (1-sim 2-nao)")
    novo_calc = int(input())

