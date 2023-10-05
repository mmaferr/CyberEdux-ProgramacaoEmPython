#Exercício 3: Remover Caracteres Especiais
#Implemente um programa que remove todos os caracteres especiais (como !, @, #, $, etc.) de uma string
import re

#Método com expressões regulares :

#Para remover o caractere especial da string, poderíamos escrever uma expressão regular que removerá automaticamente
# os caracteres especiais da string. A expressão regular para isso será [^a-zA-Z0-9], onde ^ representa qualquer caractere,
# exceto os caracteres entre colchetes, e a-zA-Z0-9 representa que a string só pode ter letras pequenas e maiúsculas e
# dígitos numéricos.

string = "!!Eai! $% Como vai @querida#?"

nova_string = re.sub(r"[^a-zA-Z0-9]","",string)
print(nova_string)