while True:
    n = int(input('Digite um número: '))
    if n < 0:
        break

    fatorial = 1
    while n > 1:
        fatorial = fatorial * n
        n -= 1

    print(fatorial)