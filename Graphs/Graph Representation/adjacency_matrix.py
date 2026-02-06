# Undirected Graphs: There is no particular direction between the nodes / vertices in the graph
# Simply, edges dont have any specific direction

# Graph is represented using an adjacency matrix (Two-dimensional array)
# 1 -> represents an edge exists
# 0 -> represents no edge b/w two nodes

class UndirectedGraph:

    def __init__(self, nodes):
        self.adj_matrix = [[0] * nodes for _ in range(nodes)]
        self.edges = 0 # no. of edges in graph
        self.vertices = nodes # no. of vertices/nodes in the graph
    
    def add_edge(self, u, v):
        self.adj_matrix[u][v] = 1
        self.adj_matrix[v][u] = 1 # because it is an undirected graph

        self.edges += 1

    def display(self):
        print(self.vertices, "Vertices")
        print(self.edges, "Edges")
        
        for node in self.adj_matrix:
            print(node)

if __name__ == "__main__":

    undirected_graph = UndirectedGraph(4)

    undirected_graph.add_edge(0, 1)
    undirected_graph.add_edge(1, 2)
    undirected_graph.add_edge(2, 3)
    undirected_graph.add_edge(3, 0)


    undirected_graph.display()

"""
output:

4 Vertices
4 Edges
[0, 1, 0, 1]
[1, 0, 1, 0]
[0, 1, 0, 1]
[1, 0, 1, 0]

"""