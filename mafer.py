#calcula média
nota1 = input('Digite a nota 1:')
nota2 = input('Digite a nota 2:')
nota3 = input('Digite a nota 3:')

soma =float(nota1)+ float(nota2) + float(nota3)
media = soma/ 3

print('Minha querida, a sua média é:',media)

if(media >= 7):
    print('Aprovado(a)!')

else:
    print('Reprovado(a)!')


#Verificação de Números Pares
n = int(input ('Digite um número:'))

if(n % 2 == 0 ):
    print('O número é par!')

else:
    print('O número é ímpar!')






