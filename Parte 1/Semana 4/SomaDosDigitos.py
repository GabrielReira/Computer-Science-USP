número = int(input('Digite um número inteiro: '))

soma_dos_dígitos = 0

while número != 0:
    último_dígito = número % 10
    soma_dos_dígitos += último_dígito
    número_sem_último_dígito = número // 10
    número = número_sem_último_dígito

print(soma_dos_dígitos)