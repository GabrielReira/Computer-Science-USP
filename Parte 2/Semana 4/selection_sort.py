class Ordenador:
  def selecao_direta(self, lista):
    fim = len(lista)

    for i in range(fim -1):
      # Inicialmente, o menor elemento visto é o i-ésimo
      pos_menor = i
      for j in range(i+1, fim):
        if lista[j] < lista[pos_menor]:
          pos_menor = j

      # Coloca o menor elemento encontrado no início da sub-lista
      # Troca de lugar os elementos nas posições i e 'pos_menor'
      lista[i], lista[pos_menor] = lista[pos_menor], lista[i]
