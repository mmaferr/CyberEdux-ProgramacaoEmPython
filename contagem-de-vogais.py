#12. Escreva um programa que peça ao usuário para inserir uma frase e conte quantas
#vogais (a, e, i, o, u) ela possui.
frase = input("Digite uma frase: ")
vogais = "aeiouAEIOU"
contagem = 0

for letra in frase:
    if letra in vogais:
        contagem += 1

print(f"A frase contém {contagem} vogais.")