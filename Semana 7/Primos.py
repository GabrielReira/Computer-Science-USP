def é_primo(número):
    if número == 2:
        return True
    fator = 2

    # Quando achar o primeiro múltiplo já acaba o loop
    while (número % fator != 0) and (fator <= número / 2):
        fator += 1

    if (número % fator == 0) or (número == 1):
        return False
    else:
        return True



n = int(input())

while n > 0:
    if é_primo(n):
        print('Primo!')
    else:
        print('Não é primo.')

    n = int(input())