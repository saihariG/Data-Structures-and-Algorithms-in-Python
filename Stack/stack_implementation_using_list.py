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
        new_node.next = self.top # linking
        self.top = new_node
        self.size += 1

    def pop(self):
        if self.is_empty():
            return None

        popped = self.top.data

        self.top = self.top.next
        self.size -= 1

        return popped

    def peek(self):
        if self.is_empty():
            return None

        return self.top.data

if __name__ == "__main__":
    s = Stack()

    s.push(10)
    s.push(20)
    s.push(30)
    print("Top element:", s.peek())
    print(s.pop())
    print(s.pop())
    print("Is stack empty?", s.is_empty())
    print(s.pop())
    print(s.pop())  # Trying to pop from an empty stack