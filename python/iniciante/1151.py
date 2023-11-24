# https://www.beecrowd.com.br/judge/pt/problems/view/1151
# Linguagem Python 3.11

numero = int(input())

if numero == 1:
    print("0")

elif numero == 2:
    print("0 1")

elif numero > 2:
    fibonacci = [0, 1]

    n1 = 0
    n2 = 1
    n = 2

    while n != numero:
        n3 = n1 + n2

        fibonacci.append(n3)
        
        n1 = n2
        n2 = n3
        n += 1

    print(" ".join(str(x) for x in fibonacci))
