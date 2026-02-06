# Undirected Graphs: There is no particular direction between the nodes / vertices in the graph
# Simply, edges dont have any specific direction

# Graph is represented using an adjacency matrix (Two-dimensional array)
# 1 -> represents an edge exists
# 0 -> represents no edge b/w two nodes

class UndirectedGraph:

    def __init__(self):
        self.adj = {}
        self.edge = 0
    
    def add_edge(self, u, v):
        if u not in self.adj:
            self.adj[u] = []
        if v not in self.adj:
            self.adj[v] = []

        self.adj[u].append(v)
        self.adj[v].append(u)

        self.edge += 1

    def display(self):
        print(len(self.adj), "Vertices")
        print(self.edge, "Edges")
        for node in self.adj:
            print(node, "->", self.adj[node])

if __name__ == "__main__":

    undirected_graph = UndirectedGraph()

    undirected_graph.add_edge(0, 1)
    undirected_graph.add_edge(1, 2)
    undirected_graph.add_edge(2, 3)
    undirected_graph.add_edge(3, 0)


    undirected_graph.display()