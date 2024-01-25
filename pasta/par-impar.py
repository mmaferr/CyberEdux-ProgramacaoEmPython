#1.Escreva um programa que peça ao usuário para inserir um número e, em seguida, imprima se o número é par ou ímpar.

numero = int(input("Digite um número: "))

if numero % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")
