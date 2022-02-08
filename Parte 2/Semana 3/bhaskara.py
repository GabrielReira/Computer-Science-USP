from math import sqrt

class Bhaskara:
  def main(self):
    a = float(input('Digite o valor de a: '))
    b = float(input('Digite o valor de b: '))
    c = float(input('Digite o valor de c: '))
    print(self.calcula_raizes(a, b, c))

  def discriminante(self, a, b, c):
    return b ** 2 - 4 * a* c

  def calcula_raizes(self, a, b, c):
    delta = self.discriminante(a, b, c)
    if delta == 0:
      raiz = - b / (2 * a)
      return 1, raiz

    elif delta > 0:
      raiz1 = (- b - sqrt(delta)) / (2 * a)
      raiz2 = (- b + sqrt(delta)) / (2 * a)
      return 2, raiz1, raiz2

    else:
      return 0
