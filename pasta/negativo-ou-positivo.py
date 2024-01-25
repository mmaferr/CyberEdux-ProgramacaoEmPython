#5. Crie um programa que determine se um número fornecido pelo usuário é positivo, negativo ou zero

numero = float(input("Digite um número: "))

if numero > 0:
    print("O número é positivo.")
elif numero < 0:
    print("O número é negativo.")
else:
    print("O número é zero.")
