# https://www.beecrowd.com.br/judge/pt/problems/view/1957
# Linguagem Python 3.11

numero = int(input())

tabela = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "A", "B", "C", "D", "E", "F"]

if numero < 16:
    print(tabela[numero])
else:
    hexadecimal = []

    while numero != 0:
        quociente, resto = divmod(numero, 16)
        hexadecimal.append(tabela[resto])

        numero = quociente

    hexadecimal.reverse()

    print("".join(str(item) for item in hexadecimal))
