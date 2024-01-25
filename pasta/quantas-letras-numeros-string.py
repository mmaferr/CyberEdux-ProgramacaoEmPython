#Exercício 2: Contar Letras e Números
# *Crie um programa que conta quantas letras e quantos números há em uma string

def contar_letras_numeros(string):
    contagem_letras = 0
    contagem_numeros = 0

    for caractere in string:
        if caractere.isalpha():     #letras
            contagem_letras += 1        #está somando contagem_letras + 1 e guardando em contagem_letras
        elif caractere.isdigit():           #numero
            contagem_numeros += 1

    return contagem_letras, contagem_numeros

string = input("Digite uma string: ")

letras, numeros = contar_letras_numeros(string)

# Exibe o resultado
print(f"Número de letras: {letras}")
print(f"Número de números: {numeros}")
