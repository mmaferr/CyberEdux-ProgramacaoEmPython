while True:
    
    entrada = input('\nOpções:\n1. Somar dois números\n2. Sair\n\nEscolha uma opção: ')
    if entrada == '':
        break

    if entrada == '1':
        def soma(x, y):
            n = x + y
            return n

        valor1 = float(input('digite o primeiro número: '))
        valor2 = float(input('digite o segundo número: '))
        resultado = soma(valor1, valor2)
        print('O resultado da soma é:', resultado)

    if entrada == '2':
        sair = input('\nTem certeza que deseja sair?\ns - Sim  n - Não\nEscolha uma opção: ')
        if sair == 's' or sair == 'S':
            print('Você saiu!')
            break
        if sair == 'n' or sair == 'N':
            print('Você voltou!!')
