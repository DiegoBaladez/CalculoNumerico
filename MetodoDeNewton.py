from scipy.misc import derivative
import math

epslon = 0.0001
z = float(input("Digite o x0: "))


def f(x):
    return x * (math.log(x, 10)) - 1


def metodoDeNewtonRaphson(z):
    xBarra = z
    fBarra = f(xBarra)
    iteracoes = 0

    while (abs(fBarra) >= epslon):
        xBarraproximo = xBarra - f(xBarra) / derivative(f, xBarra)
        fBarraproximo = f(xBarraproximo)
        xBarra = xBarraproximo
        fBarra = fBarraproximo
        iteracoes += 1
    print(f"A raiz é {xBarra:5.9f} e o F({xBarra:5.9f}) = {fBarra:5.9f}. Nº de interações = {iteracoes}")
    print(f"abs({math.fabs(fBarra):5.9f})")

metodoDeNewtonRaphson(z)
