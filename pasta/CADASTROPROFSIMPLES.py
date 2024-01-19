cadastros = dict()
while True:
    entrada = input('Digite nome, email, ano e cpf: ')
    if entrada == '':
        break
    nome, email, ano, cpf = (entrada.split(' '))
    cadastros[cpf] = nome, email, ano

while True:
    cpf = input('Digite um cpf: ')
    if cpf in cadastros.keys():  # keys retorna true ou false
        dados = cadastros[cpf]
        print(dados)
    else:
        print('usuário não cadastrado!!!!!!!')
