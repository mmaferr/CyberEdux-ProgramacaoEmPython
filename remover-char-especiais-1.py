#Exercício 3: Remover Caracteres Especiais
#Implemente um programa que remove todos os caracteres especiais (como !, @, #, $, etc.) de uma string

#Método "str.isalnum()" :

#Para remover os caracteres especiais da string, teremos que verificar se um caractere é alfanumérico e eliminá-lo caso contrário.

string = "!!Eai! $% Como vai @querida#?"

nova_string = ''.join(char for char in string if char.isalnum())
print(nova_string)