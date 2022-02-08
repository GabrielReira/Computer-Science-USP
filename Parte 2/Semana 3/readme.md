## [Exercício 1: Uma classe para triângulos][]

Defina a classe **Triangulo** cujo construtor recebe 3 valores inteiros correspondentes aos lados **a**, **b** e **c** de um triângulo.

A classe triângulo também deve possuir um método **perimetro**, que não recebe parâmetros e devolve um valor inteiro correspondente ao perímetro do triângulo.

```py
t = Triangulo(1, 1, 1)
# deve atribuir uma referência para um triângulo de lados 1, 1 e 1 à variável t 
```

Um objeto desta classe deve responder às seguintes chamadas:

```py
>>> t.a
1
>>> t. b
1
>>> t.c
1
>>> t.perimetro()
3
```


## [Exercício 2: Tipos de triângulos][]

Na classe triângulo, definida na Questão 1, escreva o metodo **tipo_lado()** que devolve uma string dizendo se o triângulo é:

- isósceles (dois lados iguais)
- equilátero (todos os lados iguais)
- escaleno (todos os lados diferentes)

Note que se o triângulo for equilátero, a função **não** deve devolver isóceles.

Exemplos:

```py
>>> t = Triangulo(4, 4, 4)
>>> t.tipo_lado()
'equilátero'

>>> u = Triangulo(3, 4, 5)
>>> u.tipo_lado()
'escaleno'
```



[Exercício 1: Uma classe para triângulos]: classe_triangulo.py
[Exercício 2: Tipos de triângulos]: tipo_triangulo.py