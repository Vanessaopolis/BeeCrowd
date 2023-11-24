# https://www.beecrowd.com.br/judge/pt/problems/view/1165
# Linguagem Python 3.11

testes = int(input())

for teste in range(testes):
    numero = int(input())
    
    divisores = 0
    
    for x in range(1, numero + 1):
        if numero % x == 0:
            divisores += 1
    
    if divisores == 2:
        print(f"{numero} eh primo")
    
    else:
        print(f"{numero} nao eh primo")
