class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.size = 0
        self.top = None

    def size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def push(self, data):
        new_node = ListNode(data)
        new_node.next = self.top # New node points to the old top
        self.top = new_node # Move top to new node
        self.size += 1

    def pop(self):
        if self.is_empty():
            return None

        popped = self.top.data

        self.top = self.top.next # Move top down one node
        self.size -= 1

        return popped

    def peek(self):
        if self.is_empty():
            return None

        return self.top.data

    # Display all elements
    def display(self):
        current = self.top
        print("Stack (top -> bottom): ", end="")
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

if __name__ == "__main__":
    s = Stack()

    s.push(10)
    s.push(20)
    s.push(30)
    s.display()
    print("Top element:", s.peek())
    print(s.pop())
    print(s.pop())
    print("Is stack empty?", s.is_empty())
    print(s.pop())
    print(s.pop())  # Trying to pop from an empty stack