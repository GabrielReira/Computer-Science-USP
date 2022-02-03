n = int(input('Digite o valor de n: '))

if n <= 0:
    print('1')

else:
    fatorial = n

    while n != 1:
        n_anterior = n - 1
        fatorial = fatorial * n_anterior
        n = n_anterior

    print(fatorial)