#Exercício 5: Separar Letras de Números
#Crie um programa que separa as letras dos números em uma string, criando duas novas strings

def separar_letras_numeros(string):
    letras = ''
    numeros = ''

    for caractere in string:
        if caractere.isalpha(): #letras
            letras += caractere
        elif caractere.isdigit():   #numeros
            numeros += caractere

    return letras, numeros

string = input("Digite uma string: ")

letras, numeros = separar_letras_numeros(string)

print("Letras na string:", letras)
print("Números na string:", numeros)
