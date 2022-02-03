def maior_elemento(lista):
    maior = lista[0]

    for i in range(len(lista)):
        if lista[i] > maior:
            maior = lista[i]
    
    return maior