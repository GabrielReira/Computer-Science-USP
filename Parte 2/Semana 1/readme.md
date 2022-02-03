## [Exercício 1: Tamanho da matriz][]

Escreva uma função dimensoes(matriz) que recebe uma matriz como parâmetro e imprime as dimensões da matriz recebida, no formato iXj.

Exemplos:

```py
>>>minha_matriz = [[1], [2], [3]]
>>>dimensoes(minha_matriz)
3X1
```
```py
>>>minha_matriz = [[1, 2, 3], [4, 5, 6]]
>>>dimensoes(minha_matriz)
2X3
```


## [Exercício 2: Soma de matrizes][]

Escreva a função soma_matrizes(m1, m2) que recebe 2 matrizes e devolve uma matriz que represente sua soma caso as matrizes tenham dimensões iguais. Caso contrário, a função deve devolver False.

Exemplos:

```py
>>>m1 = [[1, 2, 3], [4, 5, 6]]
>>>m2 = [[2, 3, 4], [5, 6, 7]]
>>>soma_matrizes(m1, m2)
[[3, 5, 7], [9, 11, 13]]
```
```py
>>>m1 = [[1], [2], [3]]
>>>m2 = [[2, 3, 4], [5, 6, 7]]
>>>soma_matrizes(m1, m2)
False
```



[Exercício 1: Tamanho da matriz]: dimensao_matriz.py
[Exercício 2: Soma de matrizes]: soma_matriz.py