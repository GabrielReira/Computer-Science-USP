n = int(input('Digite o valor de n: '))

i = 1
número = 0

while i <= n:
    número = número + 1
    if (número % 2 != 0):
        i = i + 1
        print(número)