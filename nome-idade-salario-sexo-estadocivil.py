#5. Faça um programa que leia e valide as seguintes informações:
#Nome: maior que 3 caracteres;
#Idade: entre 0 e 150;
#Salário: maior que zero;
#Sexo: 'f' ou 'm';
#Estado Civil: 's', 'c', 'v', 'd';
#(Use a função len(string) para saber o tamanho de um texto (número de caracteres)

while True:
    nome = input("Digite seu nome: ")
    if len(nome) > 3:
        break
    else:
        print("O nome deve conter mais de 3 caracteres querida(o).")

while True:
    idade = int(input("Digite sua idade: "))
    if 0 <= idade <=150:
        break
    else:
        print("A idade deve estar entre 0 e 150 anos")

while True:
    salario = float(input("Digite seu salário: "))
    if 0 < salario:
        break
    else:
        print("O salário deve ser maior que zero!")

while True:
    sexo = input("Digite seu sexo(f para feminino e m para masculinho): ")
    if sexo in ('f', 'm'):
        break
    else:
        print("Sexo deve ser 'f' ou 'm'.")

while True:
    estadocivil = input("Digite seu estado civil(s para solteiro, c para casado, v para viúvo, d para divorciado): ")
    if estadocivil in ('s', 'c', 'v', 'd'):
        break
    else:
        print("Estado civil deve ser 's', 'c', 'v' ou 'd'.")


print("Nome", nome)
print("Idade", nome)
print("Salário", nome)
print("Estado Civil", nome)

#len > é uma função em Python que é usada para calcular o tamanho, ou seja, o número de elementos, em uma sequência, como uma string, lista, tupla ou dicionário.

#A estrutura *while True* é útil em situações em que você deseja que um loop continue até que uma determinada condição seja atendida.
#Como a condição é True, o loop será executado repetidamente até que você o interrompa explicitamente com a instrução break quando a
#condição desejada for atendida.

#Em resumo, o while True é uma maneira de criar um loop infinito que pode ser interrompido manualmente quando necessário.
#Neste caso, ele faz com que o programa continue pedindo uma nota até que uma nota válida seja inserida.