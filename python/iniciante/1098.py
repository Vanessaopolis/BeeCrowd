# https://www.beecrowd.com.br/judge/pt/problems/view/1098
# Linguagem Python 3.11

i = -0.2

while i < 2:
    i = round(i + 0.2, 1)

    for j in range(1, 4):
        if i % 1 == 0:
            print(f"I={i:.0f}", end=" ")

        else:
            print(f"I={i:.1f}", end=" ")

        if (j + i) % 1 == 0:
            print(f"J={j + i:.0f}")

        else:
            print(f"J={j + i:.1f}")
