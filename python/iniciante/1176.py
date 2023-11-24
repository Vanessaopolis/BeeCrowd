# https://www.beecrowd.com.br/judge/pt/problems/view/1176
# Linguagem Python 3.11

testes = int(input())

for teste in range(testes):
    numero = int(input())

    fib = [0, 1]

    if numero > 1:
        n1 = 0
        n2 = 1

        while numero >= len(fib):
            n3 = n1 + n2
            fib.append(n3)
            n1 = n2
            n2 = n3

    print(f"Fib({numero}) = {fib[numero]}")
