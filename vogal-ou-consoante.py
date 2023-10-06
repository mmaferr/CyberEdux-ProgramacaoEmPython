#1. Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
print('Olá! Vamos verificar se uma letra é vogal ou consoante!\n')
letra = input('Digite uma letra: ').upper()
while len(letra) !=1:
    letra = input('Você pode digitar apenas uma letra!\nTente novamente: ')
if letra == 'A' or letra == 'E' or letra == 'I' or letra == 'O' or letra == 'U':
    print(f'A letra {letra} é uma Vogal!!!')
else:
    print(f'A letra {letra} é Consoante!!!')