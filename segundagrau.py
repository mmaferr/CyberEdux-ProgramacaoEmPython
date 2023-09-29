#fazer um programa que calcula as raízes de uma equação de segundo grau.

import math

def calcular_raizes(a, b, c):
    # Calcula o discriminante
    discriminante = b**2 - 4*a*c

    # Verifica o valor do discriminante
    if discriminante > 0:
        # Duas raízes reais diferentes
        raiz1 = (-b + math.sqrt(discriminante)) / (2*a)
        raiz2 = (-b - math.sqrt(discriminante)) / (2*a)
        return raiz1, raiz2
    elif discriminante == 0:
        # Uma raiz real (raízes iguais)
        raiz1 = -b / (2*a)
        return raiz1
    else:
        # Raízes complexas (não reais)
        parte_real = -b / (2*a)
        parte_imaginaria = math.sqrt(abs(discriminante)) / (2*a)
        raiz1 = complex(parte_real, parte_imaginaria)
        raiz2 = complex(parte_real, -parte_imaginaria)
        return raiz1, raiz2

# Solicita os coeficientes ao usuário
a = float(input("Digite o coeficiente a: "))
b = float(input("Digite o coeficiente b: "))
c = float(input("Digite o coeficiente c: "))

# Chama a função para calcular as raízes
raizes = calcular_raizes(a, b, c)

# Exibe o resultado
if isinstance(raizes, tuple):
    print(f"As raízes da equação são: {raizes[0]} e {raizes[1]}")
elif isinstance(raizes, float):
    print(f"A raiz da equação é: {raizes}")
else:
    print(f"As raízes da equação são complexas: {raizes[0]} e {raizes[1]}")
