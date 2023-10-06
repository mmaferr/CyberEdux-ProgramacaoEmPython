a=1
usuario = ''
senha = ''
usuario1 = ''
senha1 = ''

while a == 1:
    tabela = input('1 - Cadastrar Usuário\n2 - Login\n3 - Sair\n:')
    if tabela == '1':
        usuario = input('Insira um nome de usuário: ')
        while len(usuario) != 5:
            usuario = input('O usuário deve conter 5 caracteres! Tente novamente: ')
        senha = input('Digite uma senha: ')
        while len(senha) != 6:
            senha = input('A senha deve conter 6 caracteres!Tente novamente: ')
        print('Cadastrado com sucesso!\n')

    if tabela == '2':
        usuario1 = input('Usuário: ')

        if usuario1 == usuario:
            print('...')
            senha1 = input('Senha: ')
            if senha1 == senha:
                print('Logado com sucesso!\n')
            else:
                print('A senha está incorreta!\n')
        else:
            print('Este usuário não existe!')




    if tabela == '3':
        print('Você foi desconectado!')
        break





