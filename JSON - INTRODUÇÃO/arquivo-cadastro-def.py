# Faça um programa de cadastros de usuários que cumpra com os seguintes requisitos:
# O programa deve mostrar um menu com as seguintes opções: 1 - cadastrar usuário, 2 - listar usuários cadastrados.
# Ao escolher a opção 1, o usuário deve digitar um nome e apertar enter para cadastrar.
# Ao escolher a opção 2, o programa deve listar as pessoas cadastradas.
# Sempre que um nome for cadastrado, os cadastros devem ser escritos em um arquivo chamado "cadastros.txt".
# Você pode utilizar a função eval para ler o arquivo como lista.
import os

def salvar_cadastros(lista):
    f = open('../cadastros.txt', 'w')
    f.write(str(lista))
    f.close()

def ler_cadastros():
    if not os.path.exists('../cadastros.txt'):
        salvar_cadastros([])
    f = open('../cadastros.txt', 'r')
    return lista2

if __name__ == '__main__':
    lista = ler_cadastros()
    while True:
        opcao = input('\n------------------------- MENU -------------------------\n1 - Cadastrar usuário\n2 - Listar usuários cadastrados\nDigite uma opção: ')
        if opcao == '1':
            nome = input('\n------- CADASTRAR USUÁRIO -------\nDigite um nome e aperte enter para cadastrar\nNOME:')
            lista.append(nome)
            f = open('../cadastros.txt', 'w')
            f.write(str(lista))
            f.close() #precisa fechar o modo write para poder abrir o outro modo, aqui é
        elif opcao == '2':
            if os.path.exists('../cadastros.txt'): # se o arquivo existe abre no modo read, se n abre no modo w+
                f = open('../cadastros.txt', 'r') #aqui é apenas para ler
            else:
                f = open('../cadastros.txt', 'w+')
                f.write('[]')
            texto = f.read()
            lista2 = eval(texto)
            for nome in lista2:
                print(nome)
        else:
            print('OPÇÃO INVÁLIDA!!!!!!!!!')