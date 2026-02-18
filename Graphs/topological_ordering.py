# Criteria: Graph must be directed and Acyclic
# DAGs: Directed Acyclic Graphs

# Definition: Linear ordering of its vertices such that for every directed edge UV for vertex U to V,
# U comes before vertex v in the ordering

from collections import deque

class TopologicalOrdering:

    def __init__(self, vertices):
        self.adj_list = {}

        self.vertices = vertices
        self.edges = 0
        
        self.indegree = [0] * vertices

    def add_edge(self, u, v):
        if u not in self.adj_list:
            self.adj_list[u] = []

        self.adj_list[u].append(v) # since it's a directed graph
        self.edges += 1

        self.indegree[v] += 1

    
    # Kahn's Algorithm (BFS Approach)
    # Intuition:
    # 1. Compute in-degree (number of incoming edges) for every node
    # 2. Push all nodes with in-degree == 0 into a queue
    # Repeat,
    #   - Remove node from the queue
    #   - Add it to the result
    #   - Reduce in-degree of its neighbors
    #   - If any neighbor becomes 0, push to the queue
    # 
    # Time Complexity: O(V + E)
    def kahns_topological_ordering(self):
        queue = deque()

        for i in range(self.vertices):
            if self.indegree[i] == 0:
                queue.append(i)

        while queue:
            node = queue.popleft() 
            print(node, end=" ")

            for neighbor in self.adj_list.get(node, []):
                self.indegree[neighbor] -= 1

                if self.indegree[neighbor] == 0:
                    queue.append(neighbor)


if __name__ == "__main__":

    graph = TopologicalOrdering(5)

    graph.add_edge(0,1)
    graph.add_edge(0,3)
    graph.add_edge(1,3)
    graph.add_edge(1,2)
    graph.add_edge(3,2)
    graph.add_edge(3,4)

    graph.topological_ordering()

"""
Output : 0 1 3 2 4
"""