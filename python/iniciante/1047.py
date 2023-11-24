# https://www.beecrowd.com.br/judge/pt/problems/view/1047
# Linguagem Python 3.11

hora_inicial, minuto_inicial, hora_final, minuto_final = [int(valor) for valor in input().split(" ")]

hora_inicial_total = hora_inicial + minuto_inicial / 60
hora_final_total = hora_final + minuto_final / 60

if hora_inicial_total == hora_final_total:
    duracao = 24

elif hora_inicial_total < hora_final_total:
    duracao = hora_final_total - hora_inicial_total

else:
    duracao = 24 - hora_inicial_total + hora_final_total

duracao_horas = int(duracao)
duracao_minutos = (duracao - duracao_horas) * 60

print(f"O JOGO DUROU {duracao_horas:d} HORA(S) E {duracao_minutos:.0f} MINUTO(S)")
