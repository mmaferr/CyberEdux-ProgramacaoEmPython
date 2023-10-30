import os   # importa uma biblioteca, que nesse caso é a biblioteca 'os'
lista = ['Felipe', 'Eduardo', 'Kamila']
nome_dir = 'meus_arquivos'
nome_arq = 'nomes.txt'
f = open(os.path.join(nome_dir, nome_arq), 'r')
eval(f.read())
for nome in lista:
    print(nome)
f.close()