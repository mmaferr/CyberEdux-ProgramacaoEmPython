#Exercício 9: Substituir Números por Palavras
#Implemente um programa que substitua todos os números por palavras equivalentes
# (por exemplo, '1' por 'um', '2' por 'dois', etc.) em uma string.

#este programa só substitui os números quando estão separados.
def substituir_numeros_por_palavras(string):
    mapeamento = {
        'o': 'zero',
        '1': 'um',
        '2': 'dois',
        '3': 'três',
        '4': 'quatro',
        '5': 'cinco',
        '6': 'seis',
        '7': 'sete',
        '8': 'oito',
        '9': 'nove',
        '10': 'dez',
    }

    string_resultante = ''

    i = 0
    while i < len(string):
        # Verifica se o caractere é um dígito
        if string[i].isdigit():
            numero = ''
            while i < len(string) and string[i].isdigit():
                numero += string[i]
                i += 1
            # Substitui o número pela palavra correspondente
            palavra = mapeamento.get(numero, numero)
            string_resultante += palavra
        else:
            # Mantém o caractere inalterado se não for um dígito
            string_resultante += string[i]
            i += 1

    return string_resultante

string = input("Digite uma string: ")

nova_string = substituir_numeros_por_palavras(string)

print("Nova string:", nova_string)
