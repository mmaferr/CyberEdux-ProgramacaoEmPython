# Dada uma lista de palavras, crie um dicionário onde as chaves são as palavras e os valores
# são o número de vezes que cada palavra aparece na lista.

palavras = ['Dada', 'uma', 'lista', 'lista', 'de', 'palavras', 'crie', 'um', 'dicionário', 'onde', 'as', 'chaves', 'são', 'os', 'valores',
            'número', 'Dada', 'Dada', 'vezes', 'que', 'cada', 'aparece', 'na', 'na', 'na', 'onde', 'chaves', 'chaves', 'chaves', 'chaves', 'chaves', 'valores', 'valores']

dic = {}

for palavra in palavras:
    if palavra in dic:
        dic[palavra] += 1
    else:
        dic[palavra] = 1

print(dic)
