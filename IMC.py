#4. Escreva um programa que calcule o IMC (Índice de Massa Corporal) de uma pessoa com base no peso e altura
# inseridos pelo usuário. Em seguida, informe em qual faixa de IMC ela se encontra (abaixo do peso, peso normal, sobrepeso, etc).

peso = float(input("Digite seu peso em quilogramas: "))
altura = float(input("Digite sua altura em metros: "))

imc = peso / (altura ** 2)

if imc < 18.5:
    print("Abaixo do peso")
elif 18.5 <= imc < 24.9:
    print("Peso normal")
elif 25 <= imc < 29.9:
    print("Sobrepeso")
else:
    print("Obeso")
