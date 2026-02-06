class UndirectedGraph:

    def __init__(self):
        self.adj_list = {}
        self.edges = 0 # no. of edges in graph
    
    def add_edge(self, u, v):
        if u not in self.adj_list:
            self.adj_list[u] = []
        if v not in self.adj_list:
            self.adj_list[v] = []

        self.adj_list[u].append(v)
        self.adj_list[v].append(u) # because it is an undirected graph

        self.edges += 1

    def display(self):
        print(len(self.adj_list), "vertices, ", self.edges, "edges")
        for node in self.adj_list:
            print(node, ":", self.adj_list[node])

if __name__ == "__main__":

    undirected_graph = UndirectedGraph()

    undirected_graph.add_edge(0, 1)
    undirected_graph.add_edge(1, 2)
    undirected_graph.add_edge(2, 3)
    undirected_graph.add_edge(3, 0)


    undirected_graph.display()

"""
Output: 

4 vertices,  4 edges
0 : [1, 3]
1 : [0, 2]
2 : [1, 3]
3 : [2, 0]

"""