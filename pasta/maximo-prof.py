def maximo(lista):
    aux = lista[0]
    for v in lista:
        if v > aux:
            aux = v
    return aux

entrada = input('Digite uma sequência de números: ')
valores = entrada.split((' '))
for i in range(len(valores)):
    valores[i] = float(valores[i])
print(maximo(valores))
