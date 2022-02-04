def menor_nome(lista):
  nome_mais_curto = lista[0]
  for nome in lista:
    if len(nome.strip()) < len(nome_mais_curto):
      nome_mais_curto = nome.strip()

  return nome_mais_curto.capitalize()
