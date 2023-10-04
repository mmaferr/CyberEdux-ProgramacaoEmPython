#19. Faça um programa que imprima os primeiros 50 termos da sequência de Fibonacci.
a, b = 0, 1
count = 0

while count < 50:
    print(a, end=" ")
    fib = a + b
    a = b
    b = fib
    count += 1