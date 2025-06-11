# Carlos Alejandro Mercado Villalvazo
class Graph():

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]

    def printSolution(self, dist):
        print("Vértice \t Distancia desde el origen")
        for node in range(self.V):
            print(node, "\t\t", dist[node])

    # Encontrar el vértice con la distancia mínima que no está incluido en el conjunto de caminos más cortos
    def minDistance(self, dist, sptSet):

        # Inicializar la mínima distancia
        min = 1e7

        # Buscar que no esté incluido en el conjunto de caminos más cortos
        for v in range(self.V):
            if dist[v] < min and sptSet[v] == False:
                min = dist[v]
                min_index = v

        return min_index

    # Función que implementa el algoritmo de Dijkstra para encontrar el camino más corto desde el vértice fuente
    def dijkstra(self, src):

        dist = [1e7] * self.V
        print("Inicializando distancias:", dist)
        dist[src] = 0
        print(f"Distancia desde el origen {src} inicializada a 0")
        sptSet = [False] * self.V
        print("Conjunto de caminos más cortos inicializado:", sptSet)

        for cout in range(self.V):

            # Escoger el vértice con la distancia mínima desde el conjunto de vértices no incluídos en el conjunto de caminos más cortos
            u = self.minDistance(dist, sptSet)
            print("Vértice escogido:", u)

            # Añadir el vértice escogido al conjunto de caminos más cortos
            sptSet[u] = True

            # Actualizar la distancia de los vértices adyacentes al vértice escogido, si el nuevo camino es más corto
            for v in range(self.V):
                if (self.graph[u][v] > 0 and 
                   sptSet[v] == False and 
                   dist[v] > dist[u] + self.graph[u][v]):
                    dist[v] = dist[u] + self.graph[u][v]
                    print(f"Actualizando distancia del vértice {v} a {dist[v]}")
                    print("Estado actual de distancias:", dist)

        self.printSolution(dist)

# Ejemplo de uso
g = Graph(9)
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
           [4, 0, 8, 0, 0, 0, 0, 11, 0],
           [0, 8, 0, 7, 0, 4, 0, 0, 2],
           [0, 0, 7, 0, 9, 14, 0, 0, 0],
           [0, 0, 0, 9, 0, 10, 0, 0, 0],
           [0, 0, 4, 14, 10, 0, 2, 0, 0],
           [0, 0, 0, 0, 0, 2, 0, 1, 6],
           [8, 11, 0, 0, 0, 0, 1, 0, 7],
           [0, 0, 2, 0, 0, 0, 6, 7, 0]
           ]

g.dijkstra(0)
