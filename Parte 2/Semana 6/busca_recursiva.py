def busca_binaria(lista, elemento, min=0, max=None):
  if max == None:
    max = len(lista) - 1
  
  if max < min:
    return False
  else:
    meio = (min + max) // 2
  
  if lista[meio] > elemento:
    return busca_binaria(lista, elemento, min, meio-1)
  elif lista[meio] < elemento:
    return busca_binaria(lista, elemento, meio+1, max)
  else:
    return meio


# Testes
import pytest

numeros = [-10, 0, 10, 20, 30, 40, 50, 60, 70]
@pytest.mark.parametrize('lista, valor, esperado', [
  (numeros, -10, 0),
  (numeros, 0, 1),
  (numeros, 5, False),
  (numeros, 10, 2),
  (numeros, 20, 3),
  (numeros, 30, 4),
  (numeros, 40, 5),
  (numeros, 50, 6),
  (numeros, 60, 7),
  (numeros, 70, 8),
  (numeros, 100, False)
])
def testa_busca_binaria(lista, valor, esperado):
  assert busca_binaria(lista, valor) == esperado
