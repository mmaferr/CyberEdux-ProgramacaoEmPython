#10. Altere o programa anterior para mostrar no final a soma dos números.

numero1 = int(input("Digite o primeiro número inteiro: "))
numero2 = int(input("Digite o segundo número inteiro: "))

menor = min(numero1, numero2)
maior = max(numero1, numero2)

soma = 0

print(f"Números inteiros no intervalo de {menor} a {maior}:")
for numero in range(menor, maior + 1):
    print(numero)
    soma += numero

print(f"A soma dos números é: {soma}")
