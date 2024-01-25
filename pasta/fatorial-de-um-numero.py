#14. Desenvolva um programa que calcule o fatorial de um número inserido pelo usuário.
numero = int(input("Digite um número para calcular o fatorial: "))
fatorial = 1

if numero < 0:
    print("Fatorial não definido para números negativos.")
elif numero == 0:
    print("O fatorial de 0 é 1.")
else:
    for i in range(1, numero + 1):
        fatorial *= i
    print(f"O fatorial de {numero} é {fatorial}.")
