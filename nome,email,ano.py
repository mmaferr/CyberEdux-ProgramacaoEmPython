# 1 – Faça um programa onde o usuário cadastra um conjunto de pessoas com nome, email e ano de
# nascimento. Após a etapa de cadastro, o programa deve mostrar uma tabela de usuários cadastrados.
# Dica: armazene os cadastros em uma lista de tuplas, no seguinte formato — [(‘fulano’, ‘fulano@mail.com’,
# 2000), (‘beltrano’, ‘beltrano@mail.com’, 1995), ...].

cadastros = []

while True:
    entrada = input(f'Insira nome, email, ano de nascimento e cpf:')
    if entrada == '':
        break
    nome, email, ano, cpf = entrada.split('')
    tupla = (nome, email, ano, cpf)
    cadastros.append(tupla)

for cadastro in cadastros:
    print(cadastro[0], cadastro[1], cadastro[2],cadastro[3])
 #   dicionario = {'04396925123': ('filipe@gmail.com', 1999), '04396925124': ('filipe@gmail.com', 1999)}
  #  print(dicionario['04396925123'])
