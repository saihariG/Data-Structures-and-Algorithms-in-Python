class ConnectedComponents:

    # Representing an Undirected Graph
    def __init__(self, vertices):
        self.V = vertices
        self.adj_list = [[] for _ in range(vertices)]

        self.edges = 0

    def add_edge(self, u, v):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

        self.edges += 1

    def connected_components(self):
        visited = [False] * len(self.adj_list)

        components = [] # To track the components

        for v in range(len(self.adj_list)):
            if not visited[v]:
                component = []
                self.dfs(v, visited, component)

                components.append(component)

        return components
    
    def dfs(self, node, visited, component):
        visited[node] = True
        component.append(node)

        for neighbor in self.adj_list[node]:
            if not visited[neighbor]:
                self.dfs(neighbor, visited, component)


if __name__ == "__main__":
    graph = ConnectedComponents(6)

    # Component 1
    graph.add_edge(0, 1)
    graph.add_edge(1, 2)

    # Component 2
    graph.add_edge(3, 4)

    # Node 5 is isolated -> Component 3

    components = graph.connected_components()

    print("Connected Components:")
    for i, comp in enumerate(components):
        print(f"Component {i + 1}:", comp)