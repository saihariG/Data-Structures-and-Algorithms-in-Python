# Usecase: To find the shortest path from once source node to all other nodes in a graph (Greedy approach)
# Works for both directed and undirected graphs 
# Undirected Graphs can be converted into directed graph by creating parallel edges

# Drawback: Dijkstra's Algorithm may or may not work in case of negative edges
class Dijkstras:

    def __init__(self, vertices):
        self.vertices = vertices
        self.edges = 0

        # adjacency matrix - use infinity to represent no edge
        self.adj_matrix = [[float('inf') for _ in range(vertices)] for _ in range(vertices)]

        self.visited = [False] * vertices # To track the visited nodes

        # To track the distances of all the nodes from the source node
        self.distance = [float('inf')] * vertices # Initialized to infinity


    def add_edge(self, u, v, weight):
        self.adj_matrix[u][v] = weight
        self.adj_matrix[v][u] = weight

        self.edges += 1

    # Time Complexity: O(v^2)
    def dijkstra(self, source):
        self.distance[source] = 0

        for _ in range(self.vertices - 1):
            # pick the node which is not visited yet and has a minimum distance
            u = self.pick_min()
            self.visited[u] = True

            for v in range(self.vertices):
                if (not self.visited[v] and
                        self.adj_matrix[u][v] != float('inf') and 
                        self.distance[u] + self.adj_matrix[u][v] < self.distance[v]):
                    # update the distance
                    self.distance[v] = self.distance[u] + self.adj_matrix[u][v]

        return self.distance


    def pick_min(self) -> int:
        min_val = float('inf')
        min_node = None

        for i in range(self.vertices):
            if not self.visited[i] and self.distance[i] < min_val:
                min_val = self.distance[i]
                min_node = i

        return min_node


if __name__ == "__main__":

    graph = Dijkstras(9)

    graph.add_edge(0,1,4)
    graph.add_edge(0,4,8)
    graph.add_edge(1,4,11)
    graph.add_edge(1,2,8)
    graph.add_edge(2,8,2)
    graph.add_edge(2,3,7)
    graph.add_edge(2,6,4)
    graph.add_edge(3,6,14)
    graph.add_edge(3,7,9)
    graph.add_edge(4,5,1)
    graph.add_edge(4,8,7)
    graph.add_edge(5,6,2)
    graph.add_edge(5,8,6)
    graph.add_edge(6,7,10)

    print(graph.dijkstra(0))

"""
Ouput: 
[0, 4, 12, 19, 8, 9, 11, 21, 14]
"""