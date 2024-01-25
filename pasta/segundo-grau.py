while True:
    entrada = input('\nOpções:\n1. Resolver uma equação de 2º grau\n2. Sair\n\nEscolha uma opção: ')
    if entrada == '':
        break
    if entrada == '1':
        def calc_delta(a, b, c):
            delta = b**2 - 4*a*c
            return delta

        def raizes(delta, a, b):
            x1 = -b + delta ** 0.5 / 2 * a
            x2 = (-b - delta ** 0.5) / (2* a)
            return x1, x2

        a = float(input('A: '))
        b = float(input('B: '))
        c = float(input('C: '))

        delta = calc_delta(a,b,c)
        x1, x2 = raizes(delta,a,b)
        if delta < 0:
            print('ERRO: DELTA NEGATIVO!!!')
            exit()
        print('O valor de delta é:', delta)
        print('O valor de x1 e x2 é:', x1, x2)

