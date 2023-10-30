# "r" - Read - Abre um arquivo para leitura, erro se o arquivo não existir, retorna o arquivo como uma string
# "a" - Append - Abre um arquivo para anexar, cria o arquivo se ele não existir
# "w" - Write - Abre um arquivo para gravação, cria o arquivo se ele não existir, escreve o nome do arquivo e o texto

f = open('nome3.txt', 'w+') //aqui vc cria o arquivo digitando o seu nome dentro de open
f.write('meu nome e maria') //aqui fica o texto que irá armazenar dentro do arquivo que está criando
f.close()

# w+ > abre o arquivo ou cria se n existir
# "x" - Create - Cria o arquivo especificado, retorna um erro se o arquivo existir
# Além disso, você pode especificar se o arquivo deve ser manipulado como modo binário ou de texto
# "t" - Text - Valor padrão. Modo de texto
# "b" - Binary - Modo binário (por exemplo, imagens)


f = open('meus_arquivos/nome.txt', 'w+')  //cria um arquivo chamado "nome.txt" dentro da pasta "meus_arquivos"
f.write('meu nome e maria\n')
f.write('meu nome e linda')
f.close()

ou

f = open(os.path.join('meus_arquivos', 'nomes2.txt'), 'w+')
#text = f.read()
#print(text)
f.write('meu nome e maria\n')
f.write('meu nome e linda')
f.close()

ou

import os   # importa uma biblioteca, que nesse caso é a biblioteca 'os'
nome_dir = 'meus_arquivos'
nome_arq = 'nomes.txt'
f = open(os.path.join(nome_dir, nome_arq), 'w+')
f.write('meu nome e maria\n')
f.write('meu nome e linda')
f.close()

-------------------------------------------------------------------------------------------------------------------------------------------------
import os   # importa uma biblioteca, que nesse caso é a biblioteca 'os'
lista = ['Felipe', 'Eduardo', 'Kamila']
nome_dir = 'meus_arquivos'
nome_arq = 'nomes.txt'
f = open(os.path.join(nome_dir, nome_arq), 'w+')
f.write(str(lista))
f.close()

terminal:
['Felipe', 'Eduardo', 'Kamila']

--------------------------------------------------------------------------------------------------------------------------------------------------
// eval > se mandarmos uma string o eval nos retorna a string como um objeto lista, esse é o jeito mais simples de fazer isso em python, a maneira mais apropriada de fazer isso é usando jason. Jason é como um xml, só que mais moderno.

import os   # importa uma biblioteca, que nesse caso é a biblioteca 'os'
lista = ['Felipe', 'Eduardo', 'Kamila']
nome_dir = 'meus_arquivos'
nome_arq = 'nomes.txt'
f = open(os.path.join(nome_dir, nome_arq), 'r')
eval(f.read())
for nome in lista:
    print(nome)
f.close()



