import pytest


def fatorial(n):
  if n < 0:
    return 0
  i = fatorial = 1
  while i <= n:
    fatorial *= i
    i += 1
  return fatorial

@pytest.mark.parametrize('entrada, valor_esperado', [
  (0, 1),
  (1, 1),
  (-10, 0),
  (4, 24),
  (5, 120)
])

def testa_fatorial(entrada, valor_esperado):
  assert fatorial(entrada) == valor_esperado
