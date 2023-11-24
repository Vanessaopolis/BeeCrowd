# https://www.beecrowd.com.br/judge/pt/problems/view/2139
# Linguagem Python 3.11

def main():
    while True:
        mes, dia = list(map(int, input().split(" ")))

        if mes == 12:
            if dia == 25:
                print("E natal!")

            elif dia == 24:
                print("E vespera de natal!")

            elif dia > 25:
                print("Ja passou!")

            else:
                print(f"Faltam {25 - dia} dias para o natal!")

        else:
            dias = 0

            while mes != 12:

                if mes == 2:
                    dias += 29 - dia

                elif (mes <= 7 and mes % 2 != 0) or (mes > 7 and mes % 2 == 0):
                    dias += 31 - dia

                else:
                    dias += 30 - dia

                dia = 0
                mes += 1

            dias += 25

            print(f"Faltam {dias} dias para o natal!")


if __name__ == '__main__':
    import sys

    try:
        main()

    except EOFError:
        sys.exit()
