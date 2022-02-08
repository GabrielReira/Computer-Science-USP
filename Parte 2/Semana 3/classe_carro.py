def main():
  carro1 = Carro('brasília', 1968, 'amarela', 80)
  carro2 = Carro('mclaren', 2027, 'laranja', 350)
  carro1.acelere(40)
  carro2.acelere(200)
  carro1.acelere(50)
  carro1.pare()
  carro2.acelere(180)


class Carro:
  def __init__(self, modelo, ano, cor, vel_max):
    self.modelo = modelo
    self.ano = ano
    self.cor = cor
    self.vel = 0
    self.vel_max = vel_max

  def imprima(self):
    if self.vel == 0:
      print(f'{self.modelo} {self.cor} {self.ano} está parado.')
    elif self.vel < self.vel_max:
      print(f'{self.modelo} {self.cor} indo a {self.vel} Km/h.')
    else:
      print(f'{self.modelo} {self.cor} indo muito ráaaaaaapiiiiiidooooo!')

  def acelere(self, velocidade):
    self.vel += velocidade
    if self.vel > self.vel_max:
      self.vel = self.vel_max
    self.imprima()

  def pare(self):
    self.vel = 0
    self.imprima()


main()
