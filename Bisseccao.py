import math

a = float(input("Digite o primeiro intervalo 'a': "))
b = float(input("Digite o segundo intervalo 'b': "))

tolerancia = 0.0000001


def f(x):
    return x * (math.log(x, 10)) - 1


if (f(a) * f(b) >= 0):
    print("Acabou")

iteracoes = 0


def bisseccao(a, b):
    iteracoes = 0
    while (abs(b - a) >= tolerancia):

        pontoMedio = (a + b) / 2.0

        if (f(pontoMedio) == 0):
            print(f"A CHURREIA dessa equação é igual a: {pontoMedio:5.9f} e o número de iterações é: {iteracoes}")
            break

        if (f(pontoMedio) * f(a) < 0):
            b = pontoMedio
        else:
            a = pontoMedio
        iteracoes += 1
    print(f"A raiz dessa equação é igual a: {pontoMedio:5.9f} e o número de iterações é: {iteracoes}. F({pontoMedio}) = {math.fabs(f(pontoMedio)):10.15f}")


bisseccao(a, b)
