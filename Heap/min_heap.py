"""

Heap, in other words is a Complete Binary Tree

For every node i, the value of node (except root node) is greater than or equal to its parent value

arr[parent(i)] <= arr[i]

Properties:

1. In Min Heap, the root node will always be the smallest element
2. Nodes will be inserted through Leaf nodes
3. Time Complexity to insert / Delete: O(log n)

"""

class MinHeap:

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
        while n > 1 and self.heap[n // 2] > self.heap[n]:
            # performing swap
            self.heap[n], self.heap[n // 2] = self.heap[n // 2], self.heap[n]
            # continue shifting up
            n = n // 2

    def print_min_heap(self):
        for i in range(1, self.n + 1):
            print(self.heap[i])


if __name__ == "__main__":
    min_heap =  MinHeap()

    min_heap.insert(4)
    min_heap.insert(5)
    min_heap.insert(2)
    min_heap.insert(6)
    min_heap.insert(1)
    min_heap.insert(3)

    print(f"Size: {min_heap.size()}")
    min_heap.print_min_heap()