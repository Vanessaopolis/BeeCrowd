# https://www.beecrowd.com.br/judge/pt/problems/view/1094
# Linguagem Python 3.11

quantidade_testes = int(input())

total = 0
coelhos = 0
ratos = 0
sapos = 0

for i in range(quantidade_testes):
    quantidade, animal = input().split(" ")

    total += int(quantidade)

    if animal == "C":
        coelhos += int(quantidade)

    elif animal == "R":
        ratos += int(quantidade)

    elif animal == "S":
        sapos += int(quantidade)

print(f"Total: {total} cobaias")
print(f"Total de coelhos: {coelhos}")
print(f"Total de ratos: {ratos}")
print(f"Total de sapos: {sapos}")
print(f"Percentual de coelhos: {(coelhos / total * 100):.2f} %")
print(f"Percentual de ratos: {(ratos / total * 100):.2f} %")
print(f"Percentual de sapos: {(sapos / total * 100):.2f} %")
