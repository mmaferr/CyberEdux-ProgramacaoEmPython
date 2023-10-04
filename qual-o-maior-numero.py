#6. Faça um programa que leia 5 números e informe o maior número.
def maior(x, y, z, a, d):
    max = x

    if y > max:
        max = y
    if z > max:
        max = z

    if a > max:
        max = a

    if d > max:
        max = d

    return max

def menu():
    x = int(input('Primeiro numero: '))
    y = int(input('Segundo numero : '))
    z = int(input('Terceiro numero: '))
    a = int(input('Quarto número: '))
    d = int(input('Quinto número:'))

    print("Maior: ", maior(x, y, z, a, d))
    print()


while True:
    menu()