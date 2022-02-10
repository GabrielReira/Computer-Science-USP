## [Exercício 1: Busca binária][]

Implemente a função **busca(lista, elemento)**, que busca um determinado elemento em uma lista e devolve o índice correspondente à posição do elemento encontrado. Utilize o algoritmo de **busca binária**. Nos casos em que o elemento buscado não existir na lista, a função deve devolver o booleano *False*.

Além de devolver o índice correspondente à posição do elemento encontrado, sua função deve imprimir cada um dos índices testados pelo algoritmo.

Exemplos:

```py
>>> busca(['a', 'e', 'i'], 'e')
>>> 1
# deve devolver => 1

>>> busca([1, 2, 3, 4, 5], 6)
>>> 2
>>> 3
>>> 4
# deve devolver => False

>>> busca([1, 2, 3, 4, 5, 6], 4)
>>> 2
>>> 4
>>> 3
# deve devolver => 3
```


## [Exercício 2: Ordenação com bubble sort][]

Implemente a função **bubble_sort(lista)**, que recebe uma lista com números inteiros como parâmetro e devolve esta lista ordenada. Utilize o algoritmo **bubble sort**.

Além de devolver uma lista ordenada, ao longo do processamento sua função deve imprimir o estado atual da lista toda vez que fizer uma alteração em seus elementos.

Exemplo:

```py
>>> bubble_sort([5, 1, 4, 2])
>>> [1, 5, 4, 2]
>>> [1, 4, 5, 2]
>>> [1, 4, 2, 5]
>>> [1, 2, 4, 5]
# deve devolver [1, 2, 4, 5]
```



[Exercício 1: Busca binária]: busca.py
[Exercício 2: Ordenação com bubble sort]: bubble_sort.py