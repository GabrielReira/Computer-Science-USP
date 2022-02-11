def soma_lista(lista):
  if len(lista) == 1:
    return lista[0]
  return lista[0] + soma_lista(lista[1:])
