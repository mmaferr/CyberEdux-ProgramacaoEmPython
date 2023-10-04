#10. Desenvolva um programa que peça ao usuário para inserir um número e, em seguida,
#imprima a sequência de Fibonacci até o termo inserido.

n = int(input("Digite o número de termos da sequência de Fibonacci: "))

a, b = 0, 1
count = 0

if n <= 0:
    print("Por favor, insira um número positivo.")
elif n == 1:
    print("Sequência de Fibonacci até o 1º termo:", a)
else:
    print("Sequência de Fibonacci:")
    while count < n:
        print(a, end=" ")
        fib = a + b
        a = b
        b = fib
        count += 1


