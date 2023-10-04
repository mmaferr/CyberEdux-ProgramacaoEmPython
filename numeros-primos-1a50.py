#9. Crie um programa que encontre e imprima os números primos entre 1 e 50.
def is_primo(numero):
    if numero < 2:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True

for numero in range(1, 51):
    if is_primo(numero):
        print(numero)