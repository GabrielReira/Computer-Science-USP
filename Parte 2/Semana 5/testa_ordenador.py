import pytest
import ordenador
from conta_tempos import ContaTempos


class TestaOrdenador:

  @pytest.fixture
  def o(self):
    return ordenador.Ordenador()

  @pytest.fixture
  def lista_al(self):
    c = ContaTempos()
    return c.lista_aleatoria(100)

  @pytest.fixture
  def lista_qo(self):
    c = ContaTempos()
    return c.lista_quase_ordenada(100)

  def esta_ordenada(self, lista):
    for i in range(len(lista)-1):
      if lista[i] > lista[i+1]:
        return False
      return True

  def testa_bolha_curta_al(self, o, lista_al):
    o.bolha_curta(lista_al)
    assert self.esta_ordenada(lista_al)

  def testa_selecao_direta_al(self, o, lista_al):
    o.selecao_direta(lista_al)
    assert self.esta_ordenada(lista_al)

  def testa_bolha_curta_qo(self, o, lista_qo):
    o.bolha_curta(lista_qo)
    assert self.esta_ordenada(lista_qo)

  def testa_selecao_direta_qo(self, o, lista_qo):
    o.selecao_direta(lista_qo)
    assert self.esta_ordenada(lista_qo)
  