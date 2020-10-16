def fatorial(x):
    total = 1

    if x < 0:
        print('Erro. Fatorial negativo.')
        exit(0)
    else:
        while x > 1:
            total *= x
            x -= 1

    return total


def coeficiente_binomial(n, k):
    if (n == k) or (k == 0):
        return 1
    else:
        return (fatorial(n)) // (fatorial(k) * fatorial(n - k))
