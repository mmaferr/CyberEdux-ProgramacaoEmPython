#2. Crie um programa que determine se um ano é bissexto ou não. (Dica: um ano bissexto é divisível por 4, exceto por
#anos que são divisíveis por 100, a menos que também sejam divisíveis por 400).

ano = int(input("Digite um ano: "))

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print("O ano é bissexto.")
else:
    print("O ano não é bissexto.")
