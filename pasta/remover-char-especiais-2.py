#Exercício 3: Remover Caracteres Especiais
#Implemente um programa que remove todos os caracteres especiais (como !, @, #, $, etc.) de uma string

#Método "filter(str.isalnum, string)" :

#Para remover os caracteres especiais da string, teremos que verificar se um caractere é alfanumérico e eliminá-lo caso contrário.
#Nesta abordagem, em vez de usar o loop for e a instrução if no método str.isalnum(), usaremos a função filter().
string = "!!Eai! $% Como vai @querida#?"

nova_string = ''.join(filter(str.isalnum, string))
print(nova_string)
