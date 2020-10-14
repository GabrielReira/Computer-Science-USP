print('Digite uma sequência de valores terminada por zero.')

soma = 0
valor = 1

while valor != 0:
    valor = float(input('Digite um valor a ser somado: '))
    soma += valor

print('A soma desses valores foi:', soma)