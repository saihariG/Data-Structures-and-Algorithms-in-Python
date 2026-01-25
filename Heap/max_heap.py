"""

Heap, in other words is a Complete Binary Tree

For every node i, the value of node (except root node) is less than or equal to its parent value

arr[parent(i)] >= arr[i]
 
Properties:

1. In Max Heap, the root node will always be the largest element
2. Nodes will be inserted through Leaf nodes

"""

class MaxHeap:

    def __init__(self):
        self.heap = [None]
        self.n = 0

    def is_empty(self):
        return self.n == 0

    def size(self):
        return self.n 

    def insert(self, data):
        self.n += 1
        self.heap.append(data)
        self.swim(self.n)

    def swim(self, n):
        while n > 1 and self.heap[n // 2] < self.heap[n]:
            # performing swap
            self.heap[n], self.heap[n // 2] = self.heap[n // 2], self.heap[n]
            n = n // 2 # To continue shifting up

    def print_max_heap(self):
        for i in range(1, self.n + 1):
            print(self.heap[i])

if __name__ == "__main__":
    max_heap = MaxHeap()

    max_heap.insert(4)
    max_heap.insert(5)
    max_heap.insert(2)
    max_heap.insert(6)
    max_heap.insert(1)
    max_heap.insert(3)

    print(max_heap.size())
    max_heap.print_max_heap()
