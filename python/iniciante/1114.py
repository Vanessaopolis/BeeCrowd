# https://www.beecrowd.com.br/judge/pt/problems/view/1114
# Linguagem Python 3.11

import sys

senha = 2002

while True:
    tentativa = int(input())

    if tentativa == senha:
        print("Acesso Permitido")
        sys.exit()

    else:
        print("Senha Invalida")
