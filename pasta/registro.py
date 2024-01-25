# Crie uma lista para armazenar os registros de pessoas (cada registro será um dicionário)
cadastro = []


# Função para adicionar um novo registro ao cadastro
def adicionar_registro():
    print("IDENTIFICAÇÃO")
    nome = input("Nome: ")
    data_nascimento = input("Data de nascimento (dd/mm/aaaa): ")
    eleitor = input("Título de Eleitor: ")
    sexo = input("Sexo: ")
    naturalidade = input("Naturalidade: ")
    uf = input("UF: ")
    nome_da_mae = input("Nome da Mãe: ")

    print("ENDEREÇO")
    cep = input("CEP: ")
    municipio = input("Município: ")
    uf2 = input("UF: ")
    logradouro = input("Logradouro: ")
    numero = input("Número: ")
    complemento = input("Complemento: ")
    bairro = input("Bairro: ")
    ddd = input("DDD: ")
    telefone = input("Telefone: ")
    celular = input("Celular: ")

    registro = {"Nome": nome, "Data de Nascimento": data_nascimento, "Título de Eleitor": eleitor, "Sexo": sexo,
                "Naturalidade": naturalidade, "UF": uf, "Nome da mãe": nome_da_mae, "CEP": cep, "Município": municipio,
                "Logradouro": logradouro, "Número": numero, "Complemento": complemento, "Bairro": bairro, "DDD": ddd,
                "Telefone": telefone, "Celular": celular}
    cadastro.append(registro)
    print("Registro adicionado com sucesso!")


# Função para listar todos os registros no cadastro
def listar_registros():
    for i, registro in enumerate(cadastro, 1):
        print(f"Registro {i}:")
        print(f"Nome: {registro['Nome']}")
        print(f"Data de Nascimento: {registro['Data de Nascimento']}")
        print(f"Título de Eleitor: {registro['Título de Eleitor']}")
        print(f"Sexo: {registro['Sexo']}")
        print(f"Naturalidade: {registro['Naturalidade']}")
        print(f"UF: {registro['UF']}")
        print(f"Nome da mãe: {registro['Nome da mãe']}")
        print(f"CEP: {registro['CEP']}")
        print(f"Município: {registro['Município']}")
        print(f"UF: {registro['UF']}")
        print(f"Logradouro: {registro['Logradouro']}")
        print(f"Número: {registro['Número']}")
        print(f"Complemento: {registro['Complemento']}")
        print(f"Bairro: {registro['Bairro']}")
        print(f"DDD: {registro['DDD']}")
        print(f"Telefone: {registro['Telefone']}")
        print(f"Celular: {registro['Celular']}")
        print()


# Menu principal
while True:
    print("---- Cadastro de Pessoas ----")
    print("1. Adicionar Registro")
    print("2. Listar Registros")
    print("3. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        adicionar_registro()
    elif opcao == "2":
        listar_registros()
    elif opcao == "3":
        break
    else:
        print("Opção inválida. Tente novamente.")
