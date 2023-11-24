# https://www.beecrowd.com.br/judge/pt/problems/view/2313
# Linguagem Python 3.11

def main():
    lado_a, lado_b, lado_c = sorted(list(map(int, input().split(" "))))

    if lado_c >= lado_a + lado_b:
        print("Invalido")

    else:
        if lado_a == lado_b == lado_c:
            print("Valido-Equilatero")

        elif lado_a != lado_b != lado_c:
            print("Valido-Escaleno")

        else:
            print("Valido-Isoceles")

        if lado_c ** 2 == lado_a ** 2 + lado_b ** 2:
            print("Retangulo: S")

        else:
            print("Retangulo: N")


if __name__ == '__main__':
    main()
