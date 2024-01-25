#18. Desenvolva um programa que calcule a soma dos dígitos de um número fornecido pelo
#usuário.
numero = int(input("Digite um número: "))
soma = 0

while numero > 0:
    digito = numero % 10
    soma += digito
    numero //= 10

print("A soma dos dígitos do número é:", soma)
