# Approach: Directed Acyclic Graph's for Topological Ordering / Kahn's algorithm
# Intuition: A directed graph has a cycle iff topological ordering is NOT possible

from collections import deque

class CycleInDirectedGraph:

    # Representing a directed graph
    def __init__(self, vertices):
        self.adj_list = {}

        self.vertices = vertices
        self.edges = 0

        # Number of incoming edges for every node
        self.indegree = [0] * vertices

    def add_edge(self, u, v):
        if u not in self.adj_list:
            self.adj_list[u] = []

        self.adj_list[u].append(v)
        self.edges += 1

        self.indegree[v] += 1

    # Time Complexity: O(V + E)
    # Space Complexity: O(V)
    def detect_cycle_in_directed_graph(self):
        queue = deque() 

        for i in range(self.vertices):
            if self.indegree[i] == 0:
                queue.append(i)

        processed_nodes = 0

        while queue:
            node = queue.popleft()
            processed_nodes += 1

            for neighbor in self.adj_list.get(node, []):
                self.indegree[neighbor] -= 1

                if self.indegree[neighbor] == 0:
                    queue.append(neighbor)
        
        # If not all vertices processed -> cycle exists
        # Idea: Nodes in a cycle: 
        #   - Always have indegree >= 1
        #   - Never enters a queue or gets processed
        return processed_nodes != self.vertices


if __name__ == "__main__":

    graph = CycleInDirectedGraph(4)

    graph.add_edge(0, 1)
    graph.add_edge(1, 2)
    graph.add_edge(2, 3)

    print("Has Cycle:", graph.detect_cycle_in_directed_graph())

    g = CycleInDirectedGraph(4)

    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(2, 0)  # cycle
    g.add_edge(2, 3)

    print("Has Cycle:", g.detect_cycle_in_directed_graph())

"""
Output:

Has Cycle: False
Has Cycle: True
"""