número = int(input('Digite um número inteiro: '))

while número != 0:
    último_dígito = número % 10
    penúltimo_dígito = (número % 100) // 10

    número = número // 10

    if (último_dígito == penúltimo_dígito):
        print('sim')
        break
            
if (número == 0):
    print('não')