cadastro = []


def adicionar_registro():
    registro = {}

    print("IDENTIFICAÇÃO")
    registro["Nome"] = input("Nome: ")
    registro["Data de Nascimento"] = input("Data de nascimento (dd/mm/aaaa): ")
    registro["Título de Eleitor"] = input("Título de Eleitor: ")
    registro["Sexo"] = input("Sexo: ")
    registro["Naturalidade"] = input("Naturalidade: ")
    registro["UF"] = input("UF: ")
    registro["Nome da Mãe"] = input("Nome da Mãe: ")

    print("ENDEREÇO")
    registro["CEP"] = input("CEP: ")
    registro["Município"] = input("Município: ")
    registro["UF2"] = input("UF: ")
    registro["Logradouro"] = input("Logradouro: ")
    registro["Número"] = input("Número: ")
    registro["Complemento"] = input("Complemento: ")
    registro["Bairro"] = input("Bairro: ")
    registro["DDD"] = input("DDD: ")
    registro["Telefone"] = input("Telefone: ")
    registro["Celular"] = input("Celular: ")

    cadastro.append(registro)
    print("Registro adicionado com sucesso!")


def listar_registros():
    for i, registro in enumerate(cadastro, 1):
        print(f"Registro {i}:")
        for chave, valor in registro.items():
            print(f"{chave}: {valor}")
        print()


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
