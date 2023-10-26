while True:
    entrada = input('\nOpções:\n1. Calcular o quadrado de um número\n2. Sair\n\nEscolha uma opção: ')
    if entrada == '':
        break

    if entrada == '1':
        def quadrado(n):
            return n **2
        n = float(input('Digite um numero: '))

        print('O quadrado desse número é', quadrado(n), '!')

    if entrada == '2':
        sair = input('Tem certeza que deseja sair?\ns - Sim  n - Não\nEscolha uma opção: ')
        if sair == 's' or sair == 'S':
            print('Você saiu!')
            break
        if sair == 'n' or sair == 'N':
            print('Você voltou!!')

# / divisão para número real
# // divisão para número inteiro