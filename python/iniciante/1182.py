# https://www.beecrowd.com.br/judge/pt/problems/view/1182
# Linguagem Python 3.11

coluna_posicao = int(input())
operacao = input().upper()

matriz = []
linha = []

for i in range(12):
    for j in range(12):
        numero = float(input())
        linha.append(numero)

    matriz.append(linha)

    linha = []

soma = 0

for linha in matriz:
    soma += linha[coluna_posicao]

media = soma / 12

if operacao == "S":
    print(f"{soma:.1f}")
elif operacao == "M":
    print(f"{media:.1f}")
