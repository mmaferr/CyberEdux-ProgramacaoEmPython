numero_inicial = int(input("Digite um número inicial para a contagem regressiva: "))

for i in range(numero_inicial, -1, -1):
    print(i)

#o input é definido como inteiro
#aqui usamos o loop 'for' para criar a contagem regressiva.
#'range':
#numero_inicial> é o número que a contagem regressiva começa
#-1 > é o valor final da contagem regressiva
#-1 >  É o passo de decremento. Isso significa que a cada iteração do loop, o valor de i será reduzido em 1.
#print(i): Dentro do loop, a instrução print(i) é usada para exibir o valor atual de i na tela. Isso significa que,
#a cada iteração do loop, o programa imprimirá o valor atual de i, que começa em numero_inicial e é decrementado em 1 a cada passo até atingir o valor final de -1.
