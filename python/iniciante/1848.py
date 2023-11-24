# https://www.beecrowd.com.br/judge/pt/problems/view/1848
# Linguagem Python 3.11

gritos = 0
resultado = 0

while gritos != 3:
    sinal = input()
    
    if sinal == "caw caw":
        gritos += 1
        
        print(resultado)
        
        resultado = 0

    else:
        binario = []
        
        for elemento in reversed(sinal):

            if elemento == "*":
                binario.append(1)
            
            else:
                binario.append(0)
        
        numero = 0
        
        for i in range(3):
            numero += binario[i] * 2 ** i

        resultado += numero
