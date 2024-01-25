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











