#8. Escreva um programa que peça ao usuário para inserir um número e imprima a tabuada
#desse número.
num = int(input('Digite um número: '))

for i in range(1, 11):
    print(f'{num} x {i} = {num*i}')