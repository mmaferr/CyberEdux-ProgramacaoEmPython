import json
import os

cadastros_usuarios = {}
biblioteca = []

#Função para salvar cadastros dos usuarios e a biblioteca num arquivo JSON
def salvar():
    with open(f"cadastros_usuarios.json", "w") as file:
        json.dump(cadastros_usuarios, file)
    with open(f"biblioteca.json", "w") as file:
        json.dump(biblioteca, file)

#Função para verificar e atualizar cadastros e a biblioteca
def carregar():
    if not os.path.exists('cadastros_usuarios.json') or not os.path.exists('biblioteca.json'):
        salvar()
    with open(f"cadastros_usuarios.json", "r") as file:
        estrutura = json.load(file)
        cadastros_usuarios.clear()
        cadastros_usuarios.update(estrutura)
    with open(f"biblioteca.json", "r") as file:
        estrutura = json.load(file)
        biblioteca.clear()
        for dado in estrutura:
            biblioteca.append(dado)

#Função para criar e salvar o nickname, nome de usuario e senha de um usuario
def criar_usuario(nickname, nome_usuario, senha):
    usuario = (nome_usuario, senha)
    cadastros_usuarios[nickname] = usuario
    salvar()

#Função para salvar o titulo, autor e genero de um item a biblioteca
def cadastrar_item_na_biblioteca(tipo,titulo,autor,genero):
    tupla = (titulo, autor, genero)
    biblioteca.append(tupla)
    salvar()
    return len(biblioteca)-1

#Função para coletar dados do usuario sobre o titulo, autor, genero e determinar o codigo do livro
def cadastrar_livro():
    titulo = input("Titulo: ")
    autor = input("Autor: ")
    genero = input("Genero:")
    codigo = cadastrar_item_na_biblioteca('Livro', titulo, autor, genero)
    print("O código do Item cadastrado é :", codigo)

#Função para coletar dados do usuario sobre o titulo, autor, genero e determinar o codigo do filme
def cadastrar_filme():
    titulo = input("Titulo: ")
    autor = input("Autor: ")
    genero = input("Genero:")
    codigo = cadastrar_item_na_biblioteca('Filme', titulo, autor, genero)
    print("O código do Item cadastrado é :", codigo)

#Função para coletar dados do usuario sobre o titulo, autor, genero e determinar o codigo da série
def cadastrar_serie():
    titulo = input("Titulo: ")
    autor = input("Autor: ")
    genero = input("Genero:")
    codigo = cadastrar_item_na_biblioteca('Serie', titulo, autor, genero)
    print("O código do Item cadastrado é :", codigo)

#Função para coletar dados do usuario sobre o titulo, autor, genero e determinar o codigo do jogo
def cadastrar_jogo():
    titulo = input("Titulo: ")
    autor = input("Autor: ")
    genero = input("Genero:")
    codigo = cadastrar_item_na_biblioteca('Jogo', titulo, autor, genero)
    print("O código do Item cadastrado é :", codigo)

#Função para percorrer a biblioteca e encontrar o item pelo titulo
def pesquisar_item_por_titulo(titulo_digitado):
    for cod in range(len(biblioteca)):
        titulo, autor, genero = biblioteca[cod]
        if titulo_digitado == titulo:
            print(titulo,autor,genero,cod)

#Função para percorrer a biblioteca e encontrar o item pelo autor
def pesquisar_item_por_autor(autor_digitado):
    for cod in range(len(biblioteca)):
        titulo, autor, genero = biblioteca[cod]
        if autor_digitado == autor:
            print(titulo,autor,genero,cod)

#Função para percorrer a biblioteca e encontrar o item pelo gênero
def pesquisar_item_por_genero(genero_digitado):
    for cod in range(len(biblioteca)):
        titulo, autor, genero = biblioteca[cod]
        if genero_digitado == genero:
            print(titulo,autor,genero,cod)

#Função para percorrer a biblioteca e encontrar o item pelo titulo
def pesquisar_item_por_cod(cod_digitado):
    if cod_digitado >= 0 and cod_digitado < len(biblioteca):
        titulo, autor, genero = biblioteca[cod_digitado]
        print(titulo,autor,genero,cod_digitado)
    else:
        print("Codigo inválido !")

#Função para exibir o menu interativo da biblioteca
def menu_biblioteca():
     while True:
        print("Bem-vindo à sua biblioteca pessoal")
        print("[1] Adicionar item")
        print("[2] Pesquisar")
        print("[3] Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == '1':
            print("[1] Livro")
            print("[2] Filme")
            print("[2] Serie")
            print("[4] Jogos")
            tipo = input("Tipo : ")
            if opcao == '1':
                cadastrar_livro()
            elif opcao == '2':
                cadastrar_filme()
            elif opcao == '3':
                cadastrar_serie()
            elif opcao == '4':
                cadastrar_jogo()
        elif opcao == '2':
            print("Pesquisar por :")
            print("[1] Titulo:")
            print("[2] Autor:")
            print("[3] Genero:")
            print("[4] Código:")
            opcao2 = input()
            
            if opcao2  == '1':
                titulo = input("Digite o Titulo desejado:")
                pesquisar_item_por_titulo(titulo)
            elif opcao2 =='2':
                autor = input("Digite o Autor desejado:")
                pesquisar_item_por_autor(autor)
            elif opcao2 =='3':
                genero = input("Digite o Genero Desejado:")
                pesquisar_item_por_genero(genero)
            elif opcao2 == '4':
                cod = int(input("Digite o Código desejado:"))
                pesquisar_item_por_cod(cod)
            else :
                print("Opção invalida !")
        elif opcao == '3':
            break

#Função verificar se o nickname e a senha estão corretos
def fazer_login(nickname, senha_digitada):
    if nickname in cadastros_usuarios.keys():    
        nome, senha_real = cadastros_usuarios[nickname]
        if senha_digitada == senha_real:
            menu_biblioteca()
        else:
            print('senha incorreta')
    else:
        print("Senha ou login incorreto !")

if _name_ == "_main_":
    carregar()
    while True:
        escolha = input("[1] Criar novo usuário\n"
                        "[2] Login\n"
                        "[3] Sair\n")

        if escolha == "1":
            nome_usuario = input("Nome de usuário: ")
            nickname =input('Crie um Nick Name :')
            senha = input("Senha: ")
            criar_usuario(nickname, nome_usuario, senha)
        elif escolha == "2":
            nickname = input("Nick Name: ")
            senha = input("Senha: ")
            fazer_login(nickname, senha)
        elif escolha == '3':
            print("Logout Confirmado !")
            break
        else:
            print("Opção invalida !")
