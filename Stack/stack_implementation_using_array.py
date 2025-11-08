class Stack:
    def __init__(self, size):
        self.top = -1
        self.size = size
        self.stack = [0] * size

    def push(self, data):
        if self.is_full():
            return

        self.top += 1
        self.stack[self.top] = data


    def pop(self) -> int:
        if self.is_empty():
            return -1

        popped = self.stack[self.top]
        self.top += -1
        return popped

    def peek(self) -> int:
        if self.is_empty():
            return -1

        return self.stack[self.top]

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == len(self.stack)

    def size(self):
        return len(self.stack)

if __name__ == "__main__":
    s = Stack(5)

    s.push(10)
    s.push(20)
    s.push(30)
    print("Top element:", s.peek())
    s.pop()
    s.pop()
    print("Is stack empty?", s.is_empty())
    s.pop()
    s.pop()  # Trying to pop from an empty stack
