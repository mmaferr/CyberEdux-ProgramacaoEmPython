#13. Crie um programa que simule um jogo de adivinhação. O programa deve gerar um
#número aleatório e pedir ao usuário para adivinhar até acertar.
import random

numero_aleatorio = random.randint(1, 100)
tentativas = 0

while True:
    tentativa = int(input("Tente adivinhar o número (entre 1 e 100): ")
    tentativas += 1

    if tentativa == numero_aleatorio:
        print(f"Parabéns! Você acertou em {tentativas} tentativas.")
        break
    elif tentativa < numero_aleatorio:
        print("Tente um número maior.")
    else:
        print("Tente um número menor.")
