#2. Soma de Números: Peça ao usuário para inserir números até que a soma deles atinja um valor específico.

valor_e = int(input("Digite o valor específico da soma: "))

# Inicializa a variável para rastrear a soma
soma = 0

# Inicia um loop while que continua até que a soma atinja ou exceda o valor alvo
while soma < valor_e:
    numero = float(input("Digite um número: "))  #Float é uma variável que representa os números reais.
    soma += numero  #ele vai somar o número que o usuário digitou + o próximo número

    if soma > valor_e:
        print("A soma excedeu o valor específico.")
        print(f"Soma final: {soma}")
        print(f"Valor específico: {valor_e}")
        break   #break > Interromper e encerrar um loop

    if soma == valor_e:
        print("A soma atingiu o valor específico.")
        print(f"Soma final: {soma}")
        print(f"Valor específico: {valor_e}")
