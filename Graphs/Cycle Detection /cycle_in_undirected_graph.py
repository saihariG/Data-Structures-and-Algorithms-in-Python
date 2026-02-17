from collections import deque

# using breadth first search (queue)
class CycleInUndirectedGraph:

    def __init__(self):
        self.adj_list = {}
        self.edges = 0

    def add_edge(self, u, v):
        if u not in self.adj_list:
            self.adj_list[u] = []
        if v not in self.adj_list:
            self.adj_list[v] = []
        
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

        self.edges += 1

    def detect_cycle(self, source_node):

        visited = [False] * len(self.adj_list)
        queue = deque()

        # Tracking the node and its parent
        queue.append((source_node, -1))
        visited[source_node] = True 

        while queue:
            node, parent = queue.popleft()

            # Visiting the neighbors of the popped node
            # Adding them into the queue if not visited
            for neighbor in self.adj_list[node]:
                if not visited[neighbor]:
                    queue.append((neighbor, node))
                    visited[neighbor] = True

                elif neighbor != parent:
                    return True
                
        return False


if __name__ == "__main__":

    graph1 = CycleInUndirectedGraph()

    graph1.add_edge(0, 1)
    graph1.add_edge(1, 2)
    graph1.add_edge(2, 0)   # cycle here
    graph1.add_edge(2, 3)

    print(graph1.detect_cycle(0)) 

    graph2 = CycleInUndirectedGraph()

    graph2.add_edge(0, 1)
    graph2.add_edge(1, 2)
    graph2.add_edge(2, 3)  # Just a straight line
    print(graph2.detect_cycle(0))