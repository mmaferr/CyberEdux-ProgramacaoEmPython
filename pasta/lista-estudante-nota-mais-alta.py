# Dada uma lista de dicionários representando informações de estudantes (com
# chaves como 'nome', 'idade', 'nota'), escreva uma função para encontrar o estudante
# com a nota mais alta

def encontrar_nota_mais_alta(estudantes):
    estudante_nota_mais_alta = max(estudantes, key=lambda x: x['nota'])
    return estudante_nota_mais_alta

lista_estudantes = [
    {'Nome': 'Maria', 'idade': 19, 'nota': 100},
    {'Nome': 'Pedro', 'idade': 22, 'nota': 0},
    {'Nome': 'João', 'idade': 21, 'nota': 25},
    {'Nome': 'Guilherme', 'idade': 19, 'nota': 48},
    {'Nome': 'Valentina', 'idade': 23, 'nota': 95}
]

estudante_com_nota_mais_alta = encontrar_nota_mais_alta(lista_estudantes)

if estudante_com_nota_mais_alta:
    print("Estudante com a nota mais alta:", estudante_com_nota_mais_alta)
else:
    print("A lista de estudantes está vazia.")
    
