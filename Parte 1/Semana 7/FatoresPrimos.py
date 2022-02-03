número = int(input('Número inteiro maior que 1: '))

fator = 2

while número > 1:
    multiplicidade = 0

    while número % fator == 0:
        número = número / fator
        multiplicidade += 1

    if multiplicidade > 0:
        print(f'Fator {fator} tem multiplicidade = {multiplicidade}')

    fator += 1