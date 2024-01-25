# Crie uma lista com os números pares de 1 a 20.

n_pares = []
for n in range(1, 21):
    if n % 2 == 0:
        n_pares.append(n)
    print(n_pares)
