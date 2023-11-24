# https://www.beecrowd.com.br/judge/pt/problems/view/1040
# Linguagem Python 3.11

nota1, nota2, nota3, nota4 = [float(note) for note in input().split(" ")]

media = (nota1 * 2 + nota2 * 3 + nota3 * 4 + nota4) / 10

print(f"Media: {media:.1f}")

if media >= 7:
    print(f"Aluno aprovado.")

elif media >= 5:
    print(f"Aluno em exame.")

    exame_final = float(input())

    print(f"Nota do exame: {exame_final:.1f}")

    media_final = (media + exame_final) / 2

    if media_final >= 5:
        print(f"Aluno aprovado.")

    else:
        print(f"Aluno reprovado.")

    print(f"Media final: {media_final:.1f}")

else:
    print(f"Aluno reprovado.")
