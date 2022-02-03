quantidade = int(input('Digite a quantidade de números a serem multiplicados: '))

produto = 1
i = 0

while i < quantidade:
    valor = int(input('Digite o valor a ser multiplicado: '))
    produto *= valor
    i += 1

print('O produto dos valores digitados é: ', produto)