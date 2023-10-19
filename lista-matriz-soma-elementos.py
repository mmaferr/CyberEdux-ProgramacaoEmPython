# Crie uma lista de listas que represente uma matriz 3x3 e escreva um código para
# calcular a soma de todos os elementos.

matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

soma = 0
for linha in matriz:
    for elemento in linha:
        soma += elemento

print('A soma de todos os elementos da lista é: ', soma)