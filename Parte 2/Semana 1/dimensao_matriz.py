def dimensoes(matriz):
  num_linhas = 0
  num_colunas = 0
  for linha in matriz:
    num_linhas += 1
    num_colunas = len(linha)
  
  print(f'{num_linhas}X{num_colunas}')
