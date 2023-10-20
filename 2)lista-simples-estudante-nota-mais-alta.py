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
    {'Nome': 'Valentina', 'idade': 23, 'nota': 95},
    {'Nome': 'Mariana', 'idade': 19, 'nota': 100},
    {'Nome': 'Pedroso', 'idade': 22, 'nota': 0},
    {'Nome': 'Joãozin', 'idade': 21, 'nota': 25},
    {'Nome': 'Guilhermito', 'idade': 19, 'nota': 48},
    {'Nome': 'Valéria', 'idade': 23, 'nota': 100}
]

maior_nota = 0
for estudantes in lista_estudantes:
    if estudantes['nota'] > maior_nota:
        maior_nota = estudantes['nota']

for estudantes in lista_estudantes:
    if estudantes['nota'] == maior_nota:
        print(estudantes['Nome'], estudantes['nota'])

