## [Exercício 1][]

Escreva a função **maximo** que recebe 2 números inteiros como parâmetro e devolve o maior deles.

Exemplos de execução no shell do Python:
```
>>> maximo(3, 4)
4
>>> maximo(0, -1)
0
```


## [Exercício 2][]

Escreva a função **maior_primo** que recebe um número inteiro maior ou igual a 2 como parâmetro e devolve o maior número primo menor ou igual ao número passado à função

Exemplos de execução no shell do Python:
```
>>> maior_primo(100)
97
>>> maior_primo(7)
7
```



## [Exercício 3][]

Escreva a função **vogal** que recebe um único caractere como parâmetro e devolve **True** se ele for uma vogal e **False** se for uma consoante.

Exemplos de execução no shell de Python:
```
>>> vogal("a")
True
>>> vogal("b")
False
>>> vogal("E")
True
```
Os valores True e False devolvidos devem ser do tipo bool (booleanos), e não strings


---


## [Exercício adicional 1][]

Escreva a função **fizzbuzz** que recebe como parâmetro um número inteiro e devolve:

- 'Fizz' se o número for divisível por 3 e não for divisível por 5;
- 'Buzz' se o número for divisível por 5 e não for divisível por 3;
- 'FizzBuzz' se o número for divisível por 3 e por 5;

Caso o número não seja divisível 3 e também não seja divisível por 5, ela deve devolver o número recebido como parâmetro.

Exemplos de execução no Python Shell:
```
>>> fizzbuzz(3)
"Fizz"
>>> fizzbuzz(5)
"Buzz"
>>> fizzbuzz(15)
"FizzBuzz"
>>> fizzbuzz(4)
4
```


## [Exercício adicional 2][]

Reescreva a função **maximo** do outro exercício, que devolve o maior valor dentre dois inteiros recebidos, para que ela passe a receber 3 valores inteiros como parâmetros e devolva o maior dentre eles.

Exemplos de execução no Python Shell:
```
>>> maximo(30, 14, 10)
30
>>> maximo(0, -1, 1)
1
```



[Exercício 1]: Maximo.py
[Exercício 2]: MaiorPrimo.py
[Exercício 3]: Vogal.py
[Exercício adicional 1]: FizzBuzz.py
[Exercício adicional 2]: MaximoEntreTres.py