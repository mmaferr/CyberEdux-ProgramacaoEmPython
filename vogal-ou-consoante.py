#1. Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
#criar a variável que vai receber a letra digitada
letra = input("Digite uma letra: ").upper()

# Desenvolvendo a lógica
if (
    letra == "A"
    or letra == "E"
    or letra == "I"
    or letra == "O"
    or letra == "U"
):
    print("Vogal")
else:
    print("Consoante")
