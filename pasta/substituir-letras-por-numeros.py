#Exercício 6: Substituir Letras por Números
#Implemente um programa que substitua todas as ocorrências de letras por seus equivalentes numéricos ]
# (por exemplo, 'a' por '1', 'b' por '2', etc.) em uma string.

def substituir_letras_por_numeros(string):  #def > define função
    mapeamento = {
        'a': '1',
        'b': '2',
        'c': '3',
        'd': '4',
        'e': '5',
        'f': '6',
        'g': '7',
        'h': '8',
        'i': '9',
        'j': '10',
    }

    string_resultante = ''

    for caractere in string:
        if caractere.isalpha() and caractere.islower():
            string_resultante += mapeamento.get(caractere, caractere)
        else:
            string_resultante += caractere

    return string_resultante

string = input("Digite uma string: ")

nova_string = substituir_letras_por_numeros(string)

print("Nova string:", nova_string)
