def primeiro_lex(lista):
  escolhida = lista[0]
  for palavra in lista:
    if palavra < escolhida:
      escolhida = palavra
  return escolhida
