largura = int(input('digite a largura: '))
altura = int(input('digite a altura: '))

i = 0
while i < altura:
    j = 0
    while j < largura:
        # A primeira e última linha sempre preenchidas,
        # assim como a primeira ou última coluna
        if (i == 0) or (i == altura - 1) or (j == 0) or (j == largura - 1):
            print('#', end='')
        else:
            print(' ', end='')
        j += 1
    print()
    i += 1