# https://www.beecrowd.com.br/judge/pt/problems/view/1050
# Linguagem Python 3.11

ddd = int(input())

lista_cidades = {61: "Brasilia",
                 71: "Salvador",
                 11: "Sao Paulo",
                 21: "Rio de Janeiro",
                 32: "Juiz de Fora",
                 19: "Campinas",
                 27: "Vitoria",
                 31: "Belo Horizonte"}

if ddd in lista_cidades:
    print(lista_cidades[ddd])

else:
    print("DDD nao cadastrado")
