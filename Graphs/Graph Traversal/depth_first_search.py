class DepthFirstSearch:

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

    # Time Complexity: O(V+E)
    def dfs(self, source_node):
        # Since graph may contain a cycle and we dont wanna visit a node more than once
        # Therefore we keep track of the nodes we visited
        visited = [False] * len(self.adj_list)
        stack = [source_node]

        while stack:
            u = stack.pop()

            if not visited[u]:
                visited[u] = True
                print(u, end = " ")

                for neighbor in self.adj_list[u]:
                    if not visited[neighbor]:
                        stack.append(neighbor)


if __name__ == "__main__":

    dfs = DepthFirstSearch()

    dfs.add_edge(0, 1)
    dfs.add_edge(1, 2)
    dfs.add_edge(2, 3)
    dfs.add_edge(3, 0)
    dfs.add_edge(2, 4)

    print("DFS traversal starting from vertex 0:")
    dfs.dfs(0)

"""
Output:

DFS traversal starting from vertex 0:
0 3 2 4 1 
"""