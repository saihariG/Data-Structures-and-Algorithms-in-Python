from collections import deque

class BreadthFirstSearch:

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
    def bfs(self, source_node):
        # Since graph may contain a cycle and we dont wanna visit a node more than once
        # Therefore we keep track of the nodes we visited
        visited = [False] * len(self.adj_list)
        queue = deque()

        queue.append(source_node)
        visited[source_node] = True

        while queue:
            u = queue.popleft()
            print(u, end=" ")

            # Visiting the neighbors of the popped node
            # Adding them into the queue if not visited
            for neighbor in self.adj_list[u]:
                if not visited[neighbor]:
                    queue.append(neighbor)
                    visited[neighbor] = True


if __name__ == "__main__":

    bfs = BreadthFirstSearch()

    bfs.add_edge(0, 1)
    bfs.add_edge(1, 2)
    bfs.add_edge(2, 3)
    bfs.add_edge(3, 0)
    bfs.add_edge(2, 4)

    print("BFS traversal starting from vertex 0:")
    bfs.bfs(0)

"""
Output:

BFS traversal starting from vertex 0:
0 1 3 2 4 
"""