## [Exercício 1: Letras maiúsculas][]

Escreva a função **maiusculas(frase)** que recebe uma frase (uma string) como parâmetro e devolve uma string com as letras maiúsculas que existem nesta frase, na ordem em que elas aparecem.

Para resolver este exercício, pode ser útil verificar uma tabela ASCII, que contém os valores de cada caractere. Ver https://pt.wikipedia.org/wiki/ASCII

Note que para simplificar a solução do exercício, as frases passadas para a sua função não possuirão caracteres que não estejam presentes na tabela ASCII apresentada, como *ç*, *á*, *É*, *ã*, etc.

**Dica**: Os valores apresentados na tabela são os mesmos devolvidos pela função *ord* apresentada nas aulas.

Exemplos:

```py
maiusculas('Programamos em python 2?')
# deve devolver 'P'

maiusculas('Programamos em Python 3.')
# deve devolver 'PP'

maiusculas('PrOgRaMaMoS em python!')
# deve devolver 'PORMMS'
```


## [Exercício 2: Menor nome][]

Como pedido no primeiro vídeo desta semana, escreva uma função **menor_nome(nomes)** que recebe uma lista de strings com nome de pessoas como parâmetro e devolve o nome mais curto presente na lista.

A função deve ignorar espaços antes e depois do nome e deve devolver o menor nome presente na lista. Este nome deve ser devolvido com a primeira letra maiúscula e seus demais caracteres minúsculos, independente de como tenha sido apresentado na lista passada para a função.

Quando houver mais de um nome com o menor comprimento dentre os nomes na lista, a função deve devolver o primeiro nome com o menor comprimento presente na lista.

Exemplos:

```py
menor_nome(['maria', 'josé', 'PAULO', 'Catarina'])
# deve devolver 'José'

menor_nome(['maria', ' josé  ', '  PAULO', 'Catarina  '])
# deve devolver 'José'

menor_nome(['Bárbara', 'JOSÉ  ', 'Bill'])
# deve devolver José
```



[Exercício 1: Letras maiúsculas]: dimensao_matriz.py
[Exercício 2: Menor nome]: soma_matriz.py