def merge_sort(arr):
    """
    Implementa el algoritmo de ordenamiento por fusión.

    Parámetros:
    arr (list): Lista de elementos a ordenar.

    Retorna:
    list: Lista ordenada.
    """
    if len(arr) <= 1:
        return arr

    # Dividir el arreglo 
    mitad = len(arr) // 2
    izquierda = arr[:mitad]
    derecha = arr[mitad:]

    izquierda = merge_sort(izquierda)
    derecha = merge_sort(derecha)

    return merge(izquierda, derecha)

def merge(izquierda, derecha):
    """
    Fusiona dos listas ordenadas en una sola lista ordenada.

    Parámetros:
    izquierda (list): Lista ordenada de elementos.
    derecha (list): Lista ordenada de elementos.

    Retorna:
    list: Lista fusionada y ordenada.
    """
    resultado = []
    i = j = 0

    # Fusionar las listas ordenadas
    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] < derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1

    while i < len(izquierda):
        resultado.append(izquierda[i])
        i += 1

    while j < len(derecha):
        resultado.append(derecha[j])
        j += 1

    return resultado

# Ejemplo 3
arr = [38, 27, 43, 3, 9, 82, 10]
arr_ordenado = merge_sort(arr)
print(f"Arreglo ordenado: {arr_ordenado}")
