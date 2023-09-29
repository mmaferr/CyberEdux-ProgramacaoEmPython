#ATIVIDADE 1: Declarando e Atricuindo Variáveis...
#1 - Declare uma variável chamada nome e atribua a ela seu próprio nome.
nome = "Maria"


#2 - Declare uma variável chamada idade e atribua a ela sua idade atual.
idade = 19


#3 - Declare uma variável chamada altura e atribua a ela sua altura em metros.
altura = 2.5


#4 - Declare uma variável chamada tem_pet e atribua a ela um valor booleano que indique se você tem um animal de estimação ou não.
tem_pet = True
tem_pet = False


#5 - Declare uma variável chamada frase e atribua a ela uma frase de sua escolha.
frase = "Quero muito almoçar!"


#ATIVIDADE 2: Operações com variáveis
#1 - Declare duas variáveis chamadas num1 e num2 e atribua a elas números inteiros de sua escolha]
num1 = 1
num2 = 2


#2 - Realize as seguintes operações e atribua os resultados a novas variáveis;
#Declare uma variável chamada mensagem e atribua a ela uma string que descreva as operações que você realizou.
#Imprima as variáveis num1, num2, soma, subtracao, multiplicacao, divisao e mensagem para mostrar os resultados e a mensagem descritiva
def soma():
    n1 = float(input('Digite o primeiro número: '))
    n2 = float(input('Digite o segundo número: '))
    print('Soma: ', n1+n2)

def subtração():
    n1 = float(input('Digite o primeiro número: '))
    n2 = float(input('Digite o segundo número: '))
    print('Subtração: ', n1-n2)

def multiplicação():
    n1 = float(input('Digite o primeiro número: '))
    n2 = float(input('Digite o segundo número: '))
    print('Multiplicação: ', n1*n2)

def divisão():
    n1 = float(input('Digite o primeiro número: '))
    n2 = float(input('Digite o segundo número: '))
    print('Divisão: ', n1/n2)

opção=1

while opção:
        print('0 - Sair')
        print('1 - Somar')
        print('2 - Subtrair')
        print('3 - Multiplicar')
        print('4 - Dividir')

        opção = int(input('Opção: '))

        if(opção==1):
            soma()
        if(opção==2):
            subtração()
        if(opção==3):
            multiplicação()
        if(opção==4):
            divisão()



#ATIVIDADE 3: Conversão de Tipos de Dados
# 1 - Declare uma variável numero_inteiro e atribua a ela um número inteiro de sua escolha.
numero_inteiro = 10

# 2 - Declare uma variável numero_decimal e atribua a ela um número de ponto flutuante (float) de sua escolha.
numero_decimal = 3.14

# 3 - Declare uma variável numero_em_texto e atribua a ela uma string que represente um número inteiro (por exemplo, "42") de sua escolha.
numero_em_texto = "42"



# 4 - Realize as seguintes conversões e atribua os resultados a novas variáveis:

# a. Converta numero_inteiro em um número de ponto flutuante e atribua-o a numero_inteiro_em_float.
numero_inteiro_em_float = float(numero_inteiro)

# b. Converta numero_decimal em um número inteiro e atribua-o a numero_decimal_em_int.
numero_decimal_em_int = int(numero_decimal)

# c. Converta numero_em_texto em um número inteiro e atribua-o a numero_em_texto_em_int.
numero_em_texto_em_int = int(numero_em_texto)

# d. Converta numero_em_texto em um número de ponto flutuante e atribua-o a numero_em_texto_em_float.
numero_em_texto_em_float = float(numero_em_texto)
