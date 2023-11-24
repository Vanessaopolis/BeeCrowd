# https://www.beecrowd.com.br/judge/pt/problems/view/1181
# Linguagem Python 3.11

linha_posicao = int(input())
operacao = input().upper()

matriz = []
linha = []

for i in range(12):
    for j in range(12):
        numero = float(input())
        linha.append(numero)

    matriz.append(linha)

    linha = []

soma = sum(matriz[linha_posicao])
media = soma / 12

if operacao == "S":
    print(f"{soma:.1f}")

elif operacao == "M":
    print(f"{media:.1f}")
