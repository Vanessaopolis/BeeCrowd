# https://www.beecrowd.com.br/judge/pt/problems/view/1131
# Linguagem Python 3.11

novo_grenal = 1

inter = gremio = empate = grenais = 0

while novo_grenal != 2:

    if novo_grenal == 1:
        inter_gols, gremio_gols = [int(valor) for valor in input().split(" ")]

        if inter_gols > gremio_gols:
            inter += 1

        elif inter_gols < gremio_gols:
            gremio += 1

        else:
            empate += 1

        grenais += 1

    print("Novo grenal (1-sim 2-nao)")
    novo_grenal = int(input())

print(f"{grenais} grenais")
print(f"Inter:{inter}\nGremio:{gremio}\nEmpates:{empate}")

if inter > gremio:
    print("Inter venceu mais")
elif gremio > inter:
    print("Gremio venceu mais")
else:
    print("Nao houve vencedor")
