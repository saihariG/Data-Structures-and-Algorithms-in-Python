# Works even when the graph has negative edges
# Usecase: To detect Negative weight cycles in a graph (Directed)

class EdgePair:
    def __init__(self, _from, to, weight):
        self._from = _from
        self.to = to
        self.weight = weight 

class BellmanFord:

    def __init__(self, vertices):
        self.vertices = vertices
        # To track the distances of all the nodes from the source node
        self.distance = [float('inf')] * vertices

    # Intuition:
    #   1. Initialize distances
    #   2. Relax all edges V-1 times
    #   3. Do one extra pass to check for negative cycles
    # Time Complexity: O(vertices * Edges) 
    def bellman_ford(self, source, edges):
        self.distance[source] = 0
        updated = False # To detect negative cycle

        # Include (V-1) edges to cover all the vertices
        for _ in range(self.vertices-1):
            updated = False

            for edge in edges:
                u = edge._from
                v = edge.to
                w = edge.weight

                if self.distance[u] != float('inf') and self.distance[u] + w < self.distance[v]:
                    self.distance[v] = self.distance[u] + w
                    updated = True

            if not updated:
                break

        # Now check by relaxing once more if we have a negative edge cycle
        for i in range(len(edges)):
            edge_pair = edges[i]

            u = edge_pair._from
            v = edge_pair.to
            w = edge_pair.weight

            if self.distance[u] != float('inf') and self.distance[u] + w < self.distance[v]:
                print("Graph has a -ve edge cycle")
                break

if __name__ == "__main__":

    graph = BellmanFord(5)

    edges = [
        EdgePair(0, 1, -1),
        EdgePair(0, 2, 4),
        EdgePair(1, 2, 3),
        EdgePair(1, 3, 2),
        EdgePair(1, 4, 2),
        EdgePair(3, 2, 5),
        EdgePair(3, 1, 1),
        EdgePair(4, 3, -3)
    ]

    graph.bellman_ford(0, edges)
    print(graph.distance)

    g = BellmanFord(4)
    edges = [
        EdgePair(0, 1, 1),
        EdgePair(1, 2, -1),
        EdgePair(2, 3, -1),
        EdgePair(3, 1, -1)
    ]

    g.bellman_ford(0, edges) # Graph has a -ve edge cycle

"""
Output:
[0, -1, 2, -2, 1]
"""