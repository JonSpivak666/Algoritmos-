import heapq
import networkx as nx
import matplotlib.pyplot as plt

def prim(grafo, inicio):
    """
    Implementa el algoritmo de Prim para encontrar el Árbol de Expansión Mínima (MST).

    Parámetros:
    grafo (dict): Grafo representado como un diccionario de adyacencias.
    inicio: Nodo inicial desde donde comenzar el MST.

    Retorna:
    list: Lista de aristas que componen el MST.
    """
    mst = []
    visitados = set([inicio])
    aristas = [(peso, inicio, vecino) for vecino, peso in grafo[inicio].items()]
    heapq.heapify(aristas)

    while aristas:
        peso, desde, hasta = heapq.heappop(aristas)
        if hasta not in visitados:
            visitados.add(hasta)
            mst.append((desde, hasta, peso))

            for siguiente, peso in grafo[hasta].items():
                if siguiente not in visitados:
                    heapq.heappush(aristas, (peso, hasta, siguiente))

    return mst

# Ejemplo 4
grafo = {
    'A': {'B': 2, 'C': 3},
    'B': {'A': 2, 'C': 1, 'D': 1},
    'C': {'A': 3, 'B': 1, 'D': 5, 'E': 4},
    'D': {'B': 1, 'C': 5, 'E': 7},
    'E': {'C': 4, 'D': 7}
}

inicio = 'A'
mst = prim(grafo, inicio)

print("Aristas del Árbol de Expansión Mínima (MST):")
for desde, hasta, peso in mst:
    print(f"{desde} - {hasta} : {peso}")

G = nx.Graph()

for nodo in grafo:
    for vecino, peso in grafo[nodo].items():
        G.add_edge(nodo, vecino, weight=peso)

pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=700, font_size=10, font_weight='bold')
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

mst_edges = [(desde, hasta) for desde, hasta, peso in mst]
nx.draw_networkx_edges(G, pos, edgelist=mst_edges, edge_color='r', width=2)

plt.title(f"Árbol de Expansión Mínima (MST) desde el nodo {inicio}")
plt.show()
