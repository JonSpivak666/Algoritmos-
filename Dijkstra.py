import heapq
import networkx as nx
import matplotlib.pyplot as plt

def dijkstra(grafo, inicio):
    """
    Implementa el algoritmo de Dijkstra para encontrar el camino más corto en un grafo.

    Parámetros:
    grafo (dict): Grafo representado como un diccionario de adyacencias.
    inicio: Nodo inicial desde donde calcular las distancias más cortas.

    Retorna:
    tuple: Diccionario con las distancias más cortas desde el nodo inicial a cada nodo y el diccionario de predecesores.
    """
    # Inicializar distancias 
    distancias = {nodo: float('infinity') for nodo in grafo}
    distancias[inicio] = 0


    predecesores = {nodo: None for nodo in grafo}

    cola_prioridad = [(0, inicio)]
    heapq.heapify(cola_prioridad)

    while cola_prioridad:
        distancia_actual, nodo_actual = heapq.heappop(cola_prioridad)

        if distancia_actual > distancias[nodo_actual]:
            continue

        for vecino, peso in grafo[nodo_actual].items():
            distancia = distancia_actual + peso

            if distancia < distancias[vecino]:
                distancias[vecino] = distancia
                predecesores[vecino] = nodo_actual
                heapq.heappush(cola_prioridad, (distancia, vecino))

    return distancias, predecesores

def construir_camino(predecesores, inicio, fin):
    
    camino = []
    nodo_actual = fin
    while nodo_actual is not None:
        camino.insert(0, nodo_actual)
        nodo_actual = predecesores[nodo_actual]
    return camino if camino[0] == inicio else []

# Ejemplo 2
grafo = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

inicio = 'A'
fin = 'D'
distancias, predecesores = dijkstra(grafo, inicio)
camino = construir_camino(predecesores, inicio, fin)

print(f"Distancias más cortas desde el nodo {inicio}: {distancias}")
print(f"Camino más corto desde {inicio} hasta {fin}: {camino}")

G = nx.Graph()

for nodo in grafo:
    for vecino, peso in grafo[nodo].items():
        G.add_edge(nodo, vecino, weight=peso)

pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=700, font_size=10, font_weight='bold')
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

path_edges = list(zip(camino, camino[1:]))
nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='r', width=2)

plt.title(f"Camino más corto desde {inicio} hasta {fin}")
plt.show()
