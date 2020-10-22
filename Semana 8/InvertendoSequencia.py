valores = list()

while True:
    n = int(input('Digite um número: '))
    
    if n == 0:
        break
    else:
        valores.append(n)

for i in range(len(valores) - 1, -1, -1):
    print(valores[i])