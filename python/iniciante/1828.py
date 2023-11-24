# https://www.beecrowd.com.br/judge/pt/problems/view/1828
# Linguagem Python 3.11

hierarquias = [["tesoura", "papel"],
               ["papel", "pedra"],
               ["pedra", "lagarto"],
               ["lagarto", "Spock"],
               ["Spock", "tesoura"],
               ["tesoura", "lagarto"],
               ["lagarto", "papel"],
               ["papel", "Spock"],
               ["Spock", "pedra"],
               ["pedra", "tesoura"]]

testes = int(input())

for teste in range(testes):
    sheldon, raj = input().split(" ")

    if [sheldon, raj] in hierarquias:
        resultado_final = "Bazinga!"

    elif [raj, sheldon] in hierarquias:
        resultado_final = "Raj trapaceou!"

    else:
        resultado_final = "De novo!"

    print(f"Caso #{teste + 1}: {resultado_final}")
