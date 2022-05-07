import math

x = float(input("Entre com o primeiro valor dointervalo: "))
y = float(input("Entre com o segundo valor do  intervalo: "))

def f(x):
    return x * (math.log(x, 10)) - 1

def metodoDasSecantes(x0, x1, iteracoes = 0):
    epslon = 0.0000001
    xAnterior = x0
    xAtual = x1


    xProximo = xAtual - (f(xAtual) * (xAtual - xAnterior)) / (f(xAtual) - f(xAnterior))

    fProxima = f(xProximo)

    if (abs(f(xProximo)) < epslon ):
        return print(f" f({xProximo:5.9f}) =  {abs(f(xProximo)):5.9f}. O numero de iterações é: {iteracoes}")
    else:
        xAnterior = xAtual
        xAtual = xProximo
        return (metodoDasSecantes(xAnterior, xAtual, iteracoes+1))

print(metodoDasSecantes(x,y))