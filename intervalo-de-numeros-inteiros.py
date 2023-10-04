#9. Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.

numero1 = int(input("Digite o primeiro número inteiro: "))
numero2 = int(input("Digite o segundo número inteiro: "))

menor = min(numero1, numero2)
maior = max(numero1, numero2)

print(f"Números inteiros no intervalo de {menor} a {maior}:")
for numero in range(menor, maior + 1):
    print(numero)
