#20. Escreva um programa que simule uma calculadora simples, onde o usuário pode
#escolher entre operações de adição, subtração, multiplicação e divisão.
def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return "Divisão por zero não é permitida."
    return a / b

print("Escolha a operação:")
print("1. Adição")
print("2. Subtração")
print("3. Multiplicação")
print("4. Divisão")

escolha = input("Digite o número da operação desejada: ")

if escolha in ("1", "2", "3", "4"):
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if escolha == "1":
        print("Resultado:", soma(num1, num2))
    elif escolha == "2":
        print("Resultado:", subtracao(num1, num2))
    elif escolha == "3":
        print("Resultado:", multiplicacao(num1, num2))
    elif escolha == "4":
        print("Resultado:", divisao(num1, num2))
else:
    print("Escolha inválida.")