a = 1
camiseta = 10
tenis = 70
calca = 50
bone = 40
saia = 30

while a==1:
    tabela = input(f"\n                  === CONTROLE DE ESTOQUE ===                    \n\nCOD ITEM          QUANT.       PREÇO UN.     VALOR EM ESTOQUE\n-------------------------------------------------------------\n1 - Camiseta ------ {camiseta}    |  \n2 - Tênis --------- {tenis}    |   \n3 - Calça --------- {calca}    |\n4 - Boné ---------- {bone}    |   \n5 - Saia ---------- {saia}    |   \nS - Sair\nDigite uma opção:")
    if tabela == '1':
        opcao = input('A - Adicionar itens\nB - Remover itens\nOpção:')
        if opcao == 'A' or opcao =='a':
            quantidade1 = int(input('Informe a quantidade: '))
            print('Quantidade de itens adicionado com sucesso!!!\n')
            camiseta += quantidade1

        if opcao == 'B' or opcao == 'b':
            quantidade1 = int(input('Informe a quantidade que deseja retirar: '))
            while quantidade1 > camiseta:
                quantidade1 = int(input('Valor inadequado, digite novamente: '))
            camiseta -= quantidade1


    if tabela == '2':
        opcao = input('A - Adicionar itens\nB - Remover itens\nOpção:')
        if opcao == 'A' or opcao == 'a':
            quantidade2 = int(input('Informe a quantidade: '))
            print('Quantidade de itens adicionado com sucesso!!!\n')
            tenis += quantidade2

        if opcao == 'B' or opcao == 'b':
            quantidade2 = int(input('Informe a quantidade que deseja retirar: '))
            while quantidade2 > camiseta:
                quantidade2 = int(input('Valor inadequado, digite novamente: '))
            tenis -= quantidade2

    if tabela == '3':
        opcao = input('A - Adicionar itens\nB - Remover itens\nOpção:')
        if opcao == 'A' or opcao == 'a':
            quantidade3 = int(input('Informe a quantidade: '))
            print('Quantidade de itens adicionado com sucesso!!!\n')
            calca += quantidade3

        if opcao == 'B' or opcao == 'b':
            quantidade3 = int(input('Informe a quantidade que deseja retirar: '))
            while quantidade1 > calca:
                quantidade3 = int(input('Valor inadequado, digite novamente: '))
            calca -= quantidade3

    if tabela == '4':
        opcao = input('A - Adicionar itens\nB - Remover itens\nOpção:')
        if opcao == 'A' or opcao == 'a':
            quantidade4 = int(input('Informe a quantidade: '))
            print('Quantidade de itens adicionado com sucesso!!!\n')
            bone += quantidade4

        if opcao == 'B' or opcao == 'b':
            quantidade5 = int(input('Informe a quantidade que deseja retirar: '))
            while quantidade4 > bone:
                quantidade4 = int(input('Valor inadequado, digite novamente: '))
            bone -= quantidade4

    if tabela == '5':
        opcao = input('A - Adicionar itens\nB - Remover itens\nOpção:')
        if opcao == 'A' or opcao == 'a':
            quantidade5 = int(input('Informe a quantidade: '))
            print('Quantidade de itens adicionado com sucesso!!!\n')
            saia += quantidade5

        if opcao == 'B' or opcao == 'b':
            quantidade5 = int(input('Informe a quantidade que deseja retirar: '))
            while quantidade1 > saia:
                quantidade5 = int(input('Valor inadequado, digite novamente: '))
            saia -= quantidade5

    if tabela == 's' or tabela == 'S':
        sair = input('Deseja mesmo sair?\n1 - Sim   2 - Não\n:')
        if sair == '1':
            break
        if sair == '2':
            print('Então tá bom!')





