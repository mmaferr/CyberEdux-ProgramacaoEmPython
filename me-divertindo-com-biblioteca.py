# Crie uma lista de dicionários representando livros (com chaves como 'título', 'autor',
# 'ano de publicação') e escreva um código para encontrar todos os livros publicados
# após 2000.
a = 1
livros = [
    {
        'título': 'Dom Casmurro',
        'autor': 'Machado de Assis',
        'ano de publicação': 1899
    },
    {
        'título': 'O Senhor dos Anéis',
        'autor': 'J.R.R. Tolkien',
        'ano de publicação': 1954
    },
    {
        'título': '1984',
        'autor': 'George Orwell',
        'ano de publicação': 1949
    },
    {
        'título': 'Cem Anos de Solidão',
        'autor': 'Gabriel García Márquez',
        'ano de publicação': 1967
    },
    {
        'título': 'Harry Potter e a Pedra Filosofal',
        'autor': 'J.K. Rowling',
        'ano de publicação': 1997
    },
    {
        'título': 'A Menina que Roubava Livros',
        'autor': 'Markus Zusak',
        'ano de publicação': 2005
    },
    {
        'título': 'A Culpa É das Estrelas',
        'autor': 'John Green',
        'ano de publicação': 2012
    }
]

while a==1:
    menu = input('------- BIBLIOTECA ------\n1 - livros\ns - Sair\nDigite uma opção: ')
    if menu == '1':
        for livro in livros:
            print("Título:", livro['título'])
        menu2 = input('\nDeseja ver mais alguma coisa?\n1 - Livros publicados após o ano 2000\ns - Não, quero sair\nDigite uma opção: ')
        if menu2 == '1':
            livros_apos_2000 = []
            for livro in livros:
                if livro['ano de publicação'] > 2000:
                    livros_apos_2000.append(livro)
            for livro in livros_apos_2000:
                print("\n--- LIVRO PUBLICADO APÓS O ANO 2000 ---\n\n-Título:", livro['título'])
                print("-Autor:", livro['autor'])
                print("-Ano de Publicação:", livro['ano de publicação'])




