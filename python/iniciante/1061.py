# https://www.beecrowd.com.br/judge/pt/problems/view/1061
# Linguagem Python 3.11

dia_inicial = int(input().split(" ")[1])
hora_inicial, minuto_inicial, segundo_inicial = map(int, input().split(" : "))

dia_final = int(input().split(" ")[1])
hora_final, minuto_final, segundo_final = map(int, input().split(" : "))

DIA_PARA_SEGUNDOS = 86400
HORA_PARA_SEGUNDOS = 3600
MINUTO_PARA_SEGUNDOS = 60

segundos_inicial_total = (dia_inicial * DIA_PARA_SEGUNDOS + hora_inicial * HORA_PARA_SEGUNDOS
                          + minuto_inicial * MINUTO_PARA_SEGUNDOS + segundo_inicial)

segundos_final_total = (dia_final * DIA_PARA_SEGUNDOS + hora_final * HORA_PARA_SEGUNDOS
                        + minuto_final * MINUTO_PARA_SEGUNDOS + segundo_final)

segundos_total = segundos_final_total - segundos_inicial_total

valores_conversoes = [86400, 3600, 60, 1]
quantidades = []

for valor in valores_conversoes:
    quantidade = segundos_total // valor
    quantidades.append(quantidade)

    segundos_total = segundos_total % valor

dias, horas, minutos, segundos = quantidades

print(f"{dias:d} dia(s)\n{horas:d} hora(s)\n{minutos:d} minuto(s)\n{segundos:d} segundo(s)")
