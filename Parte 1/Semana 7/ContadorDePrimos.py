def é_primo(x):
    cont = 0
    for i in range(1, x+1):
        if x % i == 0:
            cont += 1

    if cont == 2:
        return True
    else:
        return False

def n_primos(n):
    total = 0
    for i in range(2, n + 1):
        
        if é_primo(i):
            total += 1

    return total
