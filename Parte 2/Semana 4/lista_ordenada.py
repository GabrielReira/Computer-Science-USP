def selecao_direta(lista):
  qntd_trocas = 0
  fim = len(lista)
  for i in range(fim -1):
    pos_menor = i
    for j in range(i+1, fim):
      if lista[j] < lista[pos_menor]:
        pos_menor = j
        qntd_trocas += 1
    lista[i], lista[pos_menor] = lista[pos_menor], lista[i]

  return qntd_trocas


def ordenada(lista):
  if selecao_direta(lista) == 0:
    return True
  return False
