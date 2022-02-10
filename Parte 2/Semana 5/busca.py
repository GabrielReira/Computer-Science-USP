def busca(lista, elemento):
  primeiro = 0
  ultimo = len(lista) - 1

  while (primeiro <= ultimo):
    meio = (primeiro + ultimo) // 2
    print(meio)

    if lista[meio] == elemento:
      return meio
    else:
      if elemento < lista[meio]:
        ultimo = meio - 1
      else:
        primeiro = meio + 1
        
  return False
