import os

def cadastrar(cadastros):  # dicionario de cadastros
    nome = input('--------- CADASTRAR ESTUDANTE ---------\nNome: ')
    email = input('Email: ')
    turma = input('Turma: ')
    # após a inserção dessas informações, o programa deve gerar um RGA para o aluno e cadastrar as informações
    if cadastros == dict():  # se o dicionário cadastros for igual a um dicionário vazio
        rga = 1
    else:
        rga = max(cadastros.keys()) + 1
    cadastros[rga] = (nome, email, turma)

def salvar(cadastros):
    filename = input('Nome do arquivo: ')
    f = open(filename, 'w')
    f.write(str(cadastros))
    f.close()

def carregar(cadastros):
    filename = input('Nome do arquivo: ')
    if os.path.exists(filename):
        f = open(filename, 'r')
        texto = f.read()
        eval(texto) # transforma o texto em dicionário
        return eval(texto)
    else:
        print('ARQUIVO INEXISTENTE!!!!!!!!!!!!!!!!!!!!!')
        return None # none é nada, não retorna nada

def listagem(cadastros):
    for rga in cadastros.keys():
        print('RGA', rga, 'Dados', cadastros[rga])

def buscar(cadastros):
    rga = int(input('RGA: '))
    if rga in cadastros.keys():
        print(cadastros[rga])
    else:
        print('ALUNO INEXISTENTE!!!!!!!!!')

def menu(cadastros):
    cadastros = dict()
    while True:
        opcao = input('--------- ESTUDANTES ---------\n1 - Cadastrar estudante\n2 - Listar cadastros\n3 - Buscar cadastro por RGA\n4 - Salvar cadastros em arquivos\n5 - Carregar cadastros de arquivo\n\nEscolha uma opção: ')
        if opcao == '1':
            cadastrar(cadastros)
        elif opcao == '2':
            listagem(cadastros)
        elif opcao == '3':
            buscar(cadastros)
        elif opcao == '4':
            salvar(cadastros)
        elif opcao == '5':
            retorno = carregar()
            if retorno is not None:
                cadastros = retorno
        else:
            print('OPAÇÃO INVÁLIDA!!!!!!')

if __name__ == '__main__':
    cadastros = dict()
    while True:
        menu(cadastros)