def cria_matriz(num_linhas, num_colunas):
  matriz = []
  for i in range(num_linhas):
    linha = []
    for j in range(num_colunas):
      valor = int(input(
        f'Digite o elemento [{i}][{j}]: '
      ))
      linha.append(valor)
    matriz.append(linha)

  return matriz


def le_matriz():
  linhas = int(input('Número de linhas: '))
  colunas = int(input('Número de colunas: '))
  return cria_matriz(linhas, colunas)

print(le_matriz())