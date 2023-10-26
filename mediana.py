entrada = input('Número: ')
valores = entrada.split('')
for i in range(len(valores)):
    valores[i] = int(valores[i])
valores.sort()
N = len(valores)
if N % 2 != 0:
    mediana = valores[N//2]
else:
    mediana = (valores[N//2] + valores[N//2-1])/2
print(mediana)