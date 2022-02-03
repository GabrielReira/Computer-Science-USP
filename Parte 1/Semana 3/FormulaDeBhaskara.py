from math import sqrt

a = float(input('Digite o valor de a: '))
b = float(input('Digite o valor de b: '))
c = float(input('Digite o valor de c: '))

discriminante = b ** 2 - 4 * a* c

if discriminante == 0:
    raíz = - b / (2 * a)
    print(f'a raiz desta equação é {raíz}')

elif discriminante > 0:
    raíz1 = (- b - sqrt(discriminante)) / (2 * a)
    raíz2 = (- b + sqrt(discriminante)) / (2 * a)
    print(f'as raízes da equação são {raíz1} e {raíz2}')

else:
    print('esta equação não possui raízes reais')