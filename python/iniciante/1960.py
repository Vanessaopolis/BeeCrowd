# https://www.beecrowd.com.br/judge/pt/problems/view/1960
# Linguagem Python 3.11

numero = int(input())

tabela_romanos = {1000: "M",
                  900: "CM",
                  500: "D",
                  400: "CD",
                  100: "C",
                  90: "XC",
                  50: "L",
                  40: "XL",
                  10: "X",
                  9: "IX",
                  5: "V",
                  4: "IV",
                  3: "III",
                  2: "II",
                  1: "I"}

numero_romano = []

for valor in tabela_romanos:
    quociente = numero // valor

    if quociente != 0:
        numero_romano.append(tabela_romanos[valor] * quociente)

        if numero == valor:
            break

        numero %= valor

print("".join(numero_romano))
