número_anterior = int(input('Digite o primeiro número da sequência: '))
decrescer = True

while decrescer:
    número = int(input('Digite o próximo número da sequência: '))
    if número > número_anterior:
        decrescer = False
    número_anterior = número