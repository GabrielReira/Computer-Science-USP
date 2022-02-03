def remove_repetidos(lista):
    lista_sem_repetidos = list()

    for item in lista:
        if item not in lista_sem_repetidos:
            lista_sem_repetidos.append(item)
    
    return sorted(lista_sem_repetidos)