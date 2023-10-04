#16. Escreva um programa que peça ao usuário para inserir uma sequência de números
#separados por vírgulas e, em seguida, calcule a média desses números.
entrada = input("Digite uma sequência de números separados por vírgulas: ")
numeros = [float(numero) for numero in entrada.split(",")]
media = sum(numeros) / len(numeros)
print(f"A média dos números é: {media}")