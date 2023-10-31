import os
import json
def cadastrar(cadastros):
    """
    Função que faz o cadastro do aluno.
    Parametros:
        cadastros (dict) - dicionário de cadastros
    """
    nome = input('Digite um nome: ')
    email = input('Digite um email: ')
    turma = input('Digite a turma: ')
    if cadastros == dict():
        rga = 1
    else:
        rga = max(cadastros.keys())+1
    cadastros[rga] = (nome, email, turma)

def listagem(cadastros):
    """
    Função que mostra os alunos cadastrados.
    Parametros:
        cadastros (dict) - dicionário de cadastros
    """
    for rga in cadastros.keys():
        print('RGA', rga, 'Dados', cadastros[rga])

def buscar(cadastros):
    """
    Função que faz a busca de aluno por RGA.
    Parametros:
        cadastros (dict) - dicionário de cadastros
    """
    rga = int(input('RGA: '))
    if rga in cadastros.keys():
        print(cadastros[rga])
    else:
        print('Aluno inexistente')

def salvar(cadastros):
    """
    Função que salva os cadastros em arquivo.
    Parametros:
        cadastros (dict) - dicionário de cadastros
    """
    filename = input('Nome do arquivo: ')
    f = open(filename, 'w')
    f.write(str(cadastros))
    f.close()

def carregar():
    """
    Função que retorna o dicionário salvo em um arquivo.
    Retorno:
        Dict|NoneType: caso o arquivo exista, retorna o dicionário. Caso não exista, retorna None.
    """
    filename = input('Nome do arquivo: ')
    if os.path.exists(filename):
        f = open(filename, 'r')
        texto = json.dumps()
        f.close()
        return json.loads(texto)
    else:
        print('Arquivo inexistente')
        return None

def menu():
    """
    Menu do usuário
    """
    cadastros = dict()
    while True:
        print('1 - cadastrar\n2 - listar\n3 - buscar rga\n4 - salvar\n5 - carregar')
        opcao = input('opção: ')
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
            print('Opção inválida')

if __name__ == '__main__':
    menu()
