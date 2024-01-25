# 2 — Faça um programa onde o usuário cadastra um conjunto de pessoas com nome, email, ano de
# nascimento e CPF. Após a etapa de cadastro, o programa deve seguir para uma etapa de consulta, onde o
# usuário digita CPFs de pessoas cadastradas e o programa mostra os dados das pessoas a partir disso. Caso
# o usuário digite um CPF não-cadastrado, o programa deve mostrar a mensagem “Não cadastrado”.
# Dica: armazene os cadastros em um dicionário de tuplas, usando os CPFs como chave e as tuplas como
# valores. Ex: {‘59739132014’: (‘beltrano’, ‘beltrano@mail.com’, 1995), ‘56654242009’: (‘fulano’,
# ‘fulano@mail.com’, 2000)}.

cadastros = dict()  # dict é igual a dicionário

while True:
    print('\nOpções:\n1. Cadastrar pessoa\n2. Consultar pessoa\n3. Sair\n')
    opcao = input('Escolha uma opção: ')
    if opcao == '':
        break

    if opcao == '1':
        cpf = input('CPF: ')
        nome = input('Nome: ')
        ano = input('Ano de nascimento: ')
        email = input('Email: ')
        cadastros[cpf] = (nome, ano, email)
        print('Pessoa cadastrada com sucesso!')
    elif opcao == '2':
        cpf = input('Para fazer a consulta digite o CPF da pessoa\nCPF: ')
        if cpf in cadastros:
            nome, ano, email = cadastros[cpf]
            print(f'Nome: {nome}\nAno de nascimento: {ano}\nEmail: {email}')
        else:
            print('CPF NÃO CADASTRADO!!!!!')
    elif opcao == '3':
        print('VOCÊ SAIU!!!!')
        break
    else:
        print('OPÇÃO INVÁLIDA!!! TENTE NOVAMENTE...')
