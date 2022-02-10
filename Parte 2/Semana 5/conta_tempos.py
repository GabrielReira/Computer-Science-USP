import random
import ordenador
from time import time


class ContaTempos:

  def lista_aleatoria(self, n):
    lista = [random.randrange(1000) for x in range(n)]
    return lista
  
  def lista_quase_ordenada(self, n):
    lista = [x for x in range(n)]
    lista[n//10] = -14
    return lista
  

  def compara(self, n):
    def algoritmos(lista_aleatoria = True):
      # True gera uma lista aleatória e False uma lista
      # quase ordenada
      if lista_aleatoria:
        lista1 = self.lista_aleatoria(n)
      else:
        lista1 = self.lista_quase_ordenada(n)
      lista2 = lista1[:]
      lista3 = lista1[:]
      o = ordenador.Ordenador()

      # Selection sort
      antes = time()
      o.selecao_direta(lista1)
      depois = time()
      print(f'Seleção direta durou {depois - antes:.5f} segundos')
      # Bubble sort
      antes = time()
      o.bolha(lista2)
      depois = time()
      print(f'Bolha durou {depois - antes:.5f} segundos')
      # 'Short' bubble sort
      antes = time()
      o.bolha_curta(lista3)
      depois = time()
      print(f'Bolha curta durou {depois - antes:.5f} segundos')

    print('-'*7, 'Comparando listas aleatórias', '-'*7)
    algoritmos()
    print('\n', '-'*7, 'Comparando listas quase ordenadas', '-'*7)
    algoritmos(False)



c = ContaTempos()
c.compara(5000)
