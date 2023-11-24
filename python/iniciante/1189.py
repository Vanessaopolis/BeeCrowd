# https://www.beecrowd.com.br/judge/pt/problems/view/1189
# Linguagem Python 3.11

operacao = input().upper()

matriz = []
linha_preenchida = []

for i in range(12):
    for j in range(12):
        numero = float(input())
        linha_preenchida.append(numero)

    matriz.append(linha_preenchida)

    linha_preenchida = []

soma = 0

for linha in range(1, 11):
    if linha <= 5:
        soma += sum(matriz[linha][: linha])

    else:
        soma += sum(matriz[linha][: 12 - linha - 1])

media = soma / 30

if operacao == "S":
    print(f"{soma:.1f}")

elif operacao == "M":
    print(f"{media:.1f}")
