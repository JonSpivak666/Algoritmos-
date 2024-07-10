def busqueda_binaria(lista, valor_buscado):
    """
    Realiza una búsqueda binaria en una lista ordenada.

    Parámetros:
    lista (list): Lista de elementos ordenados.
    valor_buscado: Valor a buscar en la lista.

    Retorna:
    int: Índice del valor buscado si se encuentra en la lista, de lo contrario -1.
    """
    limite_inferior = 0
    limite_superior = len(lista) - 1

    while limite_inferior <= limite_superior:
        punto_medio = (limite_inferior + limite_superior) // 2
        valor_medio = lista[punto_medio]

        if valor_medio == valor_buscado:
            return punto_medio
        elif valor_buscado < valor_medio:
            limite_superior = punto_medio - 1
        else:
            limite_inferior = punto_medio + 1

    return -1 

# Ejemplo 1
lista_ordenada = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
valor = 7
indice = busqueda_binaria(lista_ordenada, valor)

if indice != -1:
    print(f"El valor {valor} esta en el índice {indice}.")
else:
    print(f"El valor {valor} no esta en la lista.")
