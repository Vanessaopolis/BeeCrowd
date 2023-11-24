# https://www.beecrowd.com.br/judge/pt/problems/view/1046
# Linguagem Python 3.11

hora_inicial, hora_final = [int(valor) for valor in input().split(" ")]

if hora_inicial == hora_final:
    duracao = 24

elif hora_inicial < hora_final:
    duracao = hora_final - hora_inicial

else:
    duracao = 24 - hora_inicial + hora_final

print(f"O JOGO DUROU {duracao:d} HORA(S)")
