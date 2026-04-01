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
        self.heap = [None] # dummy element for 1-based indexing
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

    # Algorithm: 
   # 1. To delete the root node, replace it with the last element
   # 2. Heapify down and restore the heap property
    def delete_min(self):
        if self.n == 0:
            return
        
        min = self.heap[1]
        self.heap[1] = self.heap[n]
        self.heap.pop()
        self.n -= 1

        # heapify down
        self.sink()
        return min
    
    # Left child: 2*i
    # Right child: 2*i + 1
    def sink(self):
        i = 1 # parent

        # while atleast one child exists
        while 2*i <= self.n:

            j = 2*i # Left child

            # pick the smaller child
            if j < self.n: 
                if self.heap[j] > self.heap[j+1]:
                    j += 1
                
            # if parent is already smaller, Stop
            if self.heap[i] <= self.heap[j]:
                break

            # swap with the smaller child
            self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
            # move down
            i = j 

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