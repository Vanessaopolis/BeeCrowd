# https://www.beecrowd.com.br/judge/pt/problems/view/1049
# Linguagem Python 3.11

espinha = input().lower()
classe = input().lower()
alimentacao = input().lower()

ave = {"carnivoro": "aguia", "onivoro": "pomba"}
mamifero = {"onivoro": "homem", "herbivoro": "vaca"}

vertebrado = {"ave": ave, "mamifero": mamifero}

inseto = {"hematofago": "pulga", "herbivoro": "lagarta"}
anelideo = {"hematofago": "sanguessuga", "onivoro": "minhoca"}

invertebrado = {"inseto": inseto, "anelideo": anelideo}

arvore_animal = {"vertebrado": vertebrado, "invertebrado": invertebrado}

animal = arvore_animal[espinha][classe][alimentacao]

print(animal)
