import math

a = float(input("Digite o primeiro intervalo 'a': "))
b = float(input("Digite o segundo intervalo 'b': "))

tolerancia = 0.0001


def f(x):
    return x * (math.log(x, 10)) - 1


if (f(a) * f(b) >= 0):
    print("Acabou")


def FalsaPosicao(a, b):
    iteracoes = 0
    while ((b - a) >= tolerancia and iteracoes <= 100):

        pontoMedio = ((a * f(b)) - (b * f(a))) / (f(b) - f(a))

        if (f(pontoMedio) == 0):
            break
            print(pontoMedio)

        if (f(pontoMedio) * f(a) < 0):
            b = pontoMedio
        else:
            a = pontoMedio
        iteracoes += 1
    print(f"A raiz dessa equação é igual a: {pontoMedio} e o número de iterações é: {iteracoes}")
    print(f"A funcão f({pontoMedio}) = {f(pontoMedio):5.9f}")

FalsaPosicao(a, b)
