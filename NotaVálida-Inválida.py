#3. Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido
#e continue pedindo até que o usuário informe um valor válido.

while True:
    nota = float(input("Digite uma nota entre 0 a 10: "))

    if 0 <= nota <= 10:
        print("Nota válida:", nota)
        break   #o loop será encerrado
    else:
        print("Nota inválida. Por favor, digite uma nota entre 0 a 10: ")
                #ficará em loop até o usuário digitae ua nota válida


#A estrutura *while True* é útil em situações em que você deseja que um loop continue até que uma determinada condição seja atendida.
#Como a condição é True, o loop será executado repetidamente até que você o interrompa explicitamente com a instrução break quando a
#condição desejada for atendida.

#Em resumo, o while True é uma maneira de criar um loop infinito que pode ser interrompido manualmente quando necessário.
#Neste caso, ele faz com que o programa continue pedindo uma nota até que uma nota válida seja inserida.