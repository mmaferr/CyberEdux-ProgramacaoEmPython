#17. Crie um programa que solicite ao usuário para inserir um número e imprima se ele é
#primo ou não.
numero = int(input("Digite um número: "))

def is_primo(numero):
    if numero < 2:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True

if is_primo(numero):
    print("O número é primo.")
else:
    print("O número não é primo.")