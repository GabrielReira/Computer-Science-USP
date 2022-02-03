def cria_matriz(num_linhas, num_colunas, valor):
  matriz = []
  for i in range(num_linhas):
    linha = []
    for j in range(num_colunas):
      linha.append(valor)
    matriz.append(linha)

  return matriz
