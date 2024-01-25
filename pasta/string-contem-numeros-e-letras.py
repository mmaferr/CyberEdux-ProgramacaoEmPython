#Exercício 1: Verificar se uma String Contém Números e Letras
#Escreva um programa que verifica se uma string contém tanto letras quanto números.

import re

def contem_letras_e_numeros(s):
    padrao = r'^(?=.*[a-zA-Z])(?=.*\d)'
    return bool(re.search(padrao, s))

string = input("Digite uma string: ")

if contem_letras_e_numeros(string):
    print("A string contém tanto letras quanto números.")
else:
    print("A string não contém tanto letras quanto números.")

#* def > serve para definir funções.

#* padrao = r'^(?=.*[a-zA-Z])(?=.*\d)' > é uma expressão que define um padrão a string de entrada que deve atender para
#ser considerada como contendo tanto letras quanto números.

#* return bool(re.search(padrao, s)) > A função re.search() da biblioteca re é usada para procurar um padrão (nesse caso,
# o padrão definido em padrao) na string s. Se o padrão for encontrado em qualquer parte da string, re.search() retornará
# um objeto "match", caso contrário, retornará None.
# A função bool() é usada para converter o resultado retornado por re.search() em um valor booleano. Isso significa que se re.search() encontrar uma correspondência, bool() retornará True, caso contrário, retornará False.

