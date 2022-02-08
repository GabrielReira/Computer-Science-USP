def multiplica_matrizes(m1, m2):
  # Verificar condição de existência
  if (len(m1[0]) != len(m2)):
    return False

  # A matriz resultante possui o mesmo número de linhas da primeira
  # matriz e o mesmo número de colunas da segunda matriz
  num_linhas, num_colunas  = len(m1), len(m2[0])
  m_resultante = [[ 0 for j in range(num_colunas) ] for i in range(num_linhas)]

  # O número de somas que será realizado para preencher cada
  # espaço da matriz resultante é igual ao número de colunas
  # da matriz 1 (ou do número de linhas da matriz 2)
  num_somas = len(m1[0])

  for lin in range(num_linhas):
    for col in range(num_colunas):
      soma = 0
      for k in range(num_somas):
        soma += m1[lin][k] * m2[k][col]
      m_resultante[lin][col] = soma
  
  return m_resultante


# Teste
if __name__ == '__main__':
  A = [[3, 2], [5, -1]]
  B = [[6, 4, -2], [0, 7, 1]]
  print(multiplica_matrizes(A, B))
